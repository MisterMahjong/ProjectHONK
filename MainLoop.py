#Importing the pygame module

import pygame
import random

#Initializing pygame module
pygame.init()

#Sets a caption for the game window
pygame.display.set_caption("Here Come The Clowns")

#Setting up my variables
playx = 800
playy= 600
playfield = pygame.display.set_mode((playx, playy))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clownx = 250
clowny = 150
hboxx = 50
hboxy = 50
xdirectionswitch = 1000
ydirectionswitch = 1000
xdirection = True
ydirection = True
GameOver = False


#defining images to be called in the program
Clowned = pygame.image.load("clown1.png")
bg = pygame.image.load("spooktown.jpg")

#Custom User Events

xdirswitch = pygame.USEREVENT + 1
ydirswitch = pygame.USEREVENT + 2

#Custom Movement Events

pygame.time.set_timer(xdirswitch, xdirectionswitch)
pygame.time.set_timer(ydirswitch, ydirectionswitch)

#Defining functions

def clown(x, y):
    global Clowned
    playfield.blit(Clowned,(x, y))

def scootup():
    global clowny
    clowny = clowny + 3

def scootdown():
    global clowny
    clowny = clowny - 3

def shuffleright():
    global clownx
    clownx = clownx + 3

def shuffleleft():
    global clownx
    clownx = clownx - 3

def hitbox(boxwidth, boxheight):
    global clownx
    pygame.draw.rect(playfield, WHITE, [clownx + hboxx, clowny + hboxy, boxwidth, boxheight], 5)


#The start of the "game loop", grabs events and checks to ensure our parameter =! True

while not GameOver:
    pygame.mouse.set_visible(1)
    playfield.blit(bg, (0, 0))
    clown(clownx, clowny)
    if ydirection == True:
        scootup()
    elif ydirection == False:
        scootdown()
    if xdirection == True:
        shuffleleft()
    elif xdirection == False:
        shuffleright()
    for x in pygame.event.get():
        if x.type == xdirswitch:
            xdirection = not xdirection
        if x.type == ydirswitch:
            ydirection = not ydirection
        if x.type == pygame.QUIT:
            GameOver = True
        if x.type == pygame.MOUSEBUTTONDOWN:
            print("HONK")
        if x.type == pygame.MOUSEBUTTONUP:
            print("HONK")
        print(x)
    pygame.display.update()
    pygame.time.Clock().tick(30)
pygame.quit()
quit()
