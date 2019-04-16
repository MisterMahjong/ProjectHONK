#Importing the pygame module

import pygame
import random

#Initializing pygame module
pygame.init()

#Sets a caption for the game window
pygame.display.set_caption("onHere Come The Clowns")

#Setting up my variables
playx = 800
playy= 600
playfield = pygame.display.set_mode((playx, playy))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x = (playx)
y = (playy)
clownx = 50
clowny = 50
GameOver = False
ticktock = 0

#defining images to be called in the program
Clowned = pygame.image.load("clown1.png")
bg = pygame.image.load("spooktown.jpg")

#Defining functions

def clown(x, y):
    global Clowned
    playfield.blit(Clowned,(x, y))

def shuffleright():
    global clownx
    clownx = clownx + 5

def shuffleleft():
    global clownx
    clownx = clownx - 5

def truffleshuffle():
    global clownx
    shuffleright()

    shuffleleft()

#The start of the "game loop", grabs events and checks to ensure our parameter =! True
while not GameOver:
    playfield.blit(bg, (0, 0))
    clown(clownx, clowny)
    truffleshuffle()
    ticktock = pygame.time.get_ticks()
    print(ticktock)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        elif event.type == pygame.mouse.get_pressed(5):
            GameOver = True
        print(event)
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
quit()
