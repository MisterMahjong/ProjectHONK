#Importing the pygame module
import pygame
import pygame
#Initializing pygame module
pygame.init()
#Defining the screen/play area of the game, and the screen size.
playfield = pygame.display.set_mode((800,600))
#Sets a caption for the game window
pygame.display.set_caption("Here Come The Clowns")
#Sets a parameter to be used by the "game loop"
WHITE = (255,255,255)
GameOver = False
#The start of the "game loop", grabs events and checks to ensure our parameter =! True

while not GameOver:
    pygame.draw.rect(playfield,WHITE,[30,30,100, 100],0)
    for event in pygame.event.get():
        if event.type == pygame.mouse.get_pos():
            print("THAT'S THE SPOT!")
        if event.type == pygame.QUIT:
            GameOver = True
        print(event)
    pygame.display.update()
    time.clock()
pygame.quit()
quit()

#adding some lines
#to test the version control
#i hope this works.
#Made a change
