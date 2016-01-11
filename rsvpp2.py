# -*- coding: utf-8 -*-
# 
# ENVIRONMENT: 
# 	win10_x64, 
# 	anaconda_2.3.0_64bit, 
#	python_2.7.10. 
#

import pygame as pig
from pygame.locals import *
import numpy as nip
from win32api import GetSystemMetrics	# under windows environment, use cmd prompt: pip install pypiwin32
import random, time

###################################################
###		VISION CLASS			###
###################################################

class vision:
	# preload parameters for vision 
	def __init__(	self, 
			dottxt,
			fullscreen = True, 
			color = (255, 255, 255), 
			bgColor = (128, 128, 128), 
			size = 20, 
			distance = 60, 
			diag = 23, 
			angel = 1.5	):
		if type(dottxt) is str:
			if dottxt[-4:len(dottxt)] == '.txt':
				with open(dottxt) as a: 
					mater = unicode(a.read().decode('utf-8'))	# import the materials
			else: 
				ctypes.windll.user32.MessageBoxA(0, 'vision(): file type should be of .txt', 'Wrong', 0)
		else:
			ctypes.windll.user32.MessageBoxA(0, 'vision(): file name should be of string type (str)', 'Wrong', 0)
		self.mater = mater
		self.color = color
		self.bgColor = bgColor
		pig.init()
		self.pig = pig
		self.pig.mouse.set_visible(False)
		self.winWidth = GetSystemMetrics(0); self.winHeight = GetSystemMetrics(1)
		if fullscreen == True: 
			self.scrSize = (self.winWidth, self.winHeight)
			self.win = pig.display.set_mode(self.scrSize, FULLSCREEN | DOUBLEBUF)
		else: 
			self.scrSize = (800, 600)
			self.win = pig.display.set_mode(self.scrSize, HWSURFACE | DOUBLEBUF) 
		# set experimental materials font size
		# pixelSize/(pixels in diagonal) = realLength/(real length in diagonal)
		self.materSize = int((self.winWidth**2 + self.winHeight**2) **0.5/(diag*2.54 / (distance * nip.tan(angel/4*nip.pi/180) * 2))) 
	        self.font = pig.font.SysFont('SimHei', self.materSize)
		# init background screen
		self.clear()
		return None

	# renew the screen to a pure grey color
	def clear(self): 
		self.win.fill(self.bgColor)
		self.pig.display.flip()
		return None

	# METHOD:
	# 	PRESENT WHOLE SENTENCE: in original word order or randomized word order, depends on argument random
	# READ ME:
	# 	takes 1 argument: random
	# 	argument random will dicide the word order that presents
	def p(self, random = False): 	# REMINDER: p for present
		if random = False:
			localMater = self.mater
		else: 
			localMater = ''.join(random.sample(self.mater, len(self.mater)))
		centerText = self.font.render(localMater, True, self.color)
		self.win.blit(centerText, (self.winWidth / 2 - centerText.get_width() / 2, self.winHeight / 2 - centerText.get_height() / 2))
		self.pig.display.flip()
		return [localMater]

	# METHOD:
	# 	R_APID S_INGLE V_ISUAL P_RESENTATION
	# READ ME:
	# 	takes 3 arguments: trigger and timeout, and random
	# 	examines the event it eats. if no trigger, go on display current screen, until time up to timeout that was set
	# 	or go skip to next screen
	# 	argument random will dicide the word order that presents
	# NOTICE: if don't want timeout, set it to 0
	# TODO: modify trigger to cooperate with AUDIO CLASS
	def rsvp(self, trigger = False, timeout = 3000, random = False): # for tests' convenience, set default trigger to False, it is factually a function
		# define the material to be used in rsvp: randomized or not
		if random == True: 
			localMater = ''.join(random.sample(self.mater, len(self.mater))) 
		else: 
			localMater = self.mater
		if timeout == 0:	# time == 0, means no time limit
			for i in self.mater:	# in a certain word case
				while !trigger:	# no trigger, no skipping to next word
					# TODO: fix this bug: text has zero width
					# 	& rewrite clause inside try'n'except block
					try:
						target = self.font.render(i, True, self.color)
						self.win.blit(target, (self.winWidth / 2 - target.get_width() / 2, self.winHeight / 2 - target.get_height() / 2))
						self.pig.display.flip()
						self.pig.time.delay(timeout)
						self.clear()
					except:
						pass
		else: 	# time != 0, means there is a time limit
			for i in self.mater:	# in a certain word case
				TimeDuration = 0	# predefine TimeDuration
				startTime = time.time()	# start counting time
				while !(trigger or TimeDuration > timeout): 	# if neither trigger nor timeout, then no skipping to next word
					try:
						target = self.font.render(i, True, self.color)
						self.win.blit(target, (self.winWidth / 2 - target.get_width() / 2, self.winHeight / 2 - target.get_height() / 2))
						self.pig.display.flip()
						self.pig.time.delay(timeout)
						self.clear()
					except:
						pass
					endTime = time.time()	# stop counting time
					TimeDuration = startTime - endTime	# calculate TimeDuration
		return [TimeDuration, trigger, timeout, random, localMaterial]

###################################################		
###		AUDIO CLASS			###
###################################################

#class audio():

#	def vrecord(self): 	# REMINDER: v for voice
#		return

#	def vtrigit(self): 	# REMINDER: v for voice 
#		return 

###################################################
###		RESPONSE CLASS			###
###################################################

#class response():

#	def mconfirm(self):	# REMINDER: m for manual
#		return

###################################################
###		RECORD CLASS			###
###################################################

#class measure(): 

#	def timing(self):
#		return

###################################################		
###		POPUP MESSAGE 			###
###################################################


#	-*- author: LI Bing; date: Jan 2016 -*-
