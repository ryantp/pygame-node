#PYTHON3.5.1 (Anaconda3, 64-BIT);

# a loading manager for getting the proper level from save files and queuing the proper level

''' this module loads every level module;

in the queue_level function, a level module object will be return for the appropriate lnum.

this function will be called in the main loop of main.py, which will launch the run_appropriate_level function.
the function will run it's course, which will return an lnum and slnum list, along with updated player info (which
will contain some initial-filler information, so that a given sublevel won't have to store too much information
pertaining to the subsequent sublevel / level)'''

import os

# LEVEL MODULES
from levels import (l0,
	l1,
	l2,
	l3,
	l4)

#all future modules such as maps will need a way to hold this rootdir, maybe as a class obj version of a loadmng that holds all
#necessary information
#this module will be used whenever saved locations are accessed, so maybe this module will call all subsequent maps,
#or maybe all levels should be a class themselves
#the main init files (game init info, start screen, main_menu, and MAIN (which could call every subclass as needed)) will be regular files
# there needs to be a main.py, and all modules in subdirs need to be pulled into main.py

def rootdir():
	return os.getcwd().replace('\\', '/')

def queue_level(lnum = None, level_info = [], player_info = [], entity_info = [], required_obj = [],
	optional_obj = [], rootdir = None, screen = None):
	# this if block will determine which level to load
	if lnum == 0:
		return l0.Level0(level_info = level_info,
			player_info = player_info,
			entity_info = entity_info,
			required_obj = required_obj,
			optional_obj = optional_obj,
			rootdir = rootdir,
			screen = screen)
	elif lnum == 1:
		return l1.Level1(level_info = level_info,
			player_info = player_info,
			entity_info = entity_info,
			required_obj = required_obj,
			optional_obj = optional_obj,
			rootdir = rootdir,
			screen = screen)
	elif lnum == 2:
		pass
	elif lnum == 3:
		pass
	elif lnum == 4:
		pass

if __name__ == '__main__':
	pass