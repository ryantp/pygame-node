#PYTHON3.5.1 (Anaconda3, 64-BIT);

# for general objects

##PART1 PYGAME.DRAW

import pygame


class DObj(object):

	def __init__(self, otype = None, points = [], dimensions = [], color = [], screen = None):
		self.otype = otype
		self.points = points
		self.dimensions = dimensions
		self.color = color
		self.screen = screen

	def _otype(self):
		if self.otype == 'swh':
			self.dSWH()
		elif self.otype == 'swv':
			self.dSWV()
		elif self.otype == 'swd':
			self.dSWD()
		elif self.otype == 'cw':
			self.dCWL()
		elif self.otype == 'ibld':
			self.dIBld()
		else:
			pass

	def dSWH(self):
		if self.screen:
			pygame.draw.rect(self.screen, self.color, (self.points[0], self.points[1], self.dimensions[0], self.dimensions[1]))

	def dSWV(self):
		if self.screen:
			pygame.draw.rect(self.screen, self.color, (self.points[0], self.points[1], self.dimensions[0], self.dimensions[1])

	def dSWD(self):
		if self.screen:
			pygame.draw.polygon(self.screen, self.color, self.points)

	def dCWL(self):
		if self.screen:
			pygame.draw.polygon(self.screen, self.color, self.points)

##PART2 SCREEN.BLIT