import pygame
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
meta_start = pygame.image.load('zdjecia\metastart50.png')
pygame.display.set_icon(icon)
metaX = 0
metaY = 0
SpeedMetaX = 0
def meta(x, y):
    screen.blit(meta_start, (x, y))

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

#meta pygame
meta_Pygame = pygame.image.load('zdjecia\Bez-nazwy-1.png')
pygame.display.set_icon(icon)
meta_PygameX = 3770
meta_PygameY = 0
SpeedMeta_Pygame = 0
def ShowMeta (x, y):
    screen.blit(meta_Pygame, (x, y))






running = True

while running:
    # tło ekranu
    screen.fill((184, 225, 233))  # Red Green Blue 0-->255



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            SpeedMetaX = -0.3
            SpeedcarX = 0.06
            SpeedMeta_Pygame = -0.3
            #RUCH AUTKA KOMPUTERA
            Speedcar1 = 0.01
            redY += 0.001

        if event.key == pygame.K_UP:
            SpeedcarY = -0.3
        if event.key == pygame.K_DOWN:
            SpeedcarY = 0.3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            SpeedMetaX = 0
            SpeedMeta_Pygame = 0
            SpeedcarX = 0
            Speedcar1 = 0.05
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            SpeedcarY = 0
            SpeedMeta_Pygame = 0




    if redX >= 650:
        SpeedcarX = 0
        SpeedMeta_Pygame = 0
        SpeedMetaX = 0
        SpeedcarY = 0
        Speedcar1 = 0



    if blueX <  650:
        meta_PygameX += SpeedMeta_Pygame
        metaX += SpeedMetaX
        blueY += SpeedcarY
        blueX += SpeedcarX
        redX += Speedcar1
    elif blueX >= 650:
        SpeedcarX = 0
        SpeedMeta_Pygame = 0
        SpeedMetaX = 0
        SpeedcarY = 0
        Speedcar1 = 0



    print(redX)







    # ogranicz obszar gry
    if blueX <= 0:
        blueX = 0
    elif blueX >= 736:  #736
        bluerX = 736

    if blueY >= 550:  #
        blueY = 550
    elif blueY <= 250:  #536 - to do samej góry by było
        blueY = 250


    meta(metaX, metaY)
    autko1(redX, redY)
    autko2(blueX, blueY)
    ShowMeta(meta_PygameX, meta_PygameY)

#





    # koncowka
    pygame.display.update()