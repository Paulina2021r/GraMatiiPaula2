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
blueX = 100
blueY = 120
Speedcar2 = 0
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




    meta(metaX, metaY)
    autko1(redX, redY)
    autko2(blueX, blueY)

    # koncowka
    pygame.display.update()