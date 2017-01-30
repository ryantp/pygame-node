#PYTHON3.5.1 (Anaconda3, 64-BIT);

import datetime
import os
import sqlite3


class SaveMaster(object):
	'''SaveMaster -- object for data permanance; imporovement upon savedata.py;'''

	#db table names

	def __init__(self, rootdir):
		'''
		self.data = rootdir + '/data' # the directory that holds the database
		self._db = self.data + '/LSMDBLiteTest.db' # the actual db file
		"""self.lsp = rootdir + '/data/lsp.db' # passed through main, using loadmng
		self.lsm = rootdir + '/data/lsm.db'
		self.lsl = rootdir + '/data/lsl.db'"""

		#foreign key, to use with the referrence table
		self.fk = None # will be extrapolated from lsp.db as the lastrowid

		if not self.check_for_tables():
			self.init_tables()
		'''
		pass

	# INIT(1)
	def get_time(self):
		"""
		return "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) # datestamp
		"""
		pass

	def check_a_dir(self):
		"""
		if os.path.isdir(self.data):
			return 1
		else:
			return 0
		"""
		pass

	def make_dir(self):
		"""
		if self.check_a_dir():
			pass
		else:
			os.mkdir(self.data)
		"""
		pass

	def check_for_tables(self):
		"""
		'''checks for the existance of tables; uses cursor() object'''
		# player_data_save table
		command = "SELECT name FROM sqlite_master WHERE type='table' AND name='player_data_save'"
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()

		result = cur.execute(command).fetchall()
		if result:
			pass
		else:
			return False

		del command, cur, result

		# player_data_ref table
		command = "SELECT name FROM sqlite_master WHERE type='table' AND name='player_data_ref'"
		cur = conn.cursor()
		result = cur.execute(command).fetchall()
		if result:
			pass
		else:
			return False

		conn.close()
		del command, conn, cur, result

		# entity_data_save table
		command = "SELECT name FROM sqlite_master WHERE type='table' AND name='entity_data_save'"
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()

		result = cur.execute(command).fetchall()
		if result:
			pass
		else:
			return False

		conn.close()
		del command, conn, cur, result

		# level tables
		command = "SELECT name FROM sqlite_master WHERE type='table' AND name='levels'"
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		result = cur.execute(command).fetchall()
		if result:
			pass			
		else:
			return False
		conn.close()
		del command, conn, cur, result

		return True
		"""
		pass

	# CREATE TABLES
	def pds_init(self):
		"""
		# player_data_save table
		# 13 total columns, only 12 need to be passed
		command = '''CREATE TABLE "player_data_save" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
		"level_number" integer NOT NULL, \
		"level_name" varchar(200) NOT NULL, "sublevel_number" integer NOT NULL, "sublevel_name" varchar(200) NOT NULL, \
		"map_position_x" integer NOT NULL, "map_position_y" integer NOT NULL, "map_x_displace" integer NOT NULL, \
		"map_y_displace" integer NOT NULL, \
		"current_hearts" integer NOT NULL, "total_hearts" integer NOT NULL, "current_stamina_points" integer NOT NULL, \
		"total_stamina_points" integer NOT NULL, "datestamp" varchar(50) NOT NULL)'''
		conn = sqlite3.connect(self._db) # connect to data/lsp.db -- Lost Soul Player Database
		try:
			conn.execute(command)
		except Exception as exc:
			print('init_pds')
			print(str(exc))
		finally:
			conn.close()
		"""
		pass

	def pdr_init(self):
		"""
		# player_data_ref table
		# Lost Soul will only support one player's save progress, but will allow loading previous save points
		# 2 total columns, only one needs to be updated (last_save_id)
		command = '''CREATE TABLE "player_data_ref" ("code" varchar(10) NOT NULL, "last_save_id" integer NOT NULL)'''
		conn = sqlite3.connect(self._db) # connect (again) to data/lsp.db -- Lost Soul Player Database
		try:
			conn.execute(command)
			conn.execute("INSERT INTO player_data_ref (code, last_save_id) VALUES ('lspdr_01', 1)")
			conn.commit()
		except Exception as exc:
			print('init_pdr')
			print(str(exc))
		finally:
			conn.close()
		"""
		pass

	def eds_init(self):
		"""
		# entity_data_save table; connects to a different database!
		# id is a foreign key; does not record level / sublevel information, which will be gathered from player_data_save
		command = '''CREATE TABLE "entity_data_save" ("id" integer NOT NULL, \
		"uid" varchar(12) NOT NULL, "map_x" integer NOT NULL, "map_y" integer NOT NULL, "map_x_displace" integer NOT NULL, \
		"map_y_displace" integer NOT NULL, "path_type" varchar(20) NOT NULL, "is_agro" integer NOT NULL, "ability" varchar(50) NULL, \
		"type_name" varchar(50) NOT NULL, "personal_name" varchar(50) NULL, "is_boss" integer NOT NULL);'''
		conn = sqlite3.connect(self._db) # connect to data/lsm.db -- Lost Soul Monster Database
		try:
			conn.execute(command)
		except Exception as exc:
			print('init_eds')
			print(str(exc))
		finally:
			conn.close()"""
		pass

	def lvls_init(self):
		"""
		# lvl<#> tables; connects to a different database!
		# level_id is a combination of level_number and sublevel_number (without any punctuation marks, like `11` (level 1, sublevel 1))
		conn = sqlite3.connect(self._db)
		command = '''CREATE TABLE "levels" ("level_id" varchar(5) NOT NULL, "start_x" integer NOT NULL, "start_y" integer NOT NULL, \
		"map_width" integer NOT NULL, "Map_height" integer NOT NULL, "theme" varchar(20) NOT NULL, "enemy_type" varchar(100) NOT NULL, \
		"number_of_enemies" integer NOT NULL)''' # easiest way to do this
		try:
			conn.execute(command)
		except Exception as exc:
			print('init_levels')
			print(str(exc))
		finally:
			conn.close()
			"""
		pass

	def init_tables(self):
		"""
		'''uses predefined variables; doesn't require cursor() object'''
		self.make_dir()
		self.pds_init()
		self.pdr_init()
		self.eds_init()
		self.lvls_init()"""
		pass

	def reinit_tables(self):
		"""
		# this method is ONLY FOR NEW GAMES
		if self.check_a_dir():
			if os.path.exists(self._db):
				os.remove(self._db)
			else:
				pass
		else:
			self.make_dir()
		self.init_tables()
		"""
		pass

	# INIT(2)
	def fill_lvls_info():
		pass

	# data saving functions
	def pds_save(self, level = [], sublevel = [], map_pos = [], displace = [], hearts = [], sp = [], ds = None):
		# level = [lnum, lname]
		# sublevel = [slnum, slname]
		# map_pos = [init_map_x, init_map_y]
		# displace = [map_x, map_y]
		# hearts = [c_hearts, t_hearts]
		# sp = [c_stamina, t_stamina]
		# ds = datestamp
		if ds:
			pass
		else:
			ds = self.get_time() # for redundancy
		command = '''INSERT INTO player_data_save (level_number, level_name, sublevel_number, sublevel_name, map_position_x, \
		map_position_y, map_x_displace, map_y_displace, current_hearts, total_hearts, current_stamina_points, \
		total_stamina_points, datestamp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
		values = [level[0],
			level[1],
			sublevel[0],
			sublevel[1],
			map_pos[0],
			map_pos[1],
			displace[0],
			displace[1],
			hearts[0],
			hearts[1],
			sp[0],
			sp[1],
			ds]

		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		try:
			cur.execute(command, values)
			conn.commit()
			self.fk = cur.lastrowid
		except Exception as exc:
			print('pds_save')
			print(str(exc))
		finally:
			conn.close()

	def pdr_update(self):
		"""
		# requires self.fk, which should be udpated by pds_save()
		command = "UPDATE player_data_ref SET last_save_id=%d WHERE code='lspdr_01'" % self.fk
		conn = sqlite3.connect(self._db)
		try:
			conn.execute(command)
			conn.commit()
		except Exception as exc:
			print('pdr_update')
			print(str(exc))
		finally:
			conn.close()"""
		pass

	def eds_save(self, enemy_obj = {}):
		"""
		keys = enemy_obj.keys()
		command = '''INSERT INTO entity_data_save (id, uid, map_x, map_y, map_x_displace, map_y_displace, path_type, is_agro, ability, \
		type_name, personal_name, is_boss) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
		conn = sqlite3.connect(self._db)
		for key in keys:
			values = [self.fk,
				enemy_obj[key].uid,
				enemy_obj[key].init_blit_points[0],
				enemy_obj[key].init_blit_points[1],
				enemy_obj[key].blit_points[0],
				enemy_obj[key].blit_points[1],
				enemy_obj[key].movement_path,
				enemy_obj[key].is_agro,
				enemy_obj[key].ability,
				enemy_obj[key].type_name,
				enemy_obj[key].personal_name,
				enemy_obj[key].is_boss]
			try:
				conn.execute(command, values)
				conn.commit()
			except Exception as exc:
				print('eds_save -- %s' % key)
				print(str(exc))

		conn.close()"""
		pass

	def mass_save(self, level = [], sublevel = [], map_pos = [], displace = [], hearts = [], sp = [], enemy_obj = {}):
		"""
		'''saves to all required databases'''
		# by virtue of how Lost Soul operates, player_data_save, player_data_ref and entity_data_save will need to be updated
		# at once; entity_data_save is dependant on player_data_save's id/pk, which will be stored in player_data_ref
		self.pds_save(level = level,
			sublevel = sublevel,
			map_pos = map_pos,
			displace = displace,
			hearts = hearts,
			sp = sp,
			ds = self.get_time())
		self.pdr_update()
		self.eds_save(enemy_obj = enemy_obj)
		"""
		pass

	# data reading functions
	def pds_read(self, save_key = None):
		"""
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT * FROM player_data_save WHERE id="%d"''' % save_key
		player = []
		try:
			# perform unpacking in the try loop
			results = cur.execute(command).fetchall() # if a list/tuple isn't passed,
			#the execute function tends to not work properly
			#print(results)
			i = 0
			for result in results:
				player.append(result)
				i += 1
		except Exception as exc:
			print('pds_read: pds.data')
			print(str(exc))
		finally:
			conn.close()
			del result, results

		#return sid, [lnum, lname], [slnum, slname], [imap_x, imap_y], [cmap_x, cmap_x], [c_hearts, t_hearts], [c_stamina, t_stamina],
		#	datestamp
		#print('dbsave.SaveMaster.pds_read>> ', end = '')
		#print(player)
		return player
		"""
		pass

	def read_sid(self):
		"""
		# works; NOTE: don't initiate lists on the same line; things get wonky
		sid = []
		uds = []
		lname = []
		slname = []
		lnum = []
		slnum = []

		# first step -- getting the pk id's from pds
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT id FROM player_data_save'''
		
		try:
			results = cur.execute(command).fetchall() # should get every sid in pds
			for result in results:
				sid.append(result[0])
		except Exception as exc:
			print('read_sid <command1>[sid]: pds.data')
			print(str(exc))
		finally:
			conn.close()
		
		del command, conn, cur, result, results

		# second step -- getting the unique datestamp
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT datestamp FROM player_data_save'''

		try:
			results = cur.execute(command).fetchall()
			for result in results:
				uds.append(result[0])
		except Exception as exc:
			print('read_sid <command2>[uds]: pds.data')
			print(str(exc))
		finally:
			conn.close()

		del command, conn, cur, result, results

		# third step -- getting the level_name
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT level_name FROM player_data_save'''

		try:
			results = cur.execute(command).fetchall()
			for result in results:
				lname.append(result[0])
		except Exception as exc:
			print('read_sid <command3>[lname]: pds.data')
			print(str(exc))
		finally:
			conn.close()

		del command, conn, cur, result, results

		# fourth step -- getting the sublevel_name
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT sublevel_name FROM player_data_save'''

		try:
			results = cur.execute(command)
			for result in results:
				slname.append(result[0])
		except Exception as exc:
			print('read_sid <command4>[slname]: pds.data')
			print(str(exc))

		del command, conn, cur, result, results

		# fifth step -- getting the level_number
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT level_number FROM player_data_save'''

		try:
			results = cur.execute(command)
			for result in results:
				lnum.append(result[0])
		except Exception as exc:
			print('read_sid <command5>[lnum]: pds.data')
			print(str(exc))

		del command, conn, cur, result, results

		# sixth step -- getting the sublevel_number
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT sublevel_number FROM player_data_save'''

		try:
			results = cur.execute(command)
			for result in results:
				slnum.append(result[0])
		except Exception as exc:
			print('read_sid <command6>[slnum]: pds.data')
			print(str(exc))

		return sid, uds, lname, lnum, slname, slnum"""
		pass

	def pdr_read(self):
		"""
		# first, get pdr.last_save_id
		command = '''SELECT last_save_id FROM player_data_ref WHERE code="lspdr_01"'''
		# connect to lsp.db
		conn = sqlite3.connect(self._db)
		# no cursor required
		try:
			save_key = conn.execute(command).fetchall()
		except Exception as exc:
			print('load_in_order: pdr.last_save_id')
			print(str(exc))
		finally:
			conn.close()

		if (int(save_key[0][0])):
			return save_key[0][0]
		else:
			return 0
		"""
		pass

	def eds_read(self, save_key = None):
		"""
		# will require a for loop to iterate through all entries
		mlist = [] # Master List
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()
		command = '''SELECT * FROM entity_data_save WHERE id="%d"''' % save_key
		try:
			results = cur.execute(command).fetchall()
			#print(results)
			for result in results:
				elist = []
				_ = result[0] # pdr.last_save_id
				elist.append(result[1]) # uid
				elist.append(result[2]) # imap_x
				elist.append(result[3]) # imap_y
				elist.append(result[4]) # cmap_x
				elist.append(result[5]) # cmap_y
				elist.append(result[6]) # path_type
				elist.append(result[7]) # is_agro
				elist.append(result[8]) # ability
				elist.append(result[9]) # type_name
				elist.append(result[10]) # personal_name
				elist.append(result[11]) # is_boss
				mlist.append(elist)
		except Exception as exc:
			print('eds_read')
			print(str(exc))
		finally:
			conn.close()
			del result, results

		return mlist"""
		pass

	def continue_game(self):
		'''
		save_key = self.pdr_read()
		if int(save_key):
			player_data = self.pds_read(save_key)
			entity_data = self.eds_read(save_key)

		return player_data, entity_data # both are long_lists
		'''
		pass

	def load_in_order(self, save_id = None):
		"""'''queue a save instance:
			- pds_data:
				- id 					# pk autoincrement; used to queue the data, through pdr
				- level_number*			# REQUIRED
				- level_name
				- sublevel_number*		# REQUIRED
				- sublevel_name
				- map_position_x 		# initial blit
				- map_position_y 		# initial blit
				- map_x_displace 		# current blit
				- map_y_displace 		# current blit
				- c_heart
				- t_heart
				- c_stamina
				- t_stamina
				- datestamp 			# datestamp is a string
			- eds_data:
				- id					# fk -> pds.id
				- uid					# enemy.unit's unique id
				- map_x 				# initial blit
				- map_y 				# initial blit
				- map_x_displace 		# current blit
				- map_y_displace 		# current blit
				- path_type 			# how this unit is supposed to move within the map
				- is_agro 				# is this unit aggressive towards the player
				- ability				# special ability that this unit possesses
				- type_name 			# type of entity this unit is supposed to be
				- personal_name	 		# unit's personal name, used for ingame purposes; example, 'Bob', 'Pride Entity';
										# personal_name can be a `human_name` or a title (see above), but personal_name is used to
										# identify that specific unit in-game when they interact with the player directly
				- is_boss 				# is this unit a boss entity
			########################################################
			- pdr_data:
				- code					# lspdr_01; Lost Soul Player Data Referrence - 01; ls is only one-player
				- last_save_id			# fk -> pds.id; this is needed to pull eds_data
			########################################################
			- 
			'''
		# save_id will replace pdr.last_save_id
		# if no save_id is provided (like in a continue function), then pdr.last_save_id is called
		try:
			player_data = self.pds_read(save_id)
		except Exception as exc:
			print('load_in_order: pds_read')
			print(str(exc))
		
		try:
			entity_data = self.eds_read(save_id)
		except Exception as exc:
			print('load_in_order: eds_read')
			print(str(exc))

		return player_data, entity_data # both are long_lists"""
        pass

	# DEVELOPMENT USE ONLY
	def _read_all(self):
        # example
		'''"""this is basically a dumping function, it's target will be a text file,
		just so that the sheer amount of (potential) data can be presented
		WORKS @10.11.2016"""
		EQ_SPAN = 40
		WTFILE = self.data + '/datadump.txt'

		_all_player = []
		_all_entity = []

		HEADER = '<' + '=' * EQ_SPAN + '>'
		FOOTER = '\n<' + '=' * EQ_SPAN + '>'
		
		# setup
		if os.path.exists(WTFILE):
			with open(WTFILE, 'w') as f:
				pass
			f.close()
			del f
		else:
			with open(WTFILE, 'w') as f:
				pass
			f.close()
			del f

		with open(WTFILE, 'a') as f:
			f.write(HEADER)
			f.write('\n\n' + '=' * 20 + 'Player Data' + '=' * 20 + '\n\n')
			f.close()
			del f
			del HEADER # clear that memory

		# db vars
		conn = sqlite3.connect(self._db)
		cur = conn.cursor()

		# first, collect _all_player
		command = 'SELECT * FROM player_data_save'
		results = cur.execute(command).fetchall()
		
		for result in results:
			_player = []
			for r in result:
				_player.append(r)
			_all_player.append(_player)

		del command
		del r
		del result
		del results

		for p in _all_player:
			_player_string = 'id: %(id)d\
			\nlevel_number: %(lnum)d\
			\nlevel_name: %(lname)s\
			\nsublevel_number: %(slnum)d\
			\nsublevel_name: %(slname)s\
			\nmap_position_x: %(mpx)d\
			\nmap_position_y: %(mpy)d\
			\nmap_x_displace: %(mxd)d\
			\nmap_y_displace: %(myd)d\
			\ncurrent_hearts: %(ch)d\
			\ntotal_hearts: %(th)d\
			\ncurrent_stamina: %(cs)d\
			\ntotal_stamina: %(ts)d\
			\ndatestamp: %(ds)s\n\n' % {
				'id': p[0],
				'lnum': p[1],
				'lname': p[2],
				'slnum': p[3],
				'slname': p[4],
				'mpx': p[5],
				'mpy': p[6],
				'mxd': p[7],
				'myd': p[8],
				'ch': p[9],
				'th': p[10],
				'cs': p[11],
				'ts': p[12],
				'ds': p[13]
			}
			with open(WTFILE, 'a') as f:
				f.write(_player_string)
				f.close()
				del f
                        
                        # this is an example from a local project
                        pass

		with open(WTFILE, 'a') as f:
			f.write('\n' + '=' * 20 + 'Entity Data' + '=' * 20 + '\n\n')
			f.close()
			del f

		del _all_player
		del _player
		del _player_string
		del p

		# second, collect _all_entity
		command = 'SELECT * FROM entity_data_save'
		results = cur.execute(command).fetchall()
		for result in results:
			_entity = []
			for r in result:
				_entity.append(r)
			_all_entity.append(_entity)

			#del command
		"""del r
		del result
		del results"""

		for e in _all_entity:
			_entity_string = 'id: %(id)d\
			\nuid: %(uid)s\
			\nmap_x: %(mx)d\
			\nmap_y: %(my)d\
			\nmap_x_displace: %(mxd)d\
			\nmap_y_displace: %(myd)d\
			\npath_type: %(pt)s\
			\nis_agro: %(ia)d\
			\nability: %(abl)s\
			\ntype_name: %(tn)s\
			\npersonal_name: %(pn)s\
			\nis_boss: %(ib)d\n\n' % {
				'id': e[0],
				'uid': e[1],
				'mx': e[2],
				'my': e[3],
				'mxd': e[4],
				'myd': e[5],
				'pt': e[6],
				'ia': e[7],
				'abl': e[8],
				'tn': e[9],
				'pn': e[10],
				'ib': e[11]
			}

		with open(WTFILE, 'a') as f:
			f.write(_entity_string)
			f.close()
			del f

		del _all_entity
		del _entity
		del _entity_string
		del e

		with open(WTFILE, 'a') as f:
			f.write('\n')
			f.write(FOOTER)
			f.close()
			del f 

		print('FINISHED @ %s' % WTFILE)'''
        pass



if __name__ == '__main__':
	pass