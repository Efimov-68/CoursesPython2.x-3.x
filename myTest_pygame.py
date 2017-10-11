'''
import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0, 100)
    top = random.randint(0, 500)
    left = random.randint(0, 500)
pygame.draw.rect(screen, [0,0,0], [left, top, width, height], 1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
'''
'''
import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
pygame.draw.rect(screen, [225,220,0],[250,150,300,200],2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
'''
'''
import pygame, sys
import math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255,255,255])
plotPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x,y])
pygame.draw.lines(screen, [0,0,0],False,plotPoints,5)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
'''
'''
import pygame, sys
pygame.init()
dots = [[221,432],[225,331],[133,342],[141,310],
        [51,230],[74,217],[58,153],[114,164],
        [123,135],[176,190],[159,77],[193,93],
        [230,28],[267,93],[301,77],[284,190],
        [327,135],[336,164],[402,153],[386,217],
        [409,230],[319,310],[327,342],[233,331],[237,432]]
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.lines(screen,[255,0,0],True,dots,2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
'''

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 10
screen.blit(my_ball,[x,y])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    if x > screen.get_width() - 90 or x < 0:
        x_speed = - x_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()
