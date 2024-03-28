import sys
import pygame
from pygame.locals import *
from const import *

import image
import objectbase

size = (1200,600)
POS = (0,0)

pygame.init()

DS = pygame.display.set_mode(size)

img = image.Image(PATH_BACK,0,POS,size,0)
kun = objectbase.ObjectBase('pic/kun/kao/%d.png',0,(1200,200),(100,128),16)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DS.fill((255,255,255))

    img.draw(DS)
    kun.update()
    kun.draw(DS)
    pygame.display.update()