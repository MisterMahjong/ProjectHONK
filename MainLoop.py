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
timer = 0
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
    clownx = clownx + .1

def shuffleleft():
    global clownx
    clownx = clownx - 1

def hitbox():
    global clownx
    pygame.draw.rect(playfield, WHITE, [clownx + 250, clowny + 50, 275, 650], 5)

#The start of the "game loop", grabs events and checks to ensure our parameter =! True

while not GameOver:
    playfield.blit(bg, (0, 0))
    clown(clownx, clowny)
    shuffleleft()
    hitbox()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            p, q = event.pos
            if hitbox().collidepoint(p, q):
                print('Successful Strike')
        if event.type == pygame.MOUSEBUTTONUP:
            print("HONK")
        print(event)
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
quit()
