#Importing the pygame module

import pygame

#Setting up my variables

playx = 800
playy= 600
playfield = pygame.display.set_mode((playx, playy))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clownx = 50
clowny = 50
hboxx = 15
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
titleswap = True
clownswap = True
gruntstate = True
paincounter = 90
score = 0
scoregoal = 50
gametimer = 45

#Initializing pygame and pygame sound modules

pygame.init()
pygame.mixer.init()

#defining images to be called in the program

titlescreen1 = pygame.image.load("title1.jpg")
titlescreen2 = pygame.image.load("title2.jpg")
titlequit = pygame.image.load("titlequit.jpg")
titleplay = pygame.image.load("showtime.jpg")
Clowned = pygame.image.load("clown1.png")
painedstate = pygame.image.load("pain.png")
bg = pygame.image.load("bg.jpg")
loseclown = pygame.image.load("lose.jpg")
winclown = pygame.image.load("winscreen.jpg")


#Assigning our sound files to callable audio

start = pygame.mixer.Sound("Start.wav")
winner = pygame.mixer.Sound('winner.wav')
quitter = pygame.mixer.Sound('quitquote.wav')
berate = pygame.mixer.Sound('berate.wav')
music = pygame.mixer.Sound('music.wav')
grunt1 = pygame.mixer.Sound('grunt1.wav')
grunt2 = pygame.mixer.Sound('grunt2.wav')
miss = pygame.mixer.Sound('miss.wav')
fire = pygame.mixer.Sound('pistol.wav')
loser = pygame.mixer.Sound('loser.wav')
playtime = pygame.mixer.Sound('showtime.wav')
winsong = pygame.mixer.Sound('winsong.wav')

#Setting audio levels so I don't blow your ears out

pygame.mixer.Sound.set_volume(playtime, .8)
pygame.mixer.Sound.set_volume(fire, .7)
pygame.mixer.Sound.set_volume(winsong, .3)
pygame.mixer.Sound.set_volume(music, .3)
pygame.mixer.Sound.set_volume(miss, .2)

#Setting fonts and special messages

messagefont = pygame.font.SysFont("fourside", 32, BLACK)
scorefont = pygame.font.SysFont("applekidregular", 36, BLACK)
victorymessage = messagefont.render("YOU HONKING WIN", 1, WHITE)
failuremessage = messagefont.render("YOU HONKING LOSE", 1, WHITE)
cryforhelp = scorefont.render("WHY DID I MAKE THIS", 1, WHITE)
playgame = messagefont.render("PLAY", 1, WHITE)
exitgame = messagefont.render("QUIT", 1, WHITE)


#Sets a caption for the game window

pygame.display.set_caption("CLOWN CLICKER TURBO")

#Custom User Events

xdirswitch = pygame.USEREVENT + 1
ydirswitch = pygame.USEREVENT + 2
timercountdown = pygame.USEREVENT + 3

#Custom Movement Events

pygame.time.set_timer(xdirswitch, xdirectionswitch)
pygame.time.set_timer(ydirswitch, ydirectionswitch)
pygame.time.set_timer(timercountdown, timercountdownswitch)

#Defining functions

def countdown():
    count = 5
    while count != 0:
        playfield.blit(bg, (0, 0))
        countdownmessage1 = messagefont.render("GET READY TO HONK IN" + ' ' + str(count), 1, WHITE)
        countdownmessage2 = scorefont.render("Honk him 50 times to win", 1, WHITE)
        countdownmessage3 = scorefont.render("1 miss = 1 second lost", 1, WHITE)
        playfield.blit(countdownmessage1, (100, 200))
        playfield.blit(countdownmessage2, (275, 300))
        playfield.blit(countdownmessage3, (300, 450))
        pygame.display.update()
        pygame.time.delay(1000)
        count = count - 1

def clown(x, y):
    global Clowned, painedstate, clownswap
    if clownswap == True:
        playfield.blit(Clowned, (x, y))
    elif clownswap == False:
        playfield.blit(painedstate, (x, y))

def grunt():
    global grunt1, grunt2, gruntstate
    if gruntstate == True:
        pygame.mixer.Sound.play(grunt1)
    elif gruntstate == False:
        pygame.mixer.Sound.play(grunt2)
    gruntstate = not gruntstate

def scootup():
    global clowny
    clowny = clowny + 12

def scootdown():
    global clowny
    clowny = clowny - 12

def shuffleright():
    global clownx
    clownx = clownx + 12

def shuffleleft():
    global clownx
    clownx = clownx - 12

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



#The chunk of code below is the menu loop. The game will remain on the menu until the player selects either the play
#or start buttons. (or they decide to x out)

pygame.mixer.Sound.play(start, -1)
while not MenuOver:
    if titleswap == True:
        playfield.blit(titlescreen1,(0,0))
        titleswap = not titleswap
    elif titleswap == False:
        playfield.blit(titlescreen2, (0,0))
        titleswap = not titleswap
    startbutton = pygame.draw.rect(playfield, BLACK, [playx * .2, playy * .6, 200, 100], 0)
    quitbutton = pygame.draw.rect(playfield, BLACK, [playx * .6, playy * .6, 200, 100], 0)
    playfield.blit(playgame, (playx * .25, playy * .65))
    playfield.blit(exitgame, (playx * .65, playy * .65))
    pygame.display.update()
    pygame.time.Clock().tick(30)
    for x in pygame.event.get():
          if x.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = x.pos
            pygame.mixer.Sound.play(fire)
            if startbutton.collidepoint(mouse_pos):
                playfield.blit(titleplay, (0,0))
                pygame.mixer.Sound.play(playtime)
                pygame.display.update()
                pygame.time.delay(1500)
                playfield.blit(cryforhelp, (0, 0))
                pygame.display.update()
                pygame.time.delay(650)
                MenuOver = True
            if quitbutton.collidepoint(mouse_pos):
                playfield.blit(titlequit, (0,0))
                pygame.display.update()
                pygame.mixer.Sound.play(quitter)
                pygame.time.delay(3000)
                quit()
countdown()
pygame.mixer.stop()

#The start of the "game loop", will continue to run so long as GameOver != True
#The pygame set_grab locks the mouse inside the window for the duration of the game

pygame.event.set_grab(True)
pygame.mixer.Sound.play(music, -1)
while not GameOver:

    #These statements draw the background and the image on the playfield

    scoreboard = scorefont.render("HONKS:" + ' ' + str(score), 1, WHITE)
    timeboard = scorefont.render("Time Remaining:" + ' ' + str(gametimer), 1, WHITE)
    pygame.mouse.set_visible(1)
    playfield.blit(bg, (0, 0))
    hitbox = pygame.draw.rect(playfield, WHITE, [clownx + hboxx, clowny + hboxy, 200, 175], 1)
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
                grunt()
                clownswap = not clownswap
                pygame.display.update()
                score = score + 1
                if score == scoregoal:
                    pygame.mixer.stop()
                    pygame.mixer.Sound.play(winner)
                    pygame.mixer.Sound.play(winsong)
                    playfield.blit(winclown, (0, 0))
                    playfield.blit(victorymessage, (200, 300))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    pygame.quit()
            else:
                pygame.mixer.Sound.play(miss)
                gametimer = gametimer - 1

        if gametimer < 0:
            pygame.mixer.stop()
            playfield.blit(loseclown, (0, 0))
            playfield.blit(failuremessage, (200, 300))
            pygame.mixer.Sound.play(loser)
            pygame.mixer.Sound.play(berate)
            pygame.display.update()
            pygame.time.delay(5000)
            quit()

    pygame.time.Clock().tick(60)
pygame.quit()
quit()
