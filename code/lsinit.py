#PYTHON3.5.1 (Anaconda3, 64-BIT);

# lsinit -> for in-game use;

import sys
from win32api import GetSystemMetrics as gsm

import pygame

from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

import loadmng as L

if sys.platform == 'win32':
	pass # this program is for Windows OS only :/ (at this time)
else:
	print("Platform Error --  This program is for Windows OS")
	pygame.quit()
	quit()

clock = pygame.time.Clock()
fps = 20


class LSTool(std4.StdTool):
	'''localize the std4.StdTool, for simplicity's sake, so that the actual file won't be edited\
	 and therefore, possibly incompatable with other programs'''
	 # takes a screen object

	def button(self, text, x, y, width, height, inactive, active, fname = None, fsize = 30, fcolor = None, action = None):
		"""Placing a button on the screen"""
		cur = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		#print(click)
		if x + width > cur[0] > x and y + height > cur[1] > y:
			pygame.draw.rect(self.screen, active, (x, y, width, height))
			if click[0] == 1 and action != None:
				if action == 'start':
					return 1
				elif action == 'new':
					return 1
				elif action == 'cnt':
					return 1
				elif action == 'load':
					return 1
				elif action == 'quit':
					pygame.quit()
					quit()
				else:
					pass
					
		else:
			pygame.draw.rect(self.screen, inactive, (x, y, width, height))
		
		self.text_to_button(msg = text,
			color = fcolor,
			buttonx = x,
			buttony = y,
			buttonwidth = width,
			buttonheight = height,
			fname = fname,
			fsize = fsize)

def first_screencard(size = [], screen = None):
	# draw DEV16
	# pAr = pygame.PixelArray(screen)

	msg_tool = std4.StdTool(screen)

	startx = (size[0] / 2) - (210 / 2)
	starty = 150
	w = 210 + 40
	h = size[1] - starty * 2

	d_arch = ((startx, starty), (startx + 30, starty),
		(startx + 50, starty + 50), (startx + 60, starty + 100),
		(startx + 50, starty + 150), (startx + 30, starty + 200),
		(startx, starty + 200), (startx, starty + 195),
		(startx + 30, starty + 195), (startx + 50, starty + 145),
		(startx + 50, starty + 100), (startx + 50, starty + 55),
		(startx + 30, starty + 5), (startx, starty + 5))

	#ex = startx + 35
	ex = startx + 70
	letter_e = ((ex, starty), (ex, starty + 200),
		(ex + 50, starty + 200), (ex + 50, starty + 195),
		(ex + 5, starty + 195), (ex + 5, starty + 102),
		(ex + 50, starty + 102), (ex + 50, starty + 98),
		(ex + 5, starty + 98), (ex + 5, starty + 5),
		(ex + 50, starty + 5), (ex + 50, starty))

	vx = ex + 60
	letter_v = ((vx, starty), (vx + 23, starty + 200),
		(vx + 28, starty + 200), (vx + 50, starty),
		(vx + 45, starty), (vx + 25, starty + 195),
		(vx + 5, starty))

	onex = vx + 70
	number_1 = ((onex, starty), (onex, starty + 5),
		(onex - 8, starty + 20), (onex - 8, starty + 25),
		(onex, starty + 22), (onex, starty + 200),
		(onex + 5, starty + 200), (onex + 5, starty))

	twox = onex + 10
	number_6 = ((twox, starty), (twox, starty + 200),
		(twox + 30, starty + 200), (twox + 30, starty + 130),
		(twox + 5, starty + 130), (twox + 5, starty + 135), (twox + 25, starty + 135),
		(twox + 25, starty + 195), (twox + 5, starty + 195),
		(twox + 5, starty + 5), (twox + 30, starty + 5),
		(twox + 30, starty))

	i = 0
	ilim = 100

	lsi = True
	while lsi:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_SPACE:
					lsi = False
				elif event.key == pygame.K_RETURN:
					lsi = False
		
		pygame.draw.rect(screen, rgb.white, (startx - 20, starty - 20, w + 20, h + 20))
		pygame.draw.line(screen, rgb.red, (startx, starty), (startx, starty + 200), 5)
		pygame.draw.polygon(screen, rgb.red, d_arch)
		pygame.draw.polygon(screen, rgb.red, letter_e)
		pygame.draw.polygon(screen, rgb.red, letter_v)
		pygame.draw.polygon(screen, rgb.red, number_1)
		pygame.draw.polygon(screen, rgb.red, number_6)
		msg_tool.message_to_screen(msg = "Games",
					color = rgb.black,
					width = size[0],
					height = size[1],
					x_displace = 10,
					y_displace = 50,
					fname = 'Courier New',
					fsize = 90)

		if i >= ilim:
			lsi = False
		pygame.display.update()
		clock.tick(fps)
		i += 1

def startcard(size = [], root = None, screen = None):
	msg_tool = LSTool(screen)
	scard = pygame.image.load(root + '/resources/images/lsi/titlecard.png')
	screen.fill(rgb.black)
	carddim = (300,300)
	x = (size[0] / 2) - (carddim[0] / 2)
	y = (size[1] / 2) - (carddim[1] / 2)

	s = True
	while s:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		
		screen.blit(scard, (x, y))
		b = msg_tool.button(text = 'Start',
			x = (size[0] / 2) - 50,
			y = 600,
			width = 100,
			height = 80,
			inactive = rgb.black,
			active = rgb.dim_gray,
			fname = 'Courier',
			fsize = 30,
			fcolor = rgb.red,
			action = 'start') # returns True when clicked
		
		if b:
			s = False
		
		pygame.display.update()
		clock.tick(fps)

def main_menu(size = [], root = None, screen = None):
	msg_tool = LSTool(screen)
	screen.fill(rgb.black)
	m = True
	while m:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		
		n = msg_tool.button(text = 'New Game',
			x = size[0] - 200,
			y = 100,
			width = 150,
			height = 80,
			inactive = rgb.dodger_blue,
			active = rgb.blue,
			fname = 'Courier',
			fsize = 30,
			fcolor = rgb.black,
			action = 'new') # returns True when clicked
		c = msg_tool.button(text = 'Continue',
			x = size[0] - 200,
			y = 200,
			width = 150,
			height = 80,
			inactive = rgb.dark_green,
			active = rgb.green,
			fname = 'Courier',
			fsize = 30,
			fcolor = rgb.black,
			action = 'cnt') # returns True when clicked
		l = msg_tool.button(text = 'Load',
			x = size[0] - 200,
			y = 300,
			width = 150,
			height = 80,
			inactive = rgb.dark_turquoise,
			active = rgb.turquoise,
			fname = 'Courier',
			fsize = 30,
			fcolor = rgb.black,
			action = 'load') # returns True when clicked
		msg_tool.button(text = 'Quit',
			x = size[0] - 200,
			y = 400,
			width = 150,
			height = 80,
			inactive = rgb.orange_red,
			active = rgb.red,
			fname = 'Courier',
			fsize = 30,
			fcolor = rgb.black,
			action = 'quit') # returns True when clicked

		if n:
			return 'n' # breaks the loop

		if c:
			return 'c' # breaks the loop

		if l:
			return 'l' # breaks the loop

		pygame.display.update()
		clock.tick(fps)

def main(size = [], screen = None):
	pygame.init()
	#screen = pygame.display.set_mode(size)

	p = True
	while p:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		first_screencard(size, screen)
		startcard(size = size, root = L.rootdir(), screen = screen)
		res = main_menu(size = size, root = L.rootdir(), screen = screen)

		return res # will break the main loop
		# handling a 'c' over 'l' will be in main.py

		pygame.display.update()
		clock.tick(fps)
		p = False

if __name__ == '__main__':
	pass