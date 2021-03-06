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

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def playerHasHitBird(playerRect, birds):
    for b in birds:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# set up pygame, the window, and the mouse cursor [Thai]

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Bird Dodging Game! Dodge to Survive!!')
pygame.mouse.set_visible(False)

# set up fonts [Tran]
font = pygame.font.SysFont(None, 48)

# set up sounds [Thai]
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('backgroundmusic.mp3')

# set up images [Tran]
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
birdImage = pygame.image.load('bird.png')


# show the "Start" screen [Thai]
drawText('Bird Dodging Game! Good Luck!', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3))
drawText('Use your keyboard arrow or mouse cursor to navigate!', font, windowSurface, (WINDOWWIDTH / 3) - 250, (WINDOWHEIGHT / 3) + 50)
drawText('Press Space on your keyboard to start game!', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3) + 100)
drawText('This code was inspired by: sameerkhanna786 ', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3) + 300)
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
                    
# If the mouse moves, move the player where the cursor is. [Tran]

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

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)

        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)

        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)

        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)



# Move the mouse cursor to match the player. [Thai]

        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

# Move the birds down. [Tran]

        for b in birds:
                b['rect'].move_ip(0, b['speed'])

        for p in pokis:
            p['rect'].move_ip(0, p['speed'])


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



# Draw the game world on the window. [Tran]

        windowSurface.blit(BACKGROUNDCOLOR,(0,0))

# Draw the score and top score. [Thai]

        drawText('Current Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

# Draw the player's rectangle [Tran]

        windowSurface.blit(playerImage, playerRect)

# Draw each bird [Thai]

        for b in birds:
            windowSurface.blit(b['surface'], b['rect'])

        for p in pokis:
            windowSurface.blit(p['surface'], p['rect'])

        pygame.display.update()

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



# Stop the game and show the "Game Over" screen. [Thai]

    pygame.mixer.music.stop()

    gameOverSound.play()

    drawText('GAME OVER!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press Space on your keyboard to play again!', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 250)

    pygame.display.update()

    waitForPlayerToPressKey()

    gameOverSound.stop()