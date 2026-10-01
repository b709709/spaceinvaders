import pygame
import random
import math

pygame.init()

#SCREEN WINDOW SETUP
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("spacebackground.png")


#ENEMY
enemyImg = []
enemyWidth = []
enemyHeight = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyWidth.append(enemyImg[i].get_width())
    enemyHeight.append(enemyImg[i].get_height())
    enemyX.append(random.randint(0,800-enemyWidth[i]))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3)
    enemyY_change.append(0)

#enemyY = 50
    
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

#PLAYER
playerImg = pygame.image.load("myship.png")
playerWidth = playerImg.get_width()
playerMiddle = playerWidth / 2
playerX = 370
playerY = 520
playerX_change = 0


#SCORE
score_value = 0
font = pygame.font.Font("Team 401.ttf",32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

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

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt( (math.pow((enemyX-bulletX),2)) + 
                          (math.pow((enemyY-bulletY),2)) )
    if distance < 27:
        return True
    else:
        return False
    
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
                if bullet_state == "ready":
                  bulletX = playerX
                  fire_bullet(bulletX,bulletY)    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        

    #SCREEN UPDATING
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    #ENEMY UPDATING
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyHeight[i]
        elif enemyX[i] >= (800 - enemyWidth[i]):
            enemyX_change[i] = -3
            enemyY[i] += enemyHeight[i]
        
        #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bullet_state = "ready"
            bulletY = 480
            score_value+=1
            enemyX[i] = random.randint(0,800-enemyWidth[i])
            enemyY[i] = random.randint(50,150)
            
        enemy(enemyX[i],enemyY[i],i)

    #PLAYER UPDATING
    playerX += playerX_change
    if playerX <= 0:
       playerX = 0
    elif playerX >= (800 - playerWidth):
       playerX = (800 - playerWidth)

    #BULLET
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
        
    if bullet_state == "fire":
       fire_bullet(bulletX,bulletY)
       bulletY -= bulletY_change

    
    
    player(playerX,playerY)
    show_score(textX,textY)    

    pygame.display.update()
