import pygame

#initializing pygame
pygame.init()

#Setting the title of the game window
pygame.display.set_caption("Pong Game")

#Defining Clock
clock = pygame.time.Clock()

#creating window sreen
WIN_WIDTH = 800
WIN_HEIGHT = 600
mid_width = 400
mid_height = 300
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
on_start_screen = True

#creating font
font = pygame.font.SysFont('comicsans', 32)

#Ball
class Ball:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 5
        self.dirX = 1
        self.dirY = 1
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

    def move(self, screen):
        if self.x+self.radius > WIN_WIDTH or self.x - self.radius <0:
            self.dirX = self.dirX*-1
        elif self.y+self.radius > WIN_HEIGHT or self.y-self.radius<0:
            self.dirY = self.dirY*-1
        self.x+= self.vel*self.dirX
        self.y+= self.vel*self.dirY
        self.draw(screen)


#diffferent screens
def start_screen():
    start = font.render("Press Enter key to Start", 1, (0, 240, 0))
    screen.blit(start, (mid_width - 30, mid_height-16))
    pygame.display.update()

def mainPlayground():
    ball.move(screen)
    pygame.display.update()


#gameloop
ball = Ball(mid_width - 10, mid_height -10, (255, 0, 0), 25)

running = True
while running:

    #setting FPS
    clock.tick(30)
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


