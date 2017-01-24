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

	def __repr__(self):
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

	def __str__(self):
		return "Player %(n)s x[%(x)d] y[%(y)d]" % {
			'n': self.name,
			'x': self.pos[0],
			'y': self.pos[1]
		}

	def __repr__(self):
		return "Player %(n)s x[%(x)d] y[%(y)d]" % {
			'n': self.name,
			'x': self.pos[0],
			'y': self.pos[1]
		}

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

	def __str__(self):
		return "%(C)s %(n)s x[%(x)d] y[%(y)d]" % {
			'C': str(NPC).split("'")[1],
			'n': self.name,
			'x': self.pos[0],
			'y': self.pos[1]
		}

	def __repr__(self):
		return "%(C)s %(n)s x[%(x)d] y[%(y)d]" % {
			'C': str(NPC).split("'")[1],
			'n': self.name,
			'x': self.pos[0],
			'y': self.pos[1]
		}

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
			s = "Enemy(%(C)s) (UID: %(u)s) -- x[%(x)d] y[%(y)d]" % {
					'C': str(Enemy).split("'")[1],
					'u': self.uid,
					'x': self.pos[0],
					'y': self.pos[1]
				}
		return s

	def __repr__(self):
		return "Enemy(%(C)s) (UID: %(u)s) -- x[%(x)d] y[%(y)d]" % {
			'C': str(Enemy).split("'")[1],
			'u': self.uid,
			'x': self.pos[0],
			'y': self.pos[1]
		}

	def chase(self, target = None, speed = 0):
		# chase specified target; target must be a Char, Player, NPC or Enemy object
		# speed - speed of this unit (ie. unit can run after target)
		pass

	def move(self):
		pass


class HealthBar(object):
	'''standard pygameF health bar'''
	def __init__(self, health = [], pos = [], screen = None):
		self.curHealth = health[0] # current health
		self.ttlHealth = health[1] # total health
		self.pos = pos # [0]x and [1]y
		self.screen = screen # pygame screen object

		self.hDim = [16, 16] # 16 X 16 block
		self.hCol = [250, 0, 0] # rgb value for red
		self.blitBuff = self.hDim[0] # blit buffer

	def __str__(self):
		return "HealthBar %(C)s c[%(c)d]/t[%(t)d]" % {
			'C': str(HealthBar).split("'")[1],
			'c': self.curHealth,
			't': self.ttlHealth
		}

	def __repr__(self):
		return "HealthBar %(C)s c[%(c)d]/t[%(t)d]" % {
			'C': str(HealthBar).split("'")[1],
			'c': self.curHealth,
			't': self.ttlHealth
		}

	def get_pos(self):
		return self.pos

	def set_pos(self, pos = []):
		self.pos = pos

	def get_hDim(self):
		return self.hDim

	def set_hDim(self, hDim = []):
		self.hDim = hDim

	def get_hCol(self):
		return self.hCol

	def set_hCol(self, hCol = []):
		self.hCol = hCol

	def blit(self):
		x = self.pos[0] # initial x blit point
		for i in range(self.health[0]):
			pygame.draw.rect(self.screen, self.hCol, [x, self.pos[1], self.hDim[0], self.hDim[1]])
			x += self.blitBuff

