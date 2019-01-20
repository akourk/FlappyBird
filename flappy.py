import pygame
import random
pygame.init()
pygame.font.init()
display_width = 1200
display_height = 800
pipe_width = 75
pipe_gap = 800
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
display = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

def drawCircle (x, y, color):
    pygame.draw.circle(display, color, (x, y), 20, 0)

def drawPipes (x, y, color):
    pygame.draw.rect(display, color, (x, y-pipe_gap, pipe_width, 600), 0)
    pygame.draw.rect(display, color, (x, y, pipe_width, 600), 0)

def intro():
    start = True
    while start:
        display.fill(black)
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render("Welcome! Press any key to start!", True, blue, black)
        textrect = text.get_rect()
        textrect.centerx = display.get_rect().centerx
        textrect.centery = display.get_rect().centery
        display.blit(text, textrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                start = False

        pygame.display.update()
        clock.tick(60)

def scorescreen(score):
    end = True
    while end:
        display.fill(black)
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render("Oops, you died. Your score was: " + str(score), True, blue, black)
        textrect = text.get_rect()
        textrect.centerx = display.get_rect().centerx
        textrect.centery = display.get_rect().centery
        display.blit(text, textrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                end = False

        pygame.display.update()
        clock.tick(60)

def game_loop():
    done = False
    disco_mode = True
    x = display_width/2
    y = display_height/2
    pipe_x = display_width+pipe_width
    pipe_y = 400
    pipe_x2 = display_width / 2
    pipe_y2 = 400
    pipe_vel = 15
    y2 = 0
    bird_accel = 0
    elapsed = 700
    disco1 = 0
    disco2 = 0
    disco3 = 0
    k = 0

    intro()


    while not done:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                done = True

            if (event.type == pygame.KEYDOWN):
                bird_accel = -12

            elif (event.type == pygame.KEYUP):
                y2 = 0

        y += y2
        y += bird_accel*2
        if (bird_accel < 15):
            bird_accel += 1

        if (pipe_x > 0 - pipe_width):
            pipe_x -= pipe_vel
        else:
            pipe_x = display_width + pipe_width
            pipe_y = random.randint(display_height*.27, display_height*.95)

        if (pipe_x2 > 0 - pipe_width):
            pipe_x2 -= pipe_vel
        else:
            pipe_x2 = display_width + pipe_width
            pipe_y2 = random.randint(display_height*.27, display_height*.95)


        if y < pipe_y - 200 and pipe_x < display_width / 2 + 25 and pipe_x > display_width / 2 - 85:
            done = True

        if y > pipe_y and pipe_x < display_width / 2 + 25 and pipe_x > display_width / 2 - 25:
            done = True

        if y < pipe_y2 - 200 and pipe_x2 < display_width / 2 + 25 and pipe_x2 > display_width / 2 - 85:
            done = True

        if y > pipe_y2 and pipe_x2 < display_width / 2 + 25 and pipe_x2 > display_width / 2 - 25:
            done = True


        elapsed += pipe_vel
        score = elapsed / 687

        display.fill(black)

        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render(str(score), True, blue, black)
        textrect = text.get_rect()
        textrect.centerx = display.get_rect().centerx
        textrect.centery = display.get_rect().centery
        display.blit(text, textrect)

        if(disco_mode == True):
            if(k == 0):
                disco1 += 10
            elif(k == 1):
                disco2 += 10
            elif(k == 2):
                disco3 += 10
            if(disco1 >= 245):
                disco1 = 0
            if(disco2 >= 245):
                disco2 = 0
            if(disco3 >= 245):
                disco3 = 0
            k = random.randint(0, 3)
            disco = (disco1, disco2, disco3)
            disco_pipe2 = (disco2, disco3, disco1)
            drawPipes(pipe_x, pipe_y, disco)
            drawPipes(pipe_x2, pipe_y2, disco_pipe2)

        if(disco_mode == False):
            drawPipes(pipe_x, pipe_y, green)
            drawPipes(pipe_x2, pipe_y2, green)

        drawCircle(x, y, white)
        pygame.display.update()
        clock.tick(60)

    scorescreen(score)

game_loop()
pygame.quit()
quit()














