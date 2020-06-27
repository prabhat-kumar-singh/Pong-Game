import pygame

#initializing pygame
pygame.init()

#Setting the title of the game window
pygame.display.set_caption("Pong Game")

#creating window sreen
WIN_WIDTH = 800
WIN_HEIGHT = 600

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


#gameloop

running = True
while running:

    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()


