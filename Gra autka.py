import pygame  # string
import random
import sys



# rozpocznij program
pygame.init()

# stworz ekran gry
screen = pygame.display.set_mode((800, 600))  # szerokość

# nazwa gry
pygame.display.set_caption('Wyścigi samochodowe')

# ikona gry
icon = pygame.image.load('zdjecia/tyre.png')
pygame.display.set_icon(icon)

#meta i start
meta_start = pygame.image.load('zdjecia\Bez-nazwy-2.png')
pygame.display.set_icon(icon)
metaX = 0
metaY = 0

# autko1 red
autored = pygame.image.load('zdjecia\carobrotony1.png')
pygame.display.set_icon(icon)
redX = 20
redY = 20
Speedcar1 = 0
def autko1(x, y):
    screen.blit(autored, (x, y))
#autko2
autoblue = pygame.image.load('zdjecia\carblue1.png')
pygame.display.set_icon(icon)
blueX = 10
blueY = 450
SpeedcarX = 0
SpeedcarY = 0
def autko2(x, y):
    screen.blit(autoblue, (x, y))



#meta
def meta(x, y):
    screen.blit(meta_start, (x, y))


running = True

while running:
    # tło ekranu
    screen.fill((184, 225, 233))  # Red Green Blue 0-->255




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            SpeedcarX = 0.3
        if event.key == pygame.K_LEFT:
            SpeedcarX = -0.3
        if event.key == pygame.K_UP:
            SpeedcarY = -0.3
        if event.key == pygame.K_DOWN:
            SpeedcarY = 0.3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            SpeedcarX = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            SpeedcarY = 0

    blueX += SpeedcarX
    blueY += SpeedcarY



    meta(metaX, metaY)
    autko1(redX, redY)
    autko2(blueX, blueY)

    # koncowka
    pygame.display.update()