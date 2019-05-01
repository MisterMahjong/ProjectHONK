#Importing the pygame module

import pygame
import random

#Initializing pygame and pygame sound modules

pygame.init()
pygame.mixer.init()

#Assigning our sound files to callable audio

start = pygame.mixer.Sound("Start.wav")
winner = pygame.mixer.Sound('winlaugh.wav')
berate = pygame.mixer.Sound('hanklose.wav')
music = pygame.mixer.Sound('music.wav')
pain = pygame.mixer.Sound('pain.wav')
miss = pygame.mixer.Sound('miss.wav')
fire = pygame.mixer.Sound('pistol.wav')
loser = pygame.mixer.Sound('loser.wav')

#Setting audio levels for background music

pygame.mixer.Sound.set_volume(music, .3)
pygame.mixer.Sound.set_volume(loser, .8)
pygame.mixer.Sound.set_volume(miss, .3)

#Sets a caption for the game window

pygame.display.set_caption("Here Come The Clowns")

#Setting up my variables

playx = 800
playy= 600
playfield = pygame.display.set_mode((playx, playy))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clownx = 50
clowny = 50
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
MenuOver = False
score = 0
scoregoal = 30
gametimer = 30
scorefont = pygame.font.SysFont("applekidregular", 36, BLACK)
victorymessage = scorefont.render("YOU HONKING WIN", 1, BLACK)
failuremessage = scorefont.render("YOU HONKING LOSE", 1, WHITE)

#defining images to be called in the program

titlescreen = pygame.image.load("titlescreen.jpg")
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
    clowny = clowny + 7

def scootdown():
    global clowny
    clowny = clowny - 7

def shuffleright():
    global clownx
    clownx = clownx + 7

def shuffleleft():
    global clownx
    clownx = clownx - 7

def reset():
    global clownx, clowny, xdirection, ydirection
    if clownx > playx or clownx < playx - (playx * 1.10):
        xdirection = not xdirection
    if clowny > playy or clowny < playy - playy:
        ydirection = not ydirection

def movement():
    reset()
    if ydirection == True:
        scootup()
    elif ydirection == False:
        scootdown()
    if xdirection == True:
        shuffleleft()
    elif xdirection == False:
        shuffleright()



#The start of the "game loop", will continue to run so long as GameOver != True

pygame.mixer.Sound.play(start)
while not MenuOver:
    playfield.blit(titlescreen,(0,0))
    startbutton = pygame.draw.rect(playfield, WHITE, [playx * .2, playy * .6, 200, 100], 0)
    quitbutton = pygame.draw.rect(playfield, WHITE, [playx * .6, playy * .6, 200, 100], 0)
    pygame.display.update()
    pygame.time.Clock().tick(30)
    for x in pygame.event.get():
          if x.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = x.pos
            pygame.mixer.Sound.play(fire)
            if startbutton.collidepoint(mouse_pos):
                MenuOver = True
            if quitbutton.collidepoint(mouse_pos):
                MenuOver = True
                GameOver = True



pygame.mixer.Sound.play(music)
while not GameOver:

    #These statements draw the background and the image on the playfield

    scoreboard = scorefont.render("HONKS:" + ' ' + str(score), 1, WHITE)
    timeboard = scorefont.render("Time Remaining:" + ' ' + str(gametimer), 1, WHITE)
    pygame.mouse.set_visible(1)
    playfield.blit(bg, (0, 0))
    hitbox = pygame.draw.rect(playfield, WHITE, [clownx + hboxx, clowny + hboxy, 200, 200], 1)
    clown(clownx, clowny)
    playfield.blit(scoreboard, (50, 25))
    playfield.blit(timeboard, (50, 60))
    pygame.display.update()
    movement()

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
            pygame.mixer.Sound.play(fire)
            if hitbox.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(pain)
                score = score + 1
                print(score)
                if score == scoregoal:
                    pygame.mixer.stop()
                    pygame.mixer.Sound.play(winner)
                    playfield.blit(winclown, (0,0))
                    playfield.blit(victorymessage, (200, 300))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    pygame.quit()
            else:
                pygame.mixer.Sound.play(miss)
                gametimer = gametimer - 1

        if x.type == pygame.MOUSEBUTTONUP:
            print("HONK")


        if gametimer < 0:
            pygame.mixer.stop()
            playfield.blit(loseclown, (0, 0))
            playfield.blit(failuremessage, (200, 300))
            pygame.mixer.Sound.play(loser)
            pygame.mixer.Sound.play(berate)
            pygame.display.update()
            pygame.time.delay(5000)
            pygame.quit()

    pygame.time.Clock().tick(120)
pygame.quit()
quit()
