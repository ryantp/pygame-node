#PYTHON3.5.1 (Anaconda3, 64-BIT);

'''the main hub module for the lost souls game; any and all sub directory modules will be pulled into this file.

	this module is for actual levels and gameplay, not for the start_screen or main_menu; those should be handled in a different 
		module

	this file needs functions to:
		- deploy level modules in subdirs
		- interact with db, pull all necessary info (through loadmng.py)
		- queue the subsequent level when the current level is completed ## maybe through loadmng.py as well

	all level modules will be classes, with sublevel modules

	NOTE:
		Because pygame.display.toggle_fullscreen doesn't work for me, I'm not including it here, and so no fullscreen option
			will be made available (as of 10.6.2016

	'''

import os

import pygame

#pygamepredef, in stdlib
from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

# subdirectories
from backend import dbsave
from lsmods import (char, enemy)

import DEVTOOL # not for production
import levelmap as lmap
import loadmenu as lmenu
import loadmng
import menu
import settings

# LEVELS AND OTHER IN-GAME-GRAPHICAL-RELATED MODULES
import lsinit

##################################################################################
	# SETUP
	#
	# PRESTART
	# Queue the init_startscreen and mainmenue, which should return an _action,
	# 	either 'n', 'c' or 'l' (new game, continue or load number, respectively)
	#
	# these return codes will determine how dbsave.SaveMaster will execute
	#	- n, should trigger a new game, no need to interact with dbsave
	#	- c, dbsave.SaveMaster.continue() # will load lastest save
	#	- #, dbsave.SaveMaster.load_in_order(save_id = #) # will present player with load menu, with a list of save numbers,
	#		# lnum + slnum, lname + slname, and probably blit_points -- or any other identifying info
	#
	# 0> pygame.init()
	#
	# 1> declare the root directory `ROOT` and screen size `SIZE`
	#    declare the INIT_VARIABLES and DB_VARIABLES
	#
	# 2> lsinit -- checks sys.platform
	# 	plays the start screen and present the player with the main menu, which can be accessed on it's own
	#	the main menu will return one of three results [res]: 'n', 'c' or 'l' (`l` being load)
	#
	# 2.5> if _CHO == 'l': menu.load_menu()
	#
	# 3> backend.dbsave needs to go first, which will provide
	# 	the required info for player, levelmap and entities
	#
	# 4> determine _CHO
	###############################################################################

# INITIATE PYGAME
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("\rinitializing pygame: start\b\b\b\b\b", end = "")
	'''###===---DEBUG---===###'''
pygame.init()
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("finish")
	'''###===---DEBUG---===###'''

# rootdir
def rootdir():
	return os.getcwd().replace('\\', '/')

# CONST
ROOT = rootdir() # LS's root directory
SIZE = settings.SIZE # screen size
VER = '1.3.1a1' # version number
PROGRAM_TITLE = 'Lost Soul v%(VER)s' % {'VER': VER} # program's title
SCREEN = pygame.display.set_mode(SIZE) # screen object

pygame.display.set_caption(PROGRAM_TITLE) # setting the caption (title)

CLOCK = pygame.time.Clock() # clock object
FPS = settings.FPS # frames per second

# INIT_VARIABLES
tmp = None # this will hold the return value from lmenu.load_menu(), which is a save id (sid)
_ng = 0 # new game; boolean integer

# DB_VARIABLES
player = [] # long_list of all values held in LSMDBLiteTest.db[player_data_save]
entities = [] # nested list; holds values for every entity that appears on the given sublevel

'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("loading pygame images")
	'''###===---DEBUG---===###'''
# IMAGE VARIABLES
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("\rloading player_sprite: start\b\b\b\b\b", end = "")
	'''###===---DEBUG---===###'''
player_sprite = pygame.image.load(settings.PLAYER_R_IMG['test']) # player's character image object
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("finish")
	print("\rloading hearts: start\b\b\b\b\b", end = "")
	'''###===---DEBUG---===###'''
hearts = pygame.image.load(settings.PLAYER_R_IMG['heart'])
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("finish")
	print("\rloading stamina: start\b\b\b\b\b", end = "")
	'''###===---DEBUG---===###'''
stamina = pygame.image.load(settings.PLAYER_R_IMG['stamina'])
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("finish")
	print("image batch one -- finished")
	'''###===---DEBUG---===###'''

PLAYER_IMG_OBJ = [player_sprite, hearts, stamina] # list containing all the image objects

'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("starting lsinit.main")
	'''###===---DEBUG---===###'''
_CHO = lsinit.main(SIZE, SCREEN) # a fancy `input()` scenario; main_menu will return either l, c, n [load, continue, new]

'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("\rcreating database-save object: start\b\b\b\b\b", end = "")
	'''###===---DEBUG---===###'''
# required_obj[4] -- first to be created
d = dbsave.SaveMaster(ROOT) # database object
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("finish")
	print("\rcreating in-game menu object: start\b\b\b\b\b", end = "")
	'''###===---DEBUG---===###'''
m = menu.Menu(db_obj = d, screen = SCREEN) # master in-game menu object
'''###===---DEBUG---===###'''
if settings.DEBUG:
	print("finish")
	'''###===---DEBUG---===###'''

if _CHO == 'l':
	tmp = lmenu.load_menu(screen = SCREEN) # will return a value for Load Save ID [_]
elif _CHO == 'c':
	tmp = None # in the event of a continue, tmp is None and _ng remains False
else:
	_ng = 1 # new game; tmp is None

# determine _CHO course of action
if tmp and not _ng:
	player, entities = d.load_in_order(tmp) # queues the info from LSMDBLiteTest[player_data_save(id=tmp)]
	if settings.DEBUG:
		print(player) #DEBUG - player contains the id, which is not needed anymore, so do not call player[0], start at [1]
		# as of 10.11.2016, this is not fixed
		print(entities) #DEBUG
	'''because eds_read gathers it's data differently, everything works out fine with it'''
elif not tmp and not _ng:
	player, entities = d.continue_game() # if _CHO == 'c'; continue
elif _ng and not tmp:
	pass # this is new game;
	'''because player and entities are empty lists if the stack goes this way, then the level will launch into a new game \
	this will need to be written into the level modules'''
else:
	# PRE-ALPHA
	print('WTF?! <main.py>[tmp|_ng]') # PRE-ALPHA
	'''in the event of an unforseen option (which shouldn't be possible, as all options are accounted for), this string \
	should never end up popping up but, on the off chance that it does, then the program is going to exit and print out WTF?!'''
	pygame.quit()
	quit() # just in case something unexpected occurs

if player and entities:
	level_info = [player[0][1],
		player[0][2],
		player[0][3],
		player[0][4],
		settings.lmap_bp['%s%s' % (str(player[0][1]), str(player[0][3]))]] # 1 = lnum; 2 = lname; 3 = slnum; 4 = slname
		# 5 = '$lnum$slnum', which gets passed to a blit_point map for any given sublevel
		# this can be moved to each individual level module
	# PLAYER INFO
	player_info = [player[0][9],
		player[0][10],
		player[0][11],
		player[0][12],
		PLAYER_IMG_OBJ,
		[player[0][7], player[0][8]]] # 1 = current-hearts; 2 = total-hearts; 3 = current-stamina; 4 = total-stamina
		# 5 = image objects; 6 = blit_points (list)
	#ENTITY INFO -- entities can be passed as is
else:
	level_info = []
	player_info = []
	# because player-info and level-info was not declared above this block, which would raise an error down the stack

'''NOTES ON REQUIRED_OBJ AND OPTIONAL_OBJ:
the reason why REQUIRED_OBJ contains char.Char, lmap.Map, enemy.Unit is because the level modules are located in subdir's,
which cannot exactly pull a module from a parent directory (at least to my knowledge); this also applies to the dbsave object
which requires ls's rootdir (again, in a child directory, that would throw a monkey wrench), and the menu object, which requires
a dbsave object; it seems like a hassle (to me, anyway), but it doesn't run off any more than that, so for now it works

the OPTIONAL_OBJ list is for development and diagnostic objects (neither of which have been created yet (as of
10.11.2016); the DEVTOOL will allow me to map out points while actually in-game (for getting positions where walls should
be drawn, etc)'''

REQUIRED_OBJ = [char.Char, lmap.Map, enemy.Unit, m, d] 
OPTIONAL_OBJ = []

#level_info = [], player_info = [], entity_info = [], required_obj = [], optional_obj = [], rootdir = None, screen = screen

if player_info:
	if settings.DEBUG:
		print("%(cho)s: MAIN LOOP STARTING" % {
			'cho': _CHO.upper(),
		}) #DEBUG
	# this block is for continue or load
	loop = True
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		######################################################
			# this loadmng.queue_level function will return a
			# level module object; the next line will run
			# level.run_appropriate_level(), which will return
			# a lnum, slnum list, level-info and player-info
			#
			# entity-info will go into the next level iteration
			# as an empty list (since, the new level will have
			# all entities starting in their initial positions)

		level = loadmng.queue_level(lnum = level_info[0],
			level_info = level_info,
			player_info = player_info,
			entity_info = entities,
			required_obj = REQUIRED_OBJ,
			optional_obj = OPTIONAL_OBJ,
			rootdir = ROOT,
			screen = SCREEN)

		if settings.DEBUG:
			print(level)
		Loop = False
		break

		#rLvl_info = level.run_appropriate_level() # will return a value when the level is completed

		pygame.display.update()
		CLOCK.tick(FPS)
else:
	pass
	# this section is for launching a new game

		