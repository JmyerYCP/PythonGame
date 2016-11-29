import time
import pygame
import sys
import random
from math import *
from time import sleep
from pygame.locals import *
bif = "bg2.jpg"

pygame.init()

display_width=1080
display_height=720
screen=pygame.display.set_mode((display_width,display_height),0,32)
background=pygame.image.load(bif).convert()
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
clock = pygame.time.Clock()

def distanceFormula(x1,y1,x2,y2):
	distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	return distance

def message_to_screen(msg,color, size=25,x_offset=0,y_offset=0):
	font = pygame.font.SysFont(None, size)
	screen_text = font.render(msg,True,color)
	textRect= screen_text.get_rect()
	textRect.center = (display_width/2+x_offset,display_height/2+y_offset)
	screen.blit(screen_text, textRect)

def randomCircle():
	randomX = random.randrange(25,display_width-25)
	randomY = random.randrange(100,display_height-25)
	circletype = random.randrange(1,12)
	if circletype <4:
		colour = red
	elif circletype > 9:
		colour = green
	else:
		colour = white
	pygame.draw.circle(screen, colour, (randomX,randomY),25)
	return randomX,randomY,colour


def gameStart():
	gameBegin = False
	while not gameBegin:
		pauseTime = clock.tick() / 1000
		screen.blit(background, (0, 0))
		message_to_screen("Welcome", red, 200)
		message_to_screen("Press any key to begin", red, 25, 0, 100)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameBegin = True
			if event.type == pygame.KEYDOWN:
				gameBegin = True
				gameLoop()
				pauseTime = (clock.tick() / 1000) - pauseTime
			if event.type == pygame.MOUSEBUTTONDOWN:
				gameBegin = True
				gameLoop()
				pauseTime = (clock.tick() / 1000) - pauseTime
	pygame.quit()
	quit()





def gameLoop(self=0):
	gameExit = False
	gamePause = False
	gameEnd = False
	pauseTime = 0
	timer = 0
	playtime = 0
	score = 0
	randomX =0
	randomY = 0
	mouseX = -100
	mouseY = -100
	multiplier = 1
	colour = 0
	if score == 0:
		highscore = 0
	screen.blit(background, (0, 0))
	while not gameExit:
		pygame.Surface.fill(screen,black,[0,0,display_width,75])
		while gameEnd == True:
			pauseTime = clock.tick() / 1000
			screen.blit(background, (0, 0))
			if score > highscore:
				highscore = score
			message_to_screen("Highscore: "+str(int(highscore)),red,75,0,-150)
			message_to_screen("GAME OVER", red, 200)
			message_to_screen("Press any key to try again or Esc to quit",red,25,0,100)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameExit = True
						gameEnd = False
					else:
						gameEnd = False
						pauseTime = (clock.tick() / 1000) - pauseTime
						gameLoop()
		while gamePause == True:
			pauseTime = clock.tick()/1000
			screen.blit(background, (0, 0))
			message_to_screen("Game Paused, Press any key to continue or Esc to quit",red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameExit = True
						gamePause = False
					else:
						gamePause = False
						pauseTime = (clock.tick()/1000) - pauseTime

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gamePause = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos()
		times = clock.tick()/1000
		timer += times
		playtime += times
		speed = 1 -(timer * .008)
		if playtime>=speed:
			points = 0
			screen.blit(background, (0, 0))
			howClose = distanceFormula(randomX, randomY, mouseX, mouseY)
			print(howClose)
			if howClose <= 25:
				if colour == white:
					multi += 1
					points += 10
				elif colour == green:
					multi += 1
					points +=30
				elif colour == red:
					multi = 0
					points = -50
			elif howClose > 25 and colour == red:
				multi = multi
			else:
				multi = 0
			if multi < 5:
				multiplier = 1
			elif multi>=5 and multi <10:
				multiplier = 2
			elif multi>=10 and multi <15:
				multiplier = 3
			elif multi>=15 and multi <20:
				multiplier = 4
			elif multi>=20:
				multiplier =5
			score += points*multiplier
			randomX, randomY, colour = randomCircle()
			playtime -= speed
		if timer >= 60:
			gameEnd = True
		message_to_screen("X"+str(int(multiplier)), red, 100, -480, -320)
		message_to_screen("Score: "+str(int(score)), red, 100, 0, -320)
		message_to_screen("Time: "+str(int(timer - pauseTime)),red, 100, 380,-320)
		pygame.display.update()
	pygame.quit()
	quit()

gameStart()