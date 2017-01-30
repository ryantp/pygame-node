#PYTHON3.5.1 (Anaconda3, 64-BIT);

import datetime
import os
import sqlite3


class SaveMaster(object):
	'''SaveMaster -- object for data persistance; imporovement upon savedata.py;'''

	#db table names

	def __init__(self, rootdir):
		pass

	# INIT(1)
	def get_time(self):
		return "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) # datestamp

	def check_a_dir(self):
		pass

	def make_dir(self):
		pass

	def check_for_tables(self):
		pass

	# CREATE TABLES
	def pds_init(self):
		pass

	def pdr_init(self):
		pass

	def eds_init(self):
		pass

	def lvls_init(self):
		pass

	def init_tables(self):
		'''uses predefined variables; doesn't require cursor() object'''
		self.make_dir()
		self.pds_init()
		self.pdr_init()
		self.eds_init()
		self.lvls_init()

	def reinit_tables(self):
		pass

	# INIT(2)
	def fill_lvls_info():
		pass

	# data saving functions
	def pds_save(self, level = [], sublevel = [], map_pos = [], displace = [], hearts = [], sp = [], ds = None):
		pass

	def pdr_update(self):
		pass

	def eds_save(self, enemy_obj = {}):
		pass

	def mass_save(self, level = [], sublevel = [], map_pos = [], displace = [], hearts = [], sp = [], enemy_obj = {}):
		pass

	# data reading functions
	def pds_read(self, save_key = None):
		pass

	def read_sid(self):
		pass

	def pdr_read(self):
		pass

	def eds_read(self, save_key = None):
		pass

	def continue_game(self):
		pass

	def load_in_order(self, save_id = None):
    	pass

	# DEVELOPMENT USE ONLY
	def _read_all(self):
        pass



if __name__ == '__main__':
	pass