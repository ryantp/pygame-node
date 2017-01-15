#PYTHON3.5.1 (Anaconda3, 64-BIT);

import pygame


class Char(object):

	def __init__(self, hearts = [], stamina = [], img_objs = [], blit_points = [], screen = None):
		self.c_hearts = hearts[0]
		self.t_hearts = hearts[1]
		self.c_stamina = stamina[0]
		self.t_stamina = stamina[1]
		self.screen = screen
		self.player = img_objs[0]
		self.heart = img_objs[1]
		self.sp = img_objs[2]
		self.player_blit_points = self.init_blit_points = blit_points[0]
		self.heart_blit_points = blit_points[1]
		self.stamina_blit_points = blit_points[2]

		#std definitions
		self.player_stdsize = [40, 100]
		self.heart_stdsize = [16, 16]
		self.stamina_stdsize = [1, 16]

	def __str__(self):
		return "Character Class Object -- Player"

	def get_stdsize(self):
		return self.player_stdsize

	def restore_c_heart(self):
		self.c_hearts = self.t_hearts

	def restore_c_stamina(self):
		self.c_stamina = self.t_stamina

	def adjust_c_heart(self, number = 0):
		self.c_hearts += number # number should be positive or negative as needed

	def adjust_c_stamina(self, number = 0):
		self.c_stamina += number # number should be positive or negative as needed

	def blit_heart(self):
		for i in range(self.c_hearts):
			realign_x = self.heart_stdsize[0] * i

			self.screen.blit(self.heart, (self.heart_blit_points[0] + realign_x, self.heart_blit_points[1]))

	def blit_sp(self):
		y_displace = self.heart_stdsize[1] + 2 # the displace is the size of the hearts plus a 2 pixel buffer
		for i in range(self.c_stamina):
			realign = self.stamina_stdsize[0] * i

			self.screen.blit(self.sp, (self.stamina_blit_points[0] + realign, self.stamina_blit_points[1] + y_displace))

	def blit(self):
		if self.screen:
			self.screen.blit(self.player, self.player_blit_points)
			self.blit_heart()
			self.blit_sp()