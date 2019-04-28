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
hboxx = 0
hboxy = 50
xcounter = 3
ycounter = 5
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
    clowny = clowny + 10

def scootdown():
    global clowny
    clowny = clowny - 10

def shuffleright():
    global clownx
    clownx = clownx + 10

def shuffleleft():
    global clownx
    clownx = clownx - 10

def reset():
    global clownx, clowny, xdirection, ydirection
    if clownx > 700 or clownx < -100:
        xdirection = not xdirection
    if clowny > 500 or clowny < -100:
        ydirection = not ydirection


#The start of the "game loop", grabs events and checks to ensure our parameter =! True

while not GameOver:

    #These statements draw the background and the image on the playfield

    pygame.mouse.set_visible(1)
    playfield.blit(bg, (0, 0))
    clown(clownx, clowny)
    hitbox = pygame.draw.rect(playfield, WHITE, [clownx + hboxx, clowny + hboxy, 200, 200], 5)
    pygame.display.update()
    #These statements determine the x/y movement of the image

    reset()
    if ydirection == True:
        scootup()
    elif ydirection == False:
        scootdown()
    if xdirection == True:
        shuffleleft()
    elif xdirection == False:
        shuffleright()

    #These statements pull from a list of events and execute the given code when the appropriate events are pulled.

    for x in pygame.event.get():
        if x.type == xdirswitch:
            if xcounter > 0:
                xcounter = xcounter - 1
            elif xcounter == 0:
                xdirection = not xdirection
                xcounter = 3

        if x.type == ydirswitch:
            if ycounter > 0:
                ycounter = ycounter - 1
            elif ycounter == 0:
                ydirection = not ydirection
                ycounter = 5

        if x.type == pygame.QUIT:
            GameOver = True
        if x.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = x.pos
            if hitbox.collidepoint(mouse_pos):
                print("OH SHIT")
        if x.type == pygame.MOUSEBUTTONUP:
            print("HONK")
        print(x)
    pygame.time.Clock().tick(30)
pygame.quit()
quit()
