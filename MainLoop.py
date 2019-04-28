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
timercountdownswitch = 1000
xdirection = True
ydirection = True
GameOver = False
score = 0
gametimer = 30
scorefont = pygame.font.SysFont("arial", 36, BLACK)
victorymessage = scorefont.render("YOU HONKING WIN", 1, WHITE)
failuremessage = scorefont.render("YOU HONKING LOSE", 1, WHITE)

#defining images to be called in the program

Clowned = pygame.image.load("clown1.png")
bg = pygame.image.load("spooktown.jpg")
loseclown = pygame.image.load("sadclown.png")
winclown = pygame.image.load("happyclown.jpg")

#Custom User Events

xdirswitch = pygame.USEREVENT + 1
ydirswitch = pygame.USEREVENT + 2
timercountdown = pygame.USEREVENT + 3

#Custom Movement Events

pygame.time.set_timer(xdirswitch, xdirectionswitch)
pygame.time.set_timer(ydirswitch, ydirectionswitch)
pygame.time.set_timer(timercountdown, timercountdownswitch)

#Defining functions
def clown(x, y):
    global Clowned
    playfield.blit(Clowned,(x, y))

def scootup():
    global clowny
    clowny = clowny + 8

def scootdown():
    global clowny
    clowny = clowny - 8

def shuffleright():
    global clownx
    clownx = clownx + 8

def shuffleleft():
    global clownx
    clownx = clownx - 8

def reset():
    global clownx, clowny, xdirection, ydirection
    if clownx > 700 or clownx < -100:
        xdirection = not xdirection
    if clowny > 500 or clowny < -100:
        ydirection = not ydirection


#The start of the "game loop", grabs events and checks to ensure our parameter =! True

while not GameOver:

    #These statements draw the background and the image on the playfield
    scoreboard = scorefont.render("HONKER POINTS:" + ' ' + str(score), 1, WHITE)
    timeboard = scorefont.render("Time Remaining:" + ' ' + str(gametimer), 1, WHITE)
    pygame.mouse.set_visible(1)
    playfield.blit(bg, (0, 0))
    hitbox = pygame.draw.rect(playfield, WHITE, [clownx + hboxx, clowny + hboxy, 200, 200], 5)
    clown(clownx, clowny)
    playfield.blit(scoreboard, (50, 25))
    playfield.blit(timeboard, (50, 60))
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

        if x.type == timercountdown:
            gametimer = gametimer - 1

        if x.type == pygame.QUIT:
            GameOver = True

        if x.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = x.pos
            if hitbox.collidepoint(mouse_pos):
                score = score + 1
                print(score)
                if score == 10:
                    playfield.blit(winclown, (0,0))
                    playfield.blit(victorymessage, (200, 300))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    pygame.quit()

        if x.type == pygame.MOUSEBUTTONUP:
            print("HONK")

        if gametimer < 0:
            playfield.blit(loseclown, (0, 0))
            playfield.blit(failuremessage, (200, 300))
            pygame.display.update()
            pygame.time.delay(5000)
            pygame.quit()

    pygame.time.Clock().tick(60)
pygame.quit()
quit()
