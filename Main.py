#Bird Dodging Game
#Coders: Thai Cao, Tran Huynh

#Setup Game

import pygame, random, sys
from pygame.locals import *



WINDOWWIDTH = 1200
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = pygame.image.load('CloudBackground.png')
FPS = 120
BIRDMINSIZE = 40
BIRDMAXSIZE = 50
BIRDMINSPEED = 2
BIRDMAXSPEED = 10
ADDNEWBIRDRATE = 3
PLAYERMOVERATE = 25
