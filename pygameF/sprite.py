#Python3.5

'''
This is a simple collection of sprite classes.
'''

import pygame

from pygamepredef.sentdex import std4 as s

class Char(object):
	'''standard class for generic sprites; takes a pygame screen object'''
	def __init__(self, name, pos = [], screen = None):
		self.name = name # name of character
		self.pos = pos # pos (aka bp)
		self.screen = screen # pygame screen object

	def __str__(self):
		return "%(n)s x[%(x)d] y[%(y)d]" % {'n': self.name, 'x': self.pos[0], 'y': self.pos[1]}

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
		# player is injured
		self.health[0] = self.health[0] - damage

	def heal(self, points = 0):
		# player is healed
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

	def mvPtrn(self, *args):
		# virtual function -- must be overwritten to work
		pass


class Enemy(Char):
	'''standard class for enemy units'''
	def __init__(self, uid = 0, nid = [], health = [], dimxy = [], pos = [], screen = None):
		self.uid = uid # unique id
		self.etype = nid[0] # enemy type (ie. goblin, dragon, etc).
		self.name = nid[1] # name of enemy unit (can be `None` if not applicable)
		self.health = health # [0]current health and [1]total health
		self.dimxy = dimxy # dimensions -- [0]x and [1]y
		self.pos = pos # position -- [0]x and [1]y
		self.screen = screen # pygame screen object

	def __str__(self):
		# return string for unit
		if(self.etype):
			if(self.name):
				s = "%(t)s %(n)s (UID: %(u)s) -- x[%(x)d] y[%(y)d]" % {
					't': self.etype,
					'n': self.name,
					'u': self.uid,
					'x': self.pos[0],
					'y': self.pos[1]
				}
			else:
				s = "%(t)s (UID: %(u)s) -- x[%(x)d] y[%(y)d]" % {
					't': self.etype,
					'u': self.uid,
					'x': self.pos[0],
					'y': self.pos[1]
				}
		else:
			s = "Enemy(%(e)s) (UID: %(u)s) -- x[%(x)d] y[%(y)d]" % {
					'e': Enemy,
					'u': self.uid,
					'x': self.pos[0],
					'y': self.pos[1]
				}
		return s

	def chase(self, target = None, speed = 0):
		# chase specified target; target must be a Char, Player, NPC or Enemy object
		# speed - speed of this unit (ie. unit can run after target)
		pass

	def move(self):
		pass

