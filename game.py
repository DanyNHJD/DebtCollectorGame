import pygame
import os, sys

# Values - Player
playerPosX = 264
playerPosY = 294
playerVel = 4
playerWalkCount = 0
playerIsLeft = False
playerIsRight = False
# 0 = Left, 1 = Right
playerLastDirection = 1

# Values - Controlled Variables
playerWidth = 16
playerHeight = 32
FPS = 30

# Values - Bounderies
LeftBorder = 24
RightBorder = 503 - playerWidth
TopBorder = 56
BottomBorder = 615 - playerHeight


# Init PyGame module
pygame.init()
clock = pygame.time.Clock()
# Program Settings
icon = pygame.image.load('./sprites/icon32x32.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Debt Collector')
# Makes game run at 528x640 resolution
screen = pygame.display.set_mode((528,640))


# Load data
drawbg = pygame.image.load('./sprites/bg.png')
bgmusic = pygame.mixer.music.load('./bgm/song.ogg')

playerStillR = pygame.image.load('./sprites/player/playerStillR.png')
playerStillL = pygame.image.load('./sprites/player/playerStillL.png')
walkLeft = [pygame.image.load('./sprites/player/playerWalk1L.png'), pygame.image.load('./sprites/player/playerWalk2L.png'),
            pygame.image.load('./sprites/player/playerWalk3L.png'), pygame.image.load('./sprites/player/playerWalk4L.png'),
            pygame.image.load('./sprites/player/playerWalk5L.png'), pygame.image.load('./sprites/player/playerWalk6L.png')]
walkRight = [pygame.image.load('./sprites/player/playerWalk1R.png'), pygame.image.load('./sprites/player/playerWalk2R.png'),
            pygame.image.load('./sprites/player/playerWalk3R.png'), pygame.image.load('./sprites/player/playerWalk4R.png'),
            pygame.image.load('./sprites/player/playerWalk5R.png'), pygame.image.load('./sprites/player/playerWalk6R.png')]



# Startup (Load bg and play bgm)
pygame.display.flip()
pygame.mixer.music.play(loops=-1)

# Draw Window & GUI
def DrawGameWindow():
    pygame.display.update()
    screen.blit(drawbg,(0,0))

# Player Character
def Player():
    global playerWalkCount
    # Character Walking animations
    if playerWalkCount + 1 >= 18:
        playerWalkCount = 0
    if playerIsLeft:
        screen.blit(walkLeft[playerWalkCount//3], (playerPosX, playerPosY))
        playerWalkCount += 1
    elif playerIsRight:
        screen.blit(walkRight[playerWalkCount//3], (playerPosX, playerPosY))
        playerWalkCount += 1
    else:
        if playerLastDirection == 0:
            screen.blit(playerStillL, (playerPosX, playerPosY))
        else:
            screen.blit(playerStillR, (playerPosX, playerPosY))
    pygame.display.update()

# Running
running = True

while running:
    clock.tick(FPS)

    # Keyboard Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerPosX > LeftBorder:
        playerPosX -= playerVel
        playerIsLeft = True
        playerIsRight = False
        playerLastDirection = 0
    elif keys[pygame.K_RIGHT] and playerPosX < RightBorder:
        playerPosX += playerVel
        playerIsLeft = False
        playerIsRight = True
        playerLastDirection = 1

    elif keys[pygame.K_UP] and playerPosY > TopBorder:
        playerPosY -= playerVel
        if playerLastDirection == 0:
            playerIsLeft = True
            playerIsRight = False
        elif playerLastDirection == 1:
            playerIsLeft = False
            playerIsRight = True

    elif keys[pygame.K_DOWN] and playerPosY < BottomBorder:
        playerPosY += playerVel
        if playerLastDirection == 0:
            playerIsLeft = True
            playerIsRight = False
        elif playerLastDirection == 1:
            playerIsLeft = False
            playerIsRight = True
    else:
        playerIsLeft = False
        playerIsRight = False
        playerWalkCount = 0

    DrawGameWindow()
    Player()

    # Checks all events occuring in PyGame
    for event in pygame.event.get():
        # If user quits then exit
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
