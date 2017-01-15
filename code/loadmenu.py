#PYTHON3.5.1 (Anaconda3, 64-BIT);

import pygame

from pygamepredef.color import pygame_rgb as rgb
from pygamepredef.sentdex import std4

from backend import dbsave as dbs
import loadmng

ROOT = loadmng.rootdir()

clock = pygame.time.Clock()
fps = 30

class LSTool(std4.StdTool):

	def button(self, text, x, y, width, height, inactive, active, fname = None, fsize = 30, fcolor = None, action = None, opt = None):
		"""Placing a button on the screen"""
		cur = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		#print(click)
		if x + width > cur[0] > x and y + height > cur[1] > y:
			pygame.draw.rect(self.screen, active, (x, y, width, height))
			if click[0] == 1 and action != None:
				if action == 'continue_last':
					try:
						return opt, False
					except Exception:
						pass
				else:
					try:
						return action, False
					except TypeError as exc:
						print("LSTool Type Error Except: Tried to return None")
						print(str(exc))
					
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


def load_menu(screen = None):
	# returns all relavent info; for continuing, dbsave.SaveMaster.load_in_order() is accessed directly
	# SIZE[1] == 700; if each info-slot is 100 tall, then 7 slots can be on screen ##NOTE: now 50px tall / 14 slots;
	#
	# AS-OF 10.15.2016 -- WORKING! :) (the page doesn't change after clicking the button, because the 
	# 	function in main's main loop ``level = loadmng.queue_level()`` isn't set up yet)
	# there still may be error's being thrown (in the second nested try-except block), but I don't know the cause; the
	# 	error would be ``NoneType: is not iterable`` -> I don't know what's becoming / is None that's trying to be iterated over
	#
	# also, the scroll function is working perfectly ^_^

	RESULT = None
	
	btntool = LSTool(screen)
	
	buttons = {} # buttons dict
	
	d = dbs.SaveMaster(ROOT)
	x = y = 0 # y will increase by the button's height * n
	w = 600 # or so
	h = 48 # works good for the given font-size
	pxbuff = 2

	sid, ds, lname, lnum, slname, slnum = d.read_sid()

	for i, s in enumerate(sid):
		s = '%(sid)d  |  %(lnum)d.%(slnum)d %(lname)s -- %(slname)s >>> %(ds)s' % {'sid': sid[i],
			'lnum': lnum[i],
			'slnum': slnum[i],
			'lname': lname[i],
			'slname': slname[i],
			'ds': ds[i]
			}
		buttons[i + 1] = [s,
			[x, y],
			w,
			h,
			'Tahoma',
			20,
			rgb.black,
			i + 1] # these buttons will return their corresponding SID, and also a boolean (False) for the while loop var

	#print("Printing buttons")
	#print(buttons)
	MINIMUM = 1 # the minimum value that imin can reach
	MAXIMUM = i + 1 # the maximum value imax can reach
	PERSCREEN = 14 # the maximum number of buttons which can fit on the screen (for the current size of the screen -> (1000, 700))
	imin = 1 # these (imin, imax) will controll which buttons are blitted to the screen
	if MAXIMUM <= PERSCREEN:
		imax = MAXIMUM # if there are less save entries than the PERSCREEN max, 
		#	then imax will be equal to the actual number of entries
	else:
		imax = PERSCREEN

	#DEBUG -- MASS PRINT
	'''print('MINIMUM: %(min)d\
		\nMAXIMUM: %(max)d\
		\nPERSCREEN: %(psc)d\
		\nimin: %(imn)d\
		\nimax: %(imx)d' % {
			'min': MINIMUM,
			'max': MAXIMUM,
			'psc': PERSCREEN,
			'imn': imin,
			'imx': imax
		})'''

	'''NOTES FOR: imin & imax
		pygame.MOUSEBUTTON -> button[3] (middle wheel) will alter imin and imax;
		the MAXIMUM var will be the the max value imax can reach, and MINIMUM will be the min value that imin can reach
	'''

	SCROLLUP = 4 # will corespond to - 1
	SCROLLDOWN = 5 # will corespond to + 1

	cur = pygame.mouse.get_pos() # used to determine if the mouse is within the button column

	l = True
	while l:
		for event in pygame.event.get():
			cur = pygame.mouse.get_pos()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_g:
					print(cur) #DEV
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == SCROLLUP:
					#print(cur)
					#print(imin)
					if imin == MINIMUM:
						pass
					else:
						imin -= 1
						imax -= 1
				elif event.button == SCROLLDOWN:
					#print(cur)
					#print(imax)
					if imax == MAXIMUM:
						pass
					else:
						imin += 1
						imax += 1

		screen.fill(rgb.linen)
		try:
			i = 0 # this variable will help with the button's y position
			# will add button.height * i to the button's y blit-point, effectively (potentially) filling the whole screen
			for n in range(imin, imax + 1):
				#print("DEBUG: printing n")
				#print(n)
				try:
					# with this extra try loop, the n variable increments (and the buttons all blit), 
					# but something is still going null
					RESULT, l = btntool.button(text = buttons[n][0],
						x = buttons[n][1][0],
						y = buttons[n][1][1] + ((buttons[n][3] + pxbuff) * i),
						width = buttons[n][2],
						height = buttons[n][3],
						inactive = rgb.blue_linen,
						active = rgb.light_sky_blue,
						fname = buttons[n][4],
						fsize = buttons[n][5],
						fcolor = buttons[n][6],
						action = buttons[n][7])
				except Exception as exc:
					#print("Exception: RESULT, l = btntool.button-%(number)d" % {'number': n})
					#print(str(exc))
					pass
				i += 1
		except Exception as exc:
			#print('Exception: for n in range(imin, imax) <load_menu>')
			#print(str(exc))
			# None type is not iterable
			pass

		btntool.message_to_screen(msg = "Load A Save Instance",
			color = rgb.black,
			width = 1000,
			height = 700,
			x_displace = 300,
			y_displace = -300,
			fname = 'Tahoma',
			fsize = 35)
		btntool.message_to_screen(msg = "Use mouse-wheel to scroll through entries",
			color = rgb.black,
			width = 1000,
			height = 700,
			x_displace = 300,
			y_displace = -250,
			fname = 'Tahoma',
			fsize = 15)
		btntool.message_to_screen(msg = "Load last entry: ",
			color = rgb.black,
			width = 1000,
			height = 700,
			x_displace = 250,
			y_displace = -215,
			fname = 'Tahoma',
			fsize = 15)
		try:
			RESULT, l = btntool.button(text = "continue",
				x = 800,
				y = 120,
				width = 130,
				height = 35,
				inactive = rgb.dark_green,
				active = rgb.green,
				fname = 'Tahoma',
				fsize = 30,
				fcolor = rgb.black,
				action = 'continue_last',
				opt = MAXIMUM)
		except Exception:
			pass
		pygame.display.update()
		clock.tick(fps)

	if RESULT:
		return RESULT # there should always be a result if it reaches this point

