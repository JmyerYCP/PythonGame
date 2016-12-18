import time
import pygame
import sys
import random
from math import *
from time import sleep
from pygame.locals import *


pygame.init()
bif = "bg2.bmp"
display_width=1080
display_height=720
screen=pygame.display.set_mode((display_width,display_height),0,32)
pygame.display.set_caption("Clicky! Clicky!")
score = 0
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue =  (0,0,255)
clock = pygame.time.Clock()
background=pygame.image.load(bif).convert()
	# Function to Find distance between two points.
def distanceFormula(x1,y1,x2,y2):
	distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	return distance

	# Default Message to Screen Function
def message_to_screen(msg,color, size=25,x_offset=0,y_offset=0):
	font = pygame.font.SysFont(None, size)
	screen_text = font.render(msg,True,color)
	textRect= screen_text.get_rect()
	textRect.center = (display_width/2+x_offset,display_height/2+y_offset)
	screen.blit(screen_text, textRect)

 # Random Circle Generator. Returns coordinates of circle
def randomCircle():
	randomX = random.randrange(25,display_width-25)
	randomY = random.randrange(100,display_height-25)
	circletype = random.randrange(1,15)
	if circletype <4:
		colour = red
		circlesize = 100
	elif circletype > 8 and circletype <13:
		colour = green
		circlesize = 25
	elif circletype >12:
		colour = blue
		circlesize = 15
	else:
		colour = white
		circlesize = 50
	pygame.draw.circle(screen, colour, (randomX,randomY),circlesize)
	return randomX,randomY,colour

	# Start menu
def gameStart():
	gameBegin = False
	while not gameBegin:
		pauseTime = clock.tick() / 1000
		screen.blit(background, (0, 0))
		pygame.draw.circle(screen, red, (int(display_width/5),100), 100)
		pygame.draw.circle(screen, white, (int(2*display_width/5),150), 50)
		pygame.draw.circle(screen, green, (int(3*display_width/5),175), 25)
		pygame.draw.circle(screen, blue, (int(4*display_width / 5), 190), 15)
		message_to_screen("-50 Points", red, 50,3 *-int(display_width/10),-125)
		message_to_screen("10 Points", white, 50,- int(display_width /10), -125)
		message_to_screen("30 Points", green, 50, int(display_width /10), -125)
		message_to_screen("50 Points", blue, 50,3* int(display_width / 10), -125)
		message_to_screen("Welcome", red, 150, 0,-50)
		message_to_screen("The object of this game", green, 50, 0, 10)
		message_to_screen("is to click on as many", green, 50, 0, 40)
		message_to_screen("non-red circles as possible.", green, 50, 0, 70)
		message_to_screen("For every 5 you click in a", green, 50, 0, 100)
		message_to_screen("row, you get a multiplyer,", green, 50, 0, 130)
		message_to_screen("up to x5", green, 50, 0, 160)
		message_to_screen("", red, 50, 0, 45)

		message_to_screen("Press any key to begin", red, 25, 0, 195)
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

def readhighscore():
	textr = open("highscore.txt", "r")
	top, secondtop, thirdtop, fourthtop, fifthtop = textr.readlines()
	top = int(top)
	secondtop = int(secondtop)
	thirdtop = int(thirdtop)
	fourthtop = int(fourthtop)
	fifthtop = int(fifthtop)
	return top,secondtop,thirdtop,fourthtop,fifthtop

def trackscore(topscore):
    textr = open("highscore.txt", "r")
    top,secondtop,thirdtop,fourthtop,fifthtop = textr.readlines()
    top = int(top)
    secondtop = int(secondtop)
    thirdtop = int(thirdtop)
    fourthtop = int(fourthtop)
    fifthtop = int(fifthtop)
    if topscore > top:
        fifthtop = fourthtop
        fourthtop = thirdtop
        thirdtop = secondtop
        secondtop = top
        top = topscore
        place = 1
    elif top >= topscore > secondtop:
        fifthtop = fourthtop
        fourthtop = thirdtop
        thirdtop = secondtop
        secondtop = topscore
        place = 2
    elif secondtop >= topscore > thirdtop:
        fifthtop = fourthtop
        fourthtop = thirdtop
        thirdtop = topscore
        place = 3
    elif thirdtop >= topscore > fourthtop:
        fifthtop = fourthtop
        fourthtop = topscore
        place = 4
    elif fourthtop >= topscore > fifthtop:
        fifthtop = topscore
        place = 5
    else:
        top = top
        secondtop = secondtop
        thirdtop = thirdtop
        fourthtop = fourthtop
        fifthtop = fifthtop
        place = 0
    textw = open('highscore.txt', 'w')
    teststring = [str(top) + "\n", str(secondtop) + "\n",str(thirdtop) + "\n",str(fourthtop) + "\n",str(fifthtop) + "\n"]
    textw.writelines(teststring)
    textw.close()
    return place

def trackname(place,name):
    textr = open("trackname.txt", "r")
    first, second, third, fourth, fifth = textr.readlines()
    textw = open('trackname.txt', 'w')
    if place == 1:
        teststring = [name + "\n", first,second,third,fourth[0:-1] + " "]
    elif place == 2:
        teststring = [ first,name + "\n",second, third, fourth[0:-1] + " "]
    elif place == 3:
        teststring = [first, second,name + "\n",third, fourth[0:-1] + " "]
    elif place == 4:
        teststring = [first, second, third,  name + "\n",fourth[0:-1] + " "]
    elif place == 5:
        teststring = [first, second,  third, fourth, name+ " "]
    else:
        teststring = [first, second, third, fourth,fifth]
    textw.writelines(teststring)

def readname():
	textr = open("trackname.txt", "r")
	first, second, third, fourth, fifth = textr.readlines()
	first = first[0:-1] + " "
	second = second[0:-1] + " "
	third = third[0:-1] + " "
	fourth = fourth[0:-1] + " "
	fifth = fifth
	return first,second,third,fourth,fifth

	# Main Game Loop
def gameLoop():
	gameExit = False
	gamePause = False
	gameEnd = False
	pauseTime = 0
	timer = 0
	playtime = 0
	randomX =0
	randomY = 0
	mouseX = -100
	mouseY = -100
	multiplier = 1
	colour = 0
	score= 0
	counter = 0
	screen.blit(background, (0, 0))
	while not gameExit:
		pygame.Surface.fill(screen,black,[0,0,display_width,75])

		#End Game Menu
		while gameEnd == True:
			if counter == 0:
				pauseTime = clock.tick() / 1000
				screen.blit(background, (0, 0))
				place = trackscore(score)
				top,secondtop,thirdtop,fourthtop,fifthtop = readhighscore()
				first,second,third,fourth,fifth = readname()
				if score > fifthtop:
					name = ""
					font = pygame.font.Font(None, 50)
					loop = True
					while loop == True:
						for evt in pygame.event.get():
							if evt.type == KEYDOWN:
								if evt.unicode.isalpha():
									name += evt.unicode
								elif evt.key == K_BACKSPACE:
									name = name[:-1]
								elif evt.key == K_RETURN:
									loop = False
								elif evt.key == K_SPACE:
									name += evt.unicode
							elif evt.type == QUIT:
								return
						screen.blit(background, (0, 0))
						block = font.render(name, True, green)
						rect = block.get_rect()
						rect.center = screen.get_rect().center
						screen.blit(block, rect)
						message_to_screen("GAME OVER", red, 200, 0, -250)
						message_to_screen("New Highscore! " + str(int(score)), red, 100, 0, -150)
						message_to_screen("Enter Nickname, then press 'ENTER'", red, 50, 0, -50)
						pygame.display.flip()
					trackname(place,name)
					first, second, third, fourth, fifth = readname()
					screen.blit(background, (0, 0))
					message_to_screen("GAME OVER", red, 200, 0, -250)
					message_to_screen("Highscores",red, 100,0,-150)
					message_to_screen(first + str(int(top)),red,75,0,-75)
					message_to_screen(second + str(int(secondtop)), red, 75, 0, -25)
					message_to_screen(third + str(int(thirdtop)), red, 75, 0, 25)
					message_to_screen(fourth + str(int(fourthtop)), red, 75, 0, 75)
					message_to_screen(fifth + " "+ str(int(fifthtop)), red, 75, 0, 125)
					message_to_screen("Press any key to try again or Esc to quit",red,25,0,200)
					pygame.display.update()
				else:
					message_to_screen("GAME OVER", red, 200, 0, -250)
					message_to_screen("Highscores", red, 100, 0, -150)
					message_to_screen(first + str(int(top)), red, 75, 0, -75)
					message_to_screen(second + str(int(secondtop)), red, 75, 0, -25)
					message_to_screen(third + str(int(thirdtop)), red, 75, 0, 25)
					message_to_screen(fourth + str(int(fourthtop)), red, 75, 0, 75)
					message_to_screen(fifth + " "+ str(int(fifthtop)), red, 75, 0, 125)
					message_to_screen("Press any key to try again or Esc to quit", red, 25, 0, 200)
					pygame.display.update()
			counter +=1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gameEnd = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameExit = True
						gameEnd = False
					else:
						gameEnd = False
						pauseTime = (clock.tick() / 1000) - pauseTime
						gameLoop()

		#Pause Menu
		while gamePause == True:
			pauseTime = clock.tick()/1000
			screen.blit(background, (0, 0))
			message_to_screen("Game Paused, Press any key to continue or Esc to quit",red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					gamePause = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameExit = True
						gamePause = False
					else:
						gamePause = False
						pauseTime = (clock.tick()/1000) - pauseTime
				if event.type == pygame.MOUSEBUTTONDOWN:
					gamePause = False
					pauseTime = (clock.tick() / 1000) - pauseTime
		#User Input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gamePause = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos()
		#Timer
		times = clock.tick()/1000
		timer += times
		timer -= pauseTime
		pauseTime = 0
		playtime += times
		speed = 1 -(timer * .008) #Speed modifier
		if playtime>=speed:
			points = 0
			screen.blit(background, (0, 0))
			howClose = distanceFormula(randomX, randomY, mouseX, mouseY)
			if howClose <= 100:
				if colour == white and howClose <= 50:
					multi += 1
					points += 10
				elif colour == white and howClose > 50:
					multi = 0
				elif colour == green and howClose <= 25:
					multi += 1
					points +=30
				elif colour == green and howClose > 25:
					multi = 0
				elif colour == blue and howClose <=15:
					multi +=1
					points +=50
				elif colour == blue and howClose >25:
					multi = 0
				elif colour == red:
					multi = 0
					points = -50
			elif colour == red and howClose > 100:
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
			mouseX = -100
			mouseY = -100
			randomX, randomY, colour = randomCircle()
			playtime -= speed

		if timer >= 60:
			gameEnd = True
		#Text to Screen
		message_to_screen("x"+str(int(multiplier)), red, 100, -480, -320)
		message_to_screen("Score: "+str(int(score)), red, 100, 0, -320)
		message_to_screen("Time: "+str(int(timer)),red, 100, 380,-320)
		pygame.display.update()
	pygame.quit()
	quit()

gameStart()
