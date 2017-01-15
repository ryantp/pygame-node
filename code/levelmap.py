#PYTHON3.5.1 (Anaconda3, 64-BIT);

# a map class for easily retrieving info regarding maps in use

import pygame

class Map(object):
	"""docstring for Map"""

	def __init__(self, lnum = None, lname = None, slnum = None, slname = None, dimensions = [], blit_points = [], rootdir = None, screen = None):
		self.lnum = lnum # level number
		self.lname = lname # level name (for in-game use)
		self.slnum = slnum # sublevel number
		self.slname = slname # sublevel name
		self.dimensions = dimensions
		self.blit_points = self.init_blit_points = blit_points # list or tuple
		self.rootdir = rootdir
		self.screen = screen
		self.image = self.load_map()
		

	def __repr__(self):
		return "Level Info: LNUM: %(lnum)d LNAME: %(lname)s" % {
			'lnum': self.lnum,
			'lname': self.lname
		}

	def load_map(self):
		map_dict = {
			-1: {1: self.rootdir + '/resources/images/maps/landscape_img/test_map.png',},
			0: {1: self.rootdir + '/resources/images/maps/l0/1.png'},
			1: {1: None, 2: None, 3: None},
			2: {1: None, 2: None, 3: None},
			3: {1: None, 2: None, 3: None},
			4: {1: None, 2: None, 3: None}
		}

		return pygame.image.load(map_dict[self.lnum][self.slnum])

	def get_dimensions(self):
		return self.dimensions

	def adjust_blit(self, x = 0, y = 0):
		self.blit_points[0] = self.blit_points[0] + x
		self.blit_points[1] = self.blit_points[1] + y

	def blit(self):
		if self.screen:
			self.screen.blit(self.image, self.blit_points)
		else:
			pass