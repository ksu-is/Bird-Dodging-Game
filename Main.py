#Bird Dodging Game
#Coders: Thai Cao, Tran Huynh

#Setup Game [Thai]
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

# set up pygame, the window, and the mouse cursor [Thai]
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWHEIGHT,WINDOWWIDTH))
pyhame.mouse.set_visible(False)

# set up fonts [Tran]
font = pygame.font.SysFont(None, 48)

# set up sounds [Tran]


# set up images [Thai]
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
birdImage = pygame.image.load('bird.png')

# show the "Start" screen [Tran]

# set up the start of the game [Tran]



# the game loop runs while the game part is playing [Thai]

    while True: 
        playerMove = False
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True

                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True

                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True

                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0

                if event.key == ord('x'):
                    slowCheat = False
                    score = 0

                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    playerMove = True
                    moveLeft = False

                if event.key == K_RIGHT or event.key == ord('d'):
                    playerMove = True
                    moveRight = False

                if event.key == K_UP or event.key == ord('w'):
                    playerMove = True
                    moveUp = False

                if event.key == K_DOWN or event.key == ord('s'):
                    playerMove = True
                    moveDown = False
# If the mouse moves, move the player where the cursor is. [Thai]
            if event.type == MOUSEMOTION:
                playerMove = True
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

# Add new birds at the top of the screen, if needed. [Thai]

        while len(birds) < ADDNEWBIRDRATE:
            birdSize = random.randint(BIRDMINSIZE, BIRDMAXSIZE)
            newBird = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-birdSize), 0 - birdSize, birdSize, birdSize),
                        'speed': random.randint(BIRDMINSPEED, BIRDMAXSPEED),
                        'surface':pygame.transform.scale(birdImage, (birdSize, birdSize)),
                        }
            birds.append(newBird)

        if score%1000 == 0 and score != 0 and len(pokis)<2:
            newPoki = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-BIRDMAXSIZE), 0 - BIRDMAXSIZE, BIRDMAXSIZE, BIRDMAXSIZE),
                        'speed': BIRDMINSPEED,
                        'surface':pygame.transform.scale(pokiImage, (BIRDMAXSIZE, BIRDMAXSIZE)),
                        }
            pokis.append(newPoki)
# Move the player around. [Tran]

 



# Move the mouse cursor to match the player. [Thai]

        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

# Move the birds down. [Tran]

 

# Delete birds that have fallen past the bottom. [Thai]

        for b in birds[:]:
            if b['rect'].top > WINDOWHEIGHT:
                birds.remove(b)
                score += 2

                if BIRDMAXSPEED < 30:
                    BIRDMAXSPEED += 1

                if score%5 == 0 and score != 0:
                    print(score)
                    ADDNEWBIRDRATE += 1

        for p in pokis[:]:
            if p['rect'].top > WINDOWHEIGHT:
                pokis.remove(p)
                score -= 1000
# Draw the game world on the window. [Thai]
        windowSurface.blit(BACKGROUNDCOLOR,(0,0))
# Draw the score and top score. [Tran]

       
# Draw the player's rectangle [Tran]

       
# Draw each bird [Thai]
        drawText('Current Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
# Check if any of the birds have hit the player. [Tran]

        


# Stop the game and show the "Game Over" screen. [Tran]
