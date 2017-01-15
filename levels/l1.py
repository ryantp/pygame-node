#PYTHON3.5.1 (Anaconda3, 64-BIT);

import pygame

class Level1(object):
	# CLASS VAR
	# level_info
	lnum = 1
	lname = 'Western Block'
	slinfo = {
		1: '#<NAMEVAR_SL1',
		2: '#<NAMEVAR_SL2',
		3: '#<NAMEVAR_SL3'
	}
	slnums = slinfo.keys()
	ldim = [] # to-be-determined
	lbp = [] # to-be-determined

	# player info
	pch = ptc = 3 # this is standard, although a player can obtain more (though probably not in the tutorial level)
	pcs = pts = 100 # STD, ++ from level0, which should have about 80 or so; or can be 100 and remain so
	pip = None # this info NEEDS to be passed when the class is created
	pdim = None # this standard, and can be accessed when the player object is created

	# entity
	stdsize = {
		'INCO': [40, 100]
	}

	def __init__(self, level_info = [], player_info = [], entity_info = [], required_obj = [], optional_obj = [], rootdir = None, screen = None):
		'''PROVIDING SAVED DATA:
			all saved data must be passed when calling this class, otherwise, it will initiate the level with base stats
				which are held as class variables'''

		# META VARS
		self.current_sublevel = player_info[0] # should be the first piece of info passed into player_info

		# the main three [level, player, entity] does not require pre-created units, but rather the info required for loaded data
		# -- required_obj contains the actual classes
		# level info
		self.lnum = level_info[0], 
		self.lname = level_info[1],
		self.slnum = level_info[2], 
		self.slname = level_info[3],
		self.ldim = level_info[4]
		self.lbp = level[5]
		
		# player info
		self.pch = player_info[1]
		self.pth = player_info[2]
		self.pcs = player_info[3]
		self.pts = player_info[4]
		self.pip = player_info[5] # this is a list
		self.pdi = player_info[6]
		self.pbp = player_info[7]

		# entity info -- NESTED LISTS
		self.entity_info = self.entity_info # the actual unpacking and handling will go through the monster_maker method

		# required classes -- SPECIFIC FORMAT -- will be used in their respective methods
		self.player = required_obj[0]
		self.lmap = required_obj[1]
		self.entity = required_obj[2]
		self.menu = required_obj[3]
		self.save = required_obj[4]

		### optional objects, including DEVTOOL and DGNTOOL -- [development tool] and [diagnostic tool]
		### DEVTOOL is used for level developement, DGNTOOL is used for recording level logs /
		### all optional_obj will be passed during development, but initialization shall be commented out, until needed
		#self.devt = optional_obj[0]
		#self.dgnt = optional_obj[1]

		# in-game variables
		self.playing = True # the main game boolean
		self.is_shifted = False # for sprinting, distracting, etc.
		self.x_ch = self.y_ch = self.x_speed = self.y_speed = self.STATIC = 0
		self.MOVE = 5
		self.SPEED = 10

		# other required variables
		self.rootdir = rootdir # the root dir of LS's main file
		self.screen = screen # the master screen obj, that gets passed around to everything :P

		# STD defininitions
		self.SIZE = self.width, self.height = 1000, 700
		self.VER = '1.3A3'

	def __str__(self):
		return "%(lnum)d:%(slnum)d | %(lname)s - %(slname)s" % {
			'lnum': self.lnum,
			'slnum': self.slnum,
			'lname': self.lname,
			'slname': self.slname
		}

	def pygame_init(self):
		pygame.init()

	def set_display(self):
		pygame.display.set_mode(self.SIZE)
		pygame.display.set_caption('Lost Soul v%s' % self.VER)

	def create_char(self):
		return self.player.Char(hearts = [self.pch, self.pth],
			stamina = [self.pcs, self.pts],
			paths = self.pip,
			blit_points = self.pbp,
			screen = self.screen)

	def create_map(self):
		return self.lmap.Map(lnum = self.lnum,
			lname = self.lname,
			slnum = self.slnum,
			slname = slname,
			dimensions = self.ldim,
			blit_points = self.lbp,
			screen = self.screen)

	def create_entities(self):
		entities = {}
		for ind in self.entity_info:
			entities[ind[0]] = self.entity(uid = ind[0],
				stdsize = Level1.stdsize[ind[0]],
				path = ind[1],
				ai_model = ind[2],
				name = ind[3],
				blit_points = ind[4],
				screen = self.screen)

		return entities

	def sublevel1(self):
		# INFO -- one of the main methods; there is one main method for each sublevel
		# PYGAME REQUIREMENTS
		self.pygame_init()
		self.set_display()

		# setup map, char and entities
		lmap = self.create_map()
		player = self.create_char()
		entities = self.create_entities() #dict
		clock = pygame.time.Clock()
		fps = 30

		while self.playing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						self.y_ch = self.MOVE + self.y_speed
						if self.is_shifted:
							self.y_speed = self.SPEED
					elif event.key == pygame.K_a:
						self.x_ch = self.MOVE + self.x_speed
						if self.is_shifted:
							self.x_speed = self.SPEED
					elif event.key == pygame.K_s:
						self.y_ch = -self.MOVE - self.y_speed
						if self.is_shifted:
							self.y_speed = self.SPEED
					elif event.key == pygame.K_d:
						self.x_ch = -self.MOVE - self.x_speed
						if self.is_shifted:
							self.x_speed = self.SPEED
					elif event.key == pygame.K_g:
						# FOR DEVELOPMENT
						print("map x: %d\nmap y: %d" % (lmap.blit_points[0], lmap.blit_points[1]))
						pmng.append_points(['map', lmap.blit_points[0], lmap.blit_points[1]])
						pmng.append_points(['player', player.player_blit_points[0], player.player_blit_points[1]])
					elif event.key == pygame.K_q:
						# FOR DEVELOPMENT
						print('LOGGING %d POINT PAIRS' % pmng.lenp())
						pmng.write_to_file()
					elif event.key == pygame.K_p:
						menu.pause(player = player, lmap = lmap, enemy_obj = entities, clock = clock, screensize = [width, height], screen = screen)
					elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
						self.is_shifted = True
					elif event.key == pygame.K_SPACE:
						# TO-BE-CHANGED later
						player.adjust_c_heart(-1)
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						self.y_ch = self.STATIC
					elif event.key == pygame.K_a:
						self.x_ch = self.STATIC
					elif event.key == pygame.K_s:
						self.y_ch = self.STATIC
					elif event.key == pygame.K_d:
						self.x_ch = self.STATIC
					elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
						self.is_shifted = False
						self.x_speed = self.STATIC
						self.y_speed = self.STATIC
					elif event.key == pygame.K_SPACE:
						pass

			self.screen.fill(rgb.black)
			lmap.adjust_blit(x_ch, y_ch)
			lmap.blit()
			elist = entities.keys()
			for entity in elist:
				entities[entity].adjust_blit(x_ch, y_ch)
				entities[entity].ai_path()
				entities[entity].blit()
			player.blit()
			pygame.display.update()
			clock.tick(fps)
