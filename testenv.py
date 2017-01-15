#PYTHON3.5.1 (Anaconda3, 64-BIT);

# improved version of test_env.py

#pygame
import pygame

#pygamepredef, in stdlib
from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

#saved to stdlib for convenience
from backend import dbsave
from lsmods import (char, enemy)

# inside project root (local imports)
import DEVTOOL # not for production
import levelmap as lm
import loadmng
import menu

pygame.init()

root = loadmng.rootdir()

SIZE = width, height = 1000, 700
VER = '1.3a2'
#

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('LS v%s TESTENV' % VER)
clock = pygame.time.Clock()
fps = 30


# FUNCTIONS
def init_entities():
	# this function is level-dependant
	# inner-list format: stdsize, imgpath, ai_model, names, blit_points, screen<NOT NEEDED IN DICTIONARY>
	entities = {}
	ent_dict = {
		'l0_ic00': [[40, 100],
			loadmng.rootdir() + '/resources/images/entity/incoherence.png',
			['l_r', 0, 0, None],
			['INCO', 'Bob'],
			[width - 100, 100]
			],
		'l0_ic01': [[40, 100],
			loadmng.rootdir() + '/resources/images/entity/incoherence.png',
			['l_r', 0, 0, None],
			['INCO', 'Jerry'],
			[width - 200, -200]
			]
	}
	for key in ent_dict.keys():
		entities[key] = enemy.Unit(uid = key,
			stdsize = ent_dict[key][0],
			path = ent_dict[key][1],
			ai_model = ent_dict[key][2],
			name = ent_dict[key][3],
			blit_points = ent_dict[key][4],
			screen = screen)

	return entities

#MAIN LOOP
def main():
	d = dbsave.SaveMaster(rootdir = root)
	menu_obj = menu.Menu(db_obj = d, screen = screen)
	player_w, player_h = 40, 100
	map_w, map_h = 10000, 8000

	x_ch = y_ch = x_speed = y_speed = 0
	move = 5
	speed = 10
	static = 0
	is_shifted = False

	player = char.Char(hearts = [3,3], 
		stamina = [100, 100],
		img_objs = [pygame.image.load(root + '/resources/images/sprite/test_sprite.png'),
			pygame.image.load(root + '/resources/images/stats/heart.png'),
			pygame.image.load(root + '/resources/images/stats/sp_pip.png')],
		blit_points = [[(width / 2) - (player_w / 2), (height / 2) - (player_h / 2)], [0, 0], [0, 0]],
		screen = screen)

	entities = init_entities()

	lmap = lm.Map(lnum = 0,
		lname = 'TESTENV 2',
		slnum = 1,
		slname = 'SUBLEVEL 1',
		dimensions = [map_w, map_h],
		blit_points = [0, 0],
		rootdir = root,
		screen = screen)

	#pmng = DEVTOOL.PointManager(loadmng.rootdir() + '/DEVFOLDER/lvl%d%d_logged_points' % (lmap.lnum, lmap.slnum))
	pmng = DEVTOOL.DEVTool()
	pmng.init_pm(loadmng.rootdir() + '/DEVFOLDER/lvl%d%d_logged_points' % (lmap.lnum, lmap.slnum))

	playing = True
	while playing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					if is_shifted:
						y_speed = speed
					y_ch = move + y_speed
				elif event.key == pygame.K_a:
					if is_shifted:
						x_speed = speed
					x_ch = move + x_speed
				elif event.key == pygame.K_s:
					if is_shifted:
						y_speed = speed
					y_ch = -move - y_speed
				elif event.key == pygame.K_d:
					if is_shifted:
						x_speed = speed
					x_ch = -move - x_speed
				elif event.key == pygame.K_g:
					print("map x: %d\nmap y: %d" % (map_x, map_y))
					pmng.pm_object.append_points([map_x, map_y])
					if is_shifted:
						print('LOGGING %d POINT PAIRS' % pmng.pm_object.lenp())
						pmng.pm_object.write_to_file()
				elif event.key == pygame.K_p:
					menu_obj.pause(player = player,
						lmap = lmap,
						enemy_obj = entities,
						screensize = [width, height])
				elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
					is_shifted = True
				elif event.key == pygame.K_SPACE:
					player.adjust_c_heart(-1)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					y_ch = static
				elif event.key == pygame.K_a:
					x_ch = static
				elif event.key == pygame.K_s:
					y_ch = static
				elif event.key == pygame.K_d:
					x_ch = static
				elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
					is_shifted = False
					x_speed = static
					y_speed = static
				elif event.key == pygame.K_SPACE:
					pass

		#for entity in entities:
		#	entities[entity].ai_path()

		screen.fill(rgb.black)
		lmap.adjust_blit(x_ch, y_ch)
		lmap.blit()
		for entity in entities:
			entities[entity].adjust_blit(x_ch, y_ch)
			entities[entity].ai_path()
			entities[entity].blit()
		player.blit()
		pygame.display.update()
		clock.tick(fps)

main()