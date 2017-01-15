#PYTHON3.5.1 (Anaconda3, 64-BIT);

import pygame


class Unit(object):

	def __init__(self, uid = None, stdsize = [], path = None, ai_model = [], name = [], blit_points = [], screen = None):
		self.uid = uid # unique id
		self.stdsize = stdsize
		self.screen = screen
		self.blit_points = self.init_blit_points = blit_points
		self.img_path = path
		self.movement_path = ai_model[0]
		self.is_agro = ai_model[1]
		self.is_boss = ai_model[2]
		self.ability = ai_model[3]
		self.type_name = name[0]
		self.personal_name = name[1] # not going to be used much

		#std definitions
		self.unit = self.create_sprite_obj()
		self.move = 1
		self.MAXIMUM_DISPLACE = 200
		self.x = self.y = 0

	def __str__(self):
		return "Unit Class Object -- %s" % self.img_path

	def create_sprite_obj(self):
		return pygame.image.load(self.img_path)

	def chase(self):
		pass

	def ai_path(self):
		#PATHS = ['l_r', 'u_d', 'cir', 'squ', 'dia', 'grd']
		START_POINTS = self.blit_points
		if self.movement_path == 'l_r':
			self.blit_points[0] -= self.move
			self.x -= self.move
			print('MD: %d | X: %d' % (self.MAXIMUM_DISPLACE, self.x))
			if self.x >= self.MAXIMUM_DISPLACE or self.x <= (self.MAXIMUM_DISPLACE * -1):
				#print('MD: %d | X: %d' % (MAXIMUM_DISPLACE, x))
				self.move = self.move * -1
		else:
			pass

	def adjust_blit(self, x = 0, y = 0):
		self.blit_points[0] = self.blit_points[0] + x
		self.blit_points[1] = self.blit_points[1] + y

	def blit(self):
		if self.screen:
			self.screen.blit(self.unit, self.blit_points)
		else:
			pass