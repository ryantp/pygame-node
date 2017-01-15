#PYTHON3.5.1 (Anaconda3, 64-BIT);

'''LEVEL 0; TUTORIAL level.

level_num = 0; level_name = "Home Of Mine"; 
	sublevel_number = 1; sublevel_name = "House"
	sublevel_number = 2; sublevel_name = "Neighborhood"

sublevels = 1

'''

import pygame

from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

from lsmods import pstat
import levelmap as lm

def make_monster_dict(enemy_objs = []):
	results = {}
	for enemy in enemy_objs:
		results[enemy.uid = enemy

	return results

def main(rootdir = None, char_obj = None, map_obj = None, enemy_objs = []):
	monsters = make_monster_dict(enemy_objs)
	del enemy_objs