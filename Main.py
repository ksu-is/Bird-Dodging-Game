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

# set up fonts [Tran]
font = pygame.font.SysFont(None, 48)

# set up sounds [Tran]
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mp3')

# set up images [Thai]

# show the "Start" screen [Tran]
drawText('Bird Dodging Game! Good Luck!', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWWEIGHT / 3))
drawText('Use your keyboard arrow or mouse cursor to navigate!', font, windowSurface, (WINDOWWIDTH / 3) - 250, (WINDOWHEIGHT / 3) + 50)
drawText('Press Space on your keyboard to start game!', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3) + 100)
drawText('This code was inspiried by: sameerkhanna786 ', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3) + 300)
drawText('Coded by: Thai Cao & Tran Huynh', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3) + 350)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0

# set up the start of the game [Tran]

while True:
    birds = []
    pokis = []
    score = 0

    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False

    birdAddCounter = 0
    
    pygame.mixer.music.play(-1, 0.0)


# the game loop runs while the game part is playing [Thai]

# If the mouse moves, move the player where the cursor is. [Thai]

# Add new birds at the top of the screen, if needed. [Thai]

# Move the player around. [Tran]

 if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)

        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)

        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)

        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)



# Move the mouse cursor to match the player. [Thai]

# Move the birds down. [Tran]

 for b in birds:
                b['rect'].move_ip(0, b['speed'])

        for p in pokis:
            p['rect'].move_ip(0, p['speed'])



# Delete birds that have fallen past the bottom. [Thai]

# Draw the game world on the window. [Thai]

# Draw the score and top score. [Tran]

        drawText('Current Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

# Draw the player's rectangle [Tran]

        windowSurface.blit(playerImage, playerRect)

# Draw each bird [Thai]

# Check if any of the birds have hit the player. [Tran]

        if playerHasHitBird(playerRect, birds):
            ADDNEWBIRDRATE = 3
            BIRDMAXSPEED = 10

            if score > topScore:
                topScore = score # set new top score
            break



        if playerHasHitBird(playerRect, pokis):
            score += 1000
            ADDNEWBIRDRATE = 3
            BIRDMAXSPEED = 10
            for p in pokis[:]:
                pokis.remove(p)

        mainClock.tick(FPS)



# Stop the game and show the "Game Over" screen. [Tran]

    pygame.mixer.music.stop()

    gameOverSound.play()
