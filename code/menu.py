#PYTHON3.5.1 (Anaconda3, 64-BIT);

# basic pause menu

import pygame

from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

import loadmng

ROOT = loadmng.rootdir()

clock = pygame.time.Clock()
fps = 30

#####################
	# TO DO
	# 
	# finish load_menu -- should have a column of seven info slots (probably buttons, for ease of progragmming); it should be
	# navigatable with the middle mouse wheel or with built-in on-screen arrows; then comes the question of how to achieve
	# this -- should it be that the button's msg and return value change as options are scrolled through, or should
	# a dict of button objects, containing their appropriate info, be used?
	# 
	# the dict option seems easiest (ie. most likely to work, as changing obj's blit values seems to not work right),
	# so that will be tested first.
	#
	#################

class Menu(object):


	class LSTool(std4.StdTool):

		def button(self, text, x, y, width, height, inactive, active, fname = None, fsize = 30, fcolor = None, action = None):
			"""Placing a button on the screen"""
			cur = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
			#print(click)
			if x + width > cur[0] > x and y + height > cur[1] > y:
				pygame.draw.rect(self.screen, active, (x, y, width, height))
				if click[0] == 1 and action != None:
					return action, False
						
			else:
				pygame.draw.rect(self.screen, inactive, (x, y, width, height))
			
			self.text_to_button(msg = text,
				color = fcolor,
				buttonx = x,
				buttony = y,
				buttonwidth = width,
				buttonheight = height,
				fname = fname,
				fsize = fsize)

	def __init__(self, db_obj = None, screen = None):
		self.d = db_obj
		self.screen = screen
		self.tool = Menu.LSTool(self.screen)

	def pause(self, player = None, lmap = None, enemy_obj = [], screensize = []):
		# OBJECT INSTANCES: map, enemy_obj, clock, screen;
		#d = dbs.SaveMaster(ROOT)
		#tool = std4.StdTool(screen = screen)
		#block size
		x = 200
		y = 100
		w = screensize[0] - 400
		h = screensize[1] - 200
		rectangle = [x, y, w, h]

		colors = [rgb.dodger_blue, rgb.blue]
		s = 0

		paused = True
		while paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						paused = False
					elif event.key == pygame.K_s:
						if player and lmap and enemy_obj:
							self.d.mass_save(level = [lmap.lnum, lmap.lname],
								sublevel = [lmap.slnum, lmap.slname],
								map_pos = lmap.init_blit_points,
								displace = lmap.blit_points,
								hearts = [player.c_hearts, player.t_hearts],
								sp = [player.c_stamina, player.t_stamina],
								enemy_obj = enemy_obj)
							s += 1
						else:
							pass
					elif event.key == pygame.K_e:
						pygame.quit()
						quit()
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_s:
						s += 1

			if self.screen:
				self.screen.fill(rgb.snow)
				pygame.draw.rect(self.screen, colors[s % 2], rectangle)
				self.tool.message_to_screen(msg = "PAUSED",
					color = rgb.black,
					width = screensize[0],
					height = screensize[1],
					x_displace = 0,
					y_displace = -280,
					fname = 'Tahoma',
					fsize = 40)
				self.tool.message_to_screen(msg = "Press [P] to continue",
					color = rgb.black,
					width = screensize[0],
					height = screensize[1],
					x_displace = 0,
					y_displace = -200,
					fname = 'Tahoma',
					fsize = 30)
				self.tool.message_to_screen(msg = "Press [S] to Save",
					color = rgb.black,
					width = screensize[0],
					height = screensize[1],
					x_displace = 0,
					y_displace = -100,
					fname = 'Tahoma',
					fsize = 30)
				self.tool.message_to_screen(msg = "Press [E] to exit",
					color = rgb.black,
					width = screensize[0],
					height = screensize[1],
					x_displace = 0,
					y_displace = 0,
					fname = 'Tahoma',
					fsize = 30)
				pygame.display.update()
				clock.tick(20)
			else:
				print("No screen")
				pygame.quit()
				quit()
