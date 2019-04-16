import pygame


def clown(x, y):
    global Clowned
    global playfield
    playfield.blit(Clowned,(x, y))

def shuffleleft():
    global clownx
    clownx = clownx + 10
    if clownx > 900:
        clownx = clownx -1600

