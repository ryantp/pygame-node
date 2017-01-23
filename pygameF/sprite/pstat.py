#PYTHON3.5.1 (Anaconda3, 64-BIT);

# blit hearts and SP bar

import pygame


class Heart(object):
	"""docstring for Heart"""
	
	def __init__(self, blit_points = [], cquantity = 0, tquantity = 0, is_strong = False, screen = None):
		self.blit_points = blit_points
		self.cquantity = cquantity
		self.tquantity = tquantity
		self.is_strong = is_strong
		self.screen = screen
		# all heart images
		self.heart = self.get_img_obj()
		'''
		self.half_heart = self.get_img_obj('hh', False)
		self.strong_half_heart = self.get_img_obj('hh', True)
		self.strong_heart = self.get_img_obj('wh', True)
		self.whole_heart = self.get_img_obj('wh', False)'''


	def get_img_obj(self):
		path = 'C:/Users/alpha/Desktop/DEV16/ls/src/resources/images/stats/heart.png'

		return pygame.image.load(path)

	def get_stdsize(self):
		return (16, 16)

	def get_cquantity(self):
		return self.cquantity

	def adjust_cquantity(self, number = 0):
		self.cquantity = self.cquantity + number # number should be supplied as positive or negative as necessary

	def blit(self):
		realign_x = realign_y = 0
		j = 1
		for i in range(self.cquantity):
			realign_x = self.get_stdsize()[0] * i

			self.screen.blit(self.heart, (self.blit_points[0] + realign_x, self.blit_points[1] + realign_y))				


class Stamina(object):

	def __init__(self, blit_points = [], y_displace = 0, cquantity = 0.0, tquantity = 0, screen = None):
		self.blit_points = blit_points
		self.y_displace = y_displace + 2 # 2 pixel buffer
		self.cquantity = cquantity
		self.tquantity = tquantity
		self.screen = screen
		self.image = self.get_img_obj()
	
	def get_img_obj(self):
		path = "C:/Users/alpha/Desktop/DEV16/ls/src/resources/images/stats/sp_pip.png"

		return pygame.image.load(path)

	def get_stdsize(self):
		return (1, 16)

	def get_cquantity(self):
		return self.cquantity

	def adjust_cquantity(self, number = 0):
		self.cquantity = self.cquantity + number # if supposed to decrease, then number must be passed as negative

	def blit(self):
		x, y = self.blit_points
		for i in range(self.cquantity):
			realign = self.get_stdsize()[0] * i
			self.screen.blit(self.image, (x + realign, y + self.y_displace))