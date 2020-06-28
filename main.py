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

#paddle access
right = False
left = True
score = 0

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
        if self.y+self.radius > WIN_HEIGHT or self.y-self.radius<0:
            self.dirY = self.dirY*-1
        self.x+= self.vel*self.dirX
        self.y+= self.vel*self.dirY
        self.draw(screen)

#Paddel Class
class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 7

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))



#diffferent screens
def start_screen():
    start = font.render("Press Enter key to Start", 1, (0, 240, 0))
    screen.blit(start, (mid_width - 30, mid_height-16))
    pygame.display.update()

def mainPlayground():
    Score = font.render("Score: "+ str(score),1, (255, 200, 100))
    screen.blit(Score, (0, 0))
    ball.move(screen)
    paddleLeft.draw(screen)
    paddleRight.draw(screen)
    pygame.display.update()

def collision():
    global on_start_screen, right, left, score, ball, paddleLeft, paddleRight
    on_start_screen = True
    right = False
    left = True
    ball.x = mid_width - 10
    ball.y = mid_height - 10
    paddleLeft.y = 30
    paddleRight.y = 300
    score = 0

#gameloop
ball = Ball(mid_width - 10, mid_height -10, (255, 0, 0), 25)
paddleLeft = Paddle(0, 30, 20, 120, (255, 255, 255))
paddleRight = Paddle(WIN_WIDTH-20, 300, 20, 120, (255, 255, 255))

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

    #check if ball crosses the half width of window
    if ball.dirX >0:
        right = True
        left = False
    else:
        left = True
        right = False

    #move the paddle
    if keys[pygame.K_UP]:
        if right:
            paddle = paddleRight
        else:
            paddle = paddleLeft
        
        if paddle.y>0:
            paddle.y -= paddle.vel

    if keys[pygame.K_DOWN]:
        if right:
            paddle = paddleRight
        else:
            paddle = paddleLeft

        if paddle.y + paddle.height < WIN_HEIGHT:
            paddle.y += paddle.vel

    #check for collision
    if right:
        if ball.x+ball.radius == paddleRight.x and ball.y- ball.radius > paddleRight.y and ball.y <= paddleRight.y + paddleRight.height:
            ball.dirX = ball.dirX*-1
            score +=1
        elif ball.x+ball.radius > WIN_WIDTH or ball.x - ball.radius <0:
            collision()
    else:
        if ball.x-ball.radius == paddleLeft.x+paddleLeft.width and ball.y- ball.radius > paddleLeft.y and ball.y<= paddleLeft.y + paddleLeft.height:
            ball.dirX = ball.dirX*-1
            score+=1
        elif ball.x+ball.radius > WIN_WIDTH or ball.x - ball.radius <0:
            collision()

    screen.fill((0, 0, 0))
    if on_start_screen:
        start_screen()
        if keys[pygame.K_KP_ENTER]:
            on_start_screen = False
    else:
        mainPlayground()

pygame.quit()


