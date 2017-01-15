#PYTHON3.5.1 (Anaconda3, 64-BIT);

# separate tool to view db entries -- lsp.db; lsm.db; lsl.db

import os
import sqlite3

#from backend import savedata as sd -- savedata is defunct
from backend import dbsave

VER = "0.2"

os.system('title LSTOOL v%(VER)s' % locals())
datadir = os.getcwd().replace('\\', '/') + '/data/'

d = dbsave.SaveMaster(os.getcwd().replace('\\', '/'))

print("LSTOOL v%(VER)s" % locals())
print("Master Action(s):\n\tr -- read from a database\n\t_read -- custom read function\n\t[ ? ] -- help\n\t[ / ] -- exit the program")

def get_help():
	print("r -- read from a database")
	print("_read -- custom read function")
	print("? -- print this menu")
	print("/ -- exit the program")

def is_valid_table(key):
	tables = {
		'player_data_save': True,
		'player_data_ref': True,
		'entity_data_save': True,
		'levels': True,
	}

	try:
		return tables[key]
	except KeyError:
		return False

def rfsd(tname = None):
	if is_valid_table(tname):
		if tname == 'player_data_save':
			# use d.pds_read
			pass

def parse(args):
	# this function takes a specific format
	# W|id=$L; = WHERE id=lastinput ~~ takes from sd.playersave_ref
	_where = {}
	_select = {}
	for arg in args:
		if arg.startswith('W|'):
			arg.replace('W|', '')
			a = arg.split('=')
			_where[a[0]] = a[1]
		elif arg.startswith('S|'):
			arg.replace('S|', '')
			a = arg.split('=')
			_select[a[0]] = a[0]
		else:
			print("Invalid format")
			return 0

	return _select, _where

def custom_read():
	categories = ['id', 'uid', 'code', 'level_number', 'sublevel_number']
	c1 = '''SELECT %s FROM %s '''
	c2 = '''WHERE %s=?'''
	command = ''
	value = None
	#arg = ''
	args = []
	print("Custom Read\n")
	dbname = input("dbname: ")
	if is_in_use(dbname):
		table = input("table: ")
		if is_valid_table(table):
			print("args:\n")
			while True:
				arg = input("> ")
				if arg == '00':
					break
				args.append(arg)
			if args:
				sel, whe = parse(args)
				for c in categories:
					try:
						if sel[c]:
							c1 = c1 % (sel[c], table)
						elif whe[c]:
							c2 = c2 % (c)
							value = whe[c]
					except KeyError:
						pass
				if c1 and c2:
					command += c1 + c2
				else:
					command += c1
				conn = sqlite3.connect(dbname)
				if value:
					results = conn.execute(command, [value,])
				else:
					results = conn.execute(command)
				conn.close()
			else:
				results = rfsd(dbname, table)
		if table == '/':
			exit()
		else:
			print("Invalid data table name")
	if dbname == '/':
		exit()
	else:
		print("Invalid database name")

	return results

using = True
while using:
	
