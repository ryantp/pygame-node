#PYTHON3.5.1 (Anaconda3, 64-BIT);

import pygame

from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

from lsmods import (char, enemy)

#from backend import savedata as _sd
#from backend import dbsave as _sd

import DEVTOOL

import levelmap as lm
import loadmng
import menu

pygame.init()

root = loadmng.rootdir()

width = 1000
height = 700
player_w = 40
player_h = 100

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("LS_TEST_ENV")
ICON = pygame.image.load(root + "/resources/images/icons/lsico_NONTRANS.png")
pygame.display.set_icon(ICON)

clock = pygame.time.Clock()
fps = 30

monster_list = ['l0_ic00']

#player_img_src = "C:/Users/alpha/Desktop/DEV16/ls/src/resources/images/sprite/test_sprite.png"
#player_img = pygame.image.load(player_img_src)

def make_monsters(monster_list = None):
	monster_list
	stdsize = [40, 100]
	monsters = {}
	for monster in monster_list:
		monsters[monster] = enemy.Unit(uid = monster,
			stdsize = stdsize,
			path = root + '/resources/images/entity/incoherence.png',
			ai_model = ['l_r', 0, 0, None],
			name = ['INCO', 'Bob'],
			blit_points = [width - 100, 100],
			screen = screen)

	return monsters

def main():
	menu_obj = menu.Menu(screen)
	player_blit_points = ((width / 2) - (player_w / 2), (height / 2) - (player_h / 2))
	monsters = make_monsters(monster_list)

	map_w = 10000
	map_h = 8000
	map_x = 0
	map_y = 0
	
	x_ch = 0
	y_ch = 0

	x_speed = 0
	y_speed = 0

	move = 5
	speed = 10
	static = 0

	is_shifted = False

	player = char.Char(hearts = [3, 3],
		stamina = [100, 100],
		img_objs = [pygame.image.load(root + '/resources/images/sprite/test_sprite.png'),
			pygame.image.load(root + '/resources/images/stats/heart.png'),
			pygame.image.load(root + '/resources/images/stats/sp_pip.png')],
		blit_points = [player_blit_points, [0, 0], [0, 0]],
		screen = screen)
	
	lmap = lm.Map(lnum = 0,
		lname = 'Test Map',
		slnum = 1,
		slname = 'Zero',
		blit_points = [map_x, map_y],
		rootdir = loadmng.rootdir(),
		screen = screen)

	#heart = pstat.Heart(blit_points = [0, 0], cquantity = 6, tquantity = 2, is_strong = False, screen = screen)
	#sp = pstat.Stamina(blit_points = [0, 0], y_displace = heart.get_stdsize()[1], cquantity = 100, tquantity = 100, screen = screen)

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
					print("map x: %d\nmap y: %d" % (lmap.blit_points[0], lmap.blit_points[1]))
				elif event.key == pygame.K_q:
					print('LOGGING %d POINT PAIRS' % pmng.lenp())
				elif event.key == pygame.K_p:
					menu_obj.pause(player = player,
						lmap = lmap,
						enemy_obj = monsters,
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

		if is_shifted:
			if x_speed is not static or y_speed is not static:
				player.adjust_c_stamina(-1)

		if not is_shifted:
			x_speed = static
			y_speed = static

		for monster in monster_list:
			monsters[monster].ai_path()

		screen.fill(rgb.black)
		lmap.adjust_blit(x_ch, y_ch)
		lmap.blit()
		for monster in monster_list:
			monsters[monster].adjust_blit(x_ch, y_ch)
			monsters[monster].ai_path()
			monsters[monster].blit()
		player.blit()
		#player.blit_heart()
		#player.blit_sp()
		pygame.display.update()
		clock.tick(fps)

main()