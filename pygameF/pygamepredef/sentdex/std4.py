#!C:\Anaconda3

import pygame
from pygame.locals import *


'''
	##fonts
	ssmall_font = pygame.font.SysFont("Arial", 15)
	small_font = pygame.font.SysFont("Arial", 25)
	med_font = pygame.font.SysFont("Arial", 40)
	lar_font = pygame.font.SysFont("Arial", 70)
	imp_font = pygame.font.SysFont("Impact", 40)
	#In Game Fonts
	ig_speak_font = pygame.font.SysFont("Arial", 20)
	ig_header_font = pygame.font.SysFont("Arial", 30)
	ig_title_font = pygame.font.SysFont("Calibri", 40)'''


class StdTool(object):

	def __init__(self, screen):
		pygame.init()
		self.screen = screen

	def text_objects(self, fname, fsize, msg, color):
		"""Text Objects: for calling the defined fonts"""
		font = pygame.font.SysFont(fname, fsize)
		text_surface = font.render(msg, True, color)
		return text_surface, text_surface.get_rect()


	def text_obj2(self, fname, fsize, msg, color):
		font = pygame.font.SysFont(fname, fsize)
		text_surface = font.render(msg, True, color)
		return text_surface

	def message_to_screen(self, msg, color, width, height, x_displace = 0, y_displace = 0, fname = None, fsize = 30):
		"""displaying a message to the screen"""
		textSurf, textRect = self.text_objects(fname = fname, fsize = fsize, msg = msg, color = color)
		textRect.center = (width /2) + x_displace, (height / 2) + y_displace
		self.screen.blit(textSurf, textRect)

	def button(self, text, x, y, width, height, inactive, active, fname = None, fsize = 30, fcolor = None, action = None):
		"""Placing a button on the screen"""
		cur = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		#print(click)
		if x + width > cur[0] > x and y + height > cur[1] > y:
			pygame.draw.rect(self.screen, active, (x, y, width, height))
			if click[0] == 1 and action != None:
				if action == 'start':
					pass
					
		else:
			pygame.draw.rect(self.screen, inactive, (x, y, width, height))
		
		self.text_to_button(msg = text, color = fcolor, buttonx = x, buttony = y, buttonwidth = width, buttonheight = height, fname = fname, fsize = fsize)

	def text_to_button(self, msg, color, buttonx, buttony, buttonwidth, buttonheight, fname = None, fsize = 30):
		textSurf, textRect = self.text_objects(fname = fname, fsize = fsize, msg = msg, color = color)
		textRect.center = ((buttonx + (buttonwidth /2)),
			buttony + (buttonheight / 2))
		self.screen.blit(textSurf, textRect)
