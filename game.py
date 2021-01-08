import pygame
import os, sys

# Values
playerWidth = 16
playerHeight = 32
playerPosX = 264
playerPosY = 294
playerVel = 1
playerAnim = 3
playerWalkCount = 0


# Init PyGame module
pygame.init()
clock = pygame.time.Clock()
# Program Settings
icon = pygame.image.load('./sprites/icon32x32.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Debt Collector')
# Makes game run at 528x640 resolution
screen = pygame.display.set_mode((528,640))



# load data
drawbg = pygame.image.load('./sprites/bg.png')
bgmusic = pygame.mixer.music.load('./bgm/song.ogg')

playerStill = pygame.image.load('./sprites/player/playerStill.png')
walkLeft = [pygame.image.load('./sprites/player/playerWalk1L.png'), pygame.image.load('./sprites/player/playerWalk2L.png'),
            pygame.image.load('./sprites/player/playerWalk3L.png'), pygame.image.load('./sprites/player/playerWalk4L.png'),
            pygame.image.load('./sprites/player/playerWalk5L.png'), pygame.image.load('./sprites/player/playerWalk6L.png')]
walkRight = [pygame.image.load('./sprites/player/playerWalk1R.png'), pygame.image.load('./sprites/player/playerWalk2R.png'),
            pygame.image.load('./sprites/player/playerWalk3R.png'), pygame.image.load('./sprites/player/playerWalk4R.png'),
            pygame.image.load('./sprites/player/playerWalk5R.png'), pygame.image.load('./sprites/player/playerWalk6R.png')]



# Startup (Load bg and play bgm)
screen.blit(drawbg,(0,0))
pygame.display.flip()
pygame.mixer.music.play(loops=-1)

# Draw Window
def DrawGameWindow():
    screen.blit(playerStill, (playerPosX,playerPosY))
    pygame.display.update()

# Running
running = True

while running:
    # Keyboard Controls
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        playerPosX -= playerVel
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        playerPosX += playerVel
    if pygame.key.get_pressed()[pygame.K_UP]:
        playerPosY -= playerVel
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        playerPosY += playerVel

    DrawGameWindow()

    # Checks all events occuring in PyGame
    for event in pygame.event.get():
        # If user quits then exit
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
