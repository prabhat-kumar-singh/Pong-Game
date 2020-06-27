import pygame

#initializing pygame
pygame.init()

#Setting the title of the game window
pygame.display.set_caption("Pong Game")

#creating window sreen
WIN_WIDTH = 800
WIN_HEIGHT = 600
mid_width = 400
mid_height = 300
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
on_start_screen = True

#creating font
font = pygame.font.SysFont('comicsans', 32)

#diffferent screens
def start_screen():
    start = font.render("Press Enter key to Start", 1, (0, 240, 0))
    screen.blit(start, (mid_width - 30, mid_height-16))
    pygame.display.update()

def mainPlayground():
    start = font.render("Game Play", 1, (0, 240, 0))
    screen.blit(start, (mid_width - 16, mid_height-16))
    pygame.display.update()
#gameloop

running = True
while running:

    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #key press event
    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    if on_start_screen:
        start_screen()
        if keys[pygame.K_KP_ENTER]:
            on_start_screen = False
    else:
        mainPlayground()

pygame.quit()


