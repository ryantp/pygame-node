#Python3.5

'''
This is a simple collection of sprite classes.

'''

import pygame

from pygamepredef.sentdex import std4 as s

class Char(object):
	'''standard class for generic sprites; takes a pygame screen object'''
	def __init__(self, name, pos = [], screen = None):
		self.name = name
		self.pos = pos
		self.screen = screen

	def __str__(self):
		return "%(n)s x[%(x)d]y[%(y)d]" % {'n': self.name, 'x': self.pos[0], 'y': self.pos[1]}

	def blit(self, img = None):
		self.screen.blit(img, self.pos)


class Player(Char):
	'''standard class for player sprite'''
	def __init__(self, name, health = [], pos = [], screen = None):
		self.name = name
		self.health = health # [0] = current health; [1] = total health
		self.pos = pos # [0] = x position; [1] = y position
		self.screen = screen

	def injure(self, damage = 0):
		self.health[0] = self.health[0] - damage

	def heal(self, points = 0):
		self.health[0] = self.health[0] + points
		if(self.health[0] > self.health[1]):
			self.health[0] = self.health[1]

	def move(self, x = 0, y = 0):
		# values must be positive or negative as appropriate
		self.pos[0] = self.pos + x
		self.pos[1] = self.pos + y


class NPC(Char):
	'''standard class for NPC's'''
	def __init__(self, name, pos = [], screen = None):
		self.name = name
		self.pos = pos
		self.screen = screen
		self.textTool = s.StdTool(screen)

	def say(self, *args):
		self.textTool(msg, color, width, height, x_displace = 0, y_displace = 0, fname = None, fsize = 30)

	def mvPtrn(self, p = None, mv = []):
		# movement pattern
		# p = pattern type
		# mv = [0]displacement, [1]stride
		pass