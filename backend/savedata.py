#PYTHON3.5.1 (Anaconda3, 64-BIT);

# saving the game, loading data, table creation, etc.

import os
import sqlite3 as sql

'''these functions all revolve around player-related information'''

def table_exists(dbname = None, savefile_name = None):
	command = "SELECT name FROM sqlite_master WHERE type='table' AND name='%(savefile_name)s';" % locals()
	conn = sql.connect(dbname)
	result = conn.execute(command)
	results = None
	for r in result:
		results = r[0]
	print(results)
	if savefile_name == results:
		return True
	else:
		return False

def create_ref_table(dbname = None, savefile_name = None):
	# init with create_savefile_table
	# use with read_f_savefile; last_save_id == id (pk/ai)
	if table_exists(dbname = dbname, savefile_name = savefile_name + '_ref'):
		pass
	else:
		try:
			command = 'CREATE TABLE "%(savefile_name)s_ref" ("code" varchar(10) NOT NULL, "last_save_id" integer NOT NULL);' % locals()
			conn = sql.connect(dbname)
			conn.execute(command)
			#conn.close()
			conn.execute("INSERT INTO %(savefile_name)s_ref (code, last_save_id) VALUES (?,?)", ('psr_01', 1))
			conn.commit()
		except sql.OperationalError:
			pass
		finally:
			conn.close()

def update_ref_table(dbname = None, savefile_name = None, fk = None):
	command = '''UPDATE %(savefile_name)s_ref SET last_save_id=? WHERE code="psr_01"''' % locals()
	conn = sql.connect(dbname)
	conn.execute(command, (fk,))
	conn.commit()
	conn.close()

def create_savefile_table(dbname = None, savefile_name = None):
	if table_exists(dbname = dbname, savefile_name = savefile_name):
		pass
	else:
		command = 'CREATE TABLE "%(savefile_name)s" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "level_number" integer NOT NULL, \
		"level_name" varchar(200) NOT NULL, "sublevel_number" integer NOT NULL, "sublevel_name" varchar(200) NOT NULL, \
		"map_position_x" integer NOT NULL, "map_position_y" integer NOT NULL, "map_x_displace" integer NOT NULL, "map_y_displace" integer NOT NULL, \
		"current_hearts" real NOT NULL, "total_hearts" integer NOT NULL, "current_stamina_points" real NOT NULL, \
		"total_stamina_points" integer NOT NULL)' % locals()

		'''NOTES:
			- id = th unique id for the save file; player may load old saves
			- level_number = the number of the master level
			- level_name = the name of the master level; for in-game representation
			- sublevel_number = the number of the sublevel
			- sublevel_name = the name of the sublevel; for in-game representation
			- map_position_x = the initial blit_point(x) of the sublevel
			- map_position_y = the initial blit_point(y) of the sublevel
			- map_x_displace = the current blit_point(x) of the sublevel
			- map_y_displace = the current blit_point(y) of the sublevel
			- current_hearts = the current number of hearts a player has
			- total_hearts = the total number of hearts a player can have
			- current_stamina = the current amount of stamina a player has
			- total_stamina = the total amount of stamina a player can have
			'''
		try:
			conn = sql.connect(dbname)
			conn.execute(command)
		except sql.OperationalError:
			pass
		finally:
			conn.close()

def save_to_savefile(dbname = None, savefile_name = None, level_info = [], sublevel_info = [], map_position = [], diplace = [], hearts = [], sp = []):
	create_ref_table(dbname = dbname, savefile_name = savefile_name)
	create_savefile_table(dbname = dbname, savefile_name = savefile_name)
	values = (level_info[0],
		level_info[1],
		sublevel_info[0],
		sublevel_info[1],
		map_position[0],
		map_position[1],
		diplace[0],
		diplace[1],
		hearts[0],
		hearts[1],
		sp[0],
		sp[1])
	command = 'INSERT INTO %(savefile_name)s (level_number, level_name, sublevel_number, sublevel_name, map_position_x, map_position_y, \
	map_x_displace, map_y_displace, current_hearts, total_hearts, current_stamina_points, total_stamina_points) VALUES \
	(?,?,?,?,?,?,?,?,?,?,?,?)' % locals()
	conn = sql.connect(dbname)
	cur = conn.cursor()
	cur.execute(command, values)
	conn.commit()
	fk = cur.lastrowid
	conn.close()

	update_ref_table(dbname = dbname, savefile_name = savefile_name, fk = fk)

	return fk

def read_from_savefile(dbname = None, savefile_name = None):
	results = []
	command = 'SELECT * FROM %(savefile_name)s' % locals()
	conn = sql.connect(dbname)
	result = conn.execute(command)
	for r in result:
		results.append(r)
	conn.close()

	return results

'''the following functions will deal with level-related information, mostly enemy positions, which should be schemed similaryly to
	the above functions, but it will have to be tweaked to accomodate the needs of enemy units;

	level name and number (and sublevel name and number) will not be required, or can be extrapolated from the player db if needed, but an
	entry for every enemy unit will be required, along with a unique id (no "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT should be needed,
	only the uid). Since enemies can't really be killed, the db needs to be populated with units, units onscreen will be handled by the
	program (offscreen units won't have processing power wasted on them), but all the unit's info will need to be populated at every
	save.

	if a unit is agro (like AJF_C (Agro JF Cruelty) should be in sl4.3), then that unit will have to be handled, but other than AJF_C, not
	many units will ever go _that_ agro.

	the following functions interact with a different database file'''

# to test whether the table exists, use table_exists()

def create_table_m(dbname = None, savefile_name = None, level_info = []):
	if table_exists(dbname = dbname, savefile_name = savefile_name):
		pass
	else:
		level_string = str(level_info[0]) + str(level_info[1])
		command = 'CREATE TABLE "%(savefile_name)s_lvl%(level_string)s" ("id" integer NOT NULL, \
		"uid" varchar(12) NOT NULL, "map_x" integer NOT NULL, "mapy_y" integer NOT NULL, "map_x_displace" integer NOT NULL, \
		"map_y_displace" integer NOT NULL, "path_type" varchar(20) NOT NULL, "is_agro" integer NOT NULL, "ability" varchar(50) NULL, \
		"type_name" varchar(50) NOT NULL, "personal_name" varchar(50) NULL, "is_boss" integer NOT NULL);' % locals()
		try:
			conn = sql.connect(dbname)
			conn.execute(command)
		except sql.OperationalError:
			pass
		finally:
			conn.close()

def save_to_m(dbname = None, savefile_name = None, level_info = [], enemy_obj = [], fk = None):
	create_table_m(dbname = dbname, savefile_name = savefile_name, level_info = level_info)
	level_string = str(level_info[0]) + str(level_info[1])
	conn = sql.connect(dbname)
	command = '''INSERT INTO %(savefile_name)s_lvl%(level_string)s (id, uid, map_x, map_y, map_x_displace, map_y_displace, path_type, is_agro, ability, \
	type_name, personal_name, is_boss) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''' % locals()
	for unit in enemy_obj:
		values = (fk,
			unit.uid,
			unit.init_blit_point[0],
			unit.init_blit_point[1],
			unit.blit_point[0],
			unit.blit_point[1],
			unit.movement_path,
			unit.is_agro,
			unit.ability,
			unit.type_name,
			unit.personal_name,
			unit.is_boss)
		conn.execute(command, values)
		conn.commit()
	conn.close()

def read_from_m(dbname = None, savefile_name = None, level_info = None):
	command = 'SELECT * FROM %(savefile_name)s_lvl%(level_info)s' % locals()
	conn = sql.connect(dbname)
	results_big = conn.execute(command)
	conn.close()

	results = []

	for r in results_big:
		results.append(r)

	return results

'''the following functions deal with the levels themselves'''

def create_level_tables(dbname = None):
	table_names = ['lvl01', 'lvl02', 'lvl11', 'lvl12', 'lvl13', 'lvl21', 'lvl22', 'lvl23', 'lvl31',
		'lvl32', 'lvl33', 'lvl41', 'lvl42', 'lvl43']

	conn = sql.connect(dbname)

	for name in table_names:
		if table_exists(dbname = dbname, savefile_name = name):
			pass
		else:
			command = '''CREATE TABLE "%s" ("level_id" varchar(5) NOT NULL, "start_x" integer NOT NULL, "start_y" integer NOT NULL, \
			"map_width" integer NOT NULL, "Map_height" integer NOT NULL, "theme" varchar(20) NOT NULL, "enemy_type" varchar(100) NOT NULL, \
			"number_of_enemies" integer NOT NULL)''' % name
			try:
				conn.execute(command)
			except sql.OperationalError:
				pass
			finally:
				conn.close()

def read_level_table(dbname = None, table_name = None):
	command = 'SELECT * FROM %(table_name)s' % locals()
	conn = sql.connect(dbname)
	results = conn.execute(command)
	conn.close()

	return results

if __name__ == '__main__':
	pass