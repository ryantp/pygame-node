#PYTHON3.5.1 (Anaconda3, 64-BIT);

import loadmng

'''Settings module for PRJ_LS; setup not dissimilar to Django settings module.

	Screen size, FPS, standart map sizes, and all standard settings.

	All sublevel map sizes should be registered here after completion, along with
	all sprite image dimensions.'''

# META var's
DEBUG = True

#screen
SIZE = VW, VH = (1000, 700) # standard, not-fullscreen size

#player-sprite
PLYRDIM = PW, PH = 40, 100 # dimensions for current player-character sprite

#FPS
FPS = 30

# absolute image paths -- STATS
SPRITE_DIR = loadmng.rootdir() + '/resources/images/sprite/'
STATS_DIR = loadmng.rootdir() + '/resources/images/stats/'

PLAYER_R_IMG = {
	'test': SPRITE_DIR + 'test_sprite.png',
	'std': None,
	'heart': STATS_DIR + 'heart.png',
	'stamina': STATS_DIR + 'sp_pip.png',
}



lmap_dim = {
	'01': [2000, 1200],
	'02': [2000, 1200],
	'03': None,
	'11': None,
	'12': None,
	'13': None,
	'21': None,
	'22': None,
	'23': None,
	'31': None,
	'32': None,
	'33': None,
	'41': None,
	'42': None,
	'43': None
}

lmap_bp = {
	'-11': [0, 0],
	'01': [0, 0],
	'02': None,
	'03': None,
	'11': None,
	'12': None,
	'13': None,
	'21': None,
	'22': None,
	'23': None,
	'31': None,
	'32': None,
	'33': None,
	'41': None,
	'42': None,
	'43': None
}

if __name__ == '__main__':
	pass