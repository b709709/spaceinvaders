import pygame
import random

pygame.init()

#SCREEN WINDOW SETUP
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("spacebackground.png")


#ENEMY
enemyImg = pygame.image.load("enemy.png")
enemyWidth = enemyImg.get_width()
enemyHeight = enemyImg.get_height()
enemyX = random.randint(0,800-enemyWidth)
enemyY = random.randint(50,150)
enemyY = 50
enemyX_change = 3
enemyY_change = 0
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#PLAYER

playerImg = pygame.image.load("myship.png")
playerWidth = playerImg.get_width()
playerMiddle = playerWidth / 2
playerX = 370
playerY = 520
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

#BULLET
#ready - you can't see the bullet on the screen
#fire - the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 5
bulletX_change = 0
bulletStart = playerMiddle - (bulletImg.get_width() / 2)
bullet_state = "ready"
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

#GAME LOOP
brunning:bool = True
while brunning:

    #EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            brunning = False
        #PLAYER KEYBOARD EVENTS    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        

    #SCREEN UPDATING
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    #ENEMY UPDATING
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyHeight
    elif enemyX >= (800 - enemyWidth):
        enemyX_change = -3
        enemyY += enemyHeight

    #PLAYER UPDATING
    playerX += playerX_change
    if playerX <= 0:
       playerX = 0
    elif playerX >= (800 - playerWidth):
       playerX = (800 - playerWidth)

    #BULLET
    if bullet_state == "fire":
       fire_bullet(playerX,bulletY)
       bulletY -= bulletY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()
