import pygame
import time
import random


lasersX = []
lasersY = []

dificulty = 100

enemyX = []
enemyY = []


PlayerVite = 10

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


windowWidth, windowHeight = screen.get_size()

pygame.display.set_caption("Game")

PlayerWidth = 20
PlayerHeight = 20

laserWidth = 10
laserHeight = 10

enemyHeight = 20
enemyWidth = 20

PlayerX = windowWidth / 2

PlayerY = windowHeight -100

FPM = 10



timeOnGameOver = 2000

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

scor = 0


font = pygame.font.Font('freesansbold.ttf', 32)



run = True
def draw():
        pygame.draw.rect(screen, (255, 255, 255), (PlayerX, PlayerY, PlayerWidth, PlayerHeight)) 

        for i in range(len(lasersY)):
                pygame.draw.rect(screen, (255, 0, 0), (lasersX[i], lasersY[i], laserWidth, laserHeight)) 

        for i in range(len(enemyY)):
                pygame.draw.rect(screen, (0, 255, 0), (enemyX[i]- enemyWidth//5, enemyY[i], enemyWidth, enemyHeight)) 


def reset():
        global scor
        lasersX.clear()
        lasersY.clear()
        enemyX.clear()
        enemyY.clear()
        PlayerX = windowWidth / 2

        PlayerY = windowHeight -100
        scor = 0
        dificulty = 100
 

        text = font.render('', True, green, blue)
        screen.blit(text, (windowHeight // 2, windowWidth // 2))
        pygame.display.update()





def onGameOver():
        text = font.render('Game Over', True, green, blue)
        screen.blit(text, (windowHeight // 2, windowWidth // 2))
        pygame.display.update()
   
        
        pygame.time.delay(timeOnGameOver)            
                
        
        reset()
   





def isGameOver():
        for i in range(len(enemyX)):
                
             
                if abs(PlayerY - enemyY[i]) < enemyHeight:

                        if abs(PlayerX - enemyX[i]) < enemyWidth:
                                

                

                                onGameOver()
                                break



def fire():
        lasersX.append(PlayerX + PlayerWidth//3)
    
        lasersY.append(PlayerY - PlayerHeight)


def creatEnemy():
        enemyX.append(random.randint(0, windowWidth - enemyWidth))
        enemyY.append(0)
        


def isEnemyDead():
        global scor
        global dificulty
        EnemyToDelete = []
        LaserToDelete = []

        for i in range(len(lasersX)):
                for ii in range(len(enemyX)):
                        if lasersY[i] - enemyY[ii] < enemyHeight:

                                if abs(lasersX[i] - enemyX[ii]) < enemyWidth:
                                

                
                                        EnemyToDelete.append(ii)        
                                        LaserToDelete.append(i)
                                        scor = scor + 2
                                        if dificulty > 2:
                                                dificulty -= 1
                   
                                   
        for i in EnemyToDelete:
                del enemyX[i]
                del enemyY[i]

        for i in LaserToDelete:
                del lasersX[i]
                del lasersY[i]



chrono = 0

while run:


        scorText = font.render(str(scor), True, green, blue)
        screen.blit(scorText, (10, 10))
        pygame.display.update()


        pygame.time.delay(FPM) 
        for event in pygame.event.get():
        
                
                if event.type == pygame.QUIT:

                        run = False
        
        

        keys = pygame.key.get_pressed()



        if keys[pygame.K_ESCAPE]:

                run = False


        if keys[pygame.K_RIGHT] and PlayerX < (windowWidth - PlayerWidth):

                PlayerX += PlayerVite
        
        if keys[pygame.K_LEFT] and PlayerX > 0:

                PlayerX -= PlayerVite


        if keys[pygame.K_SPACE]:
        
                if time.time() - chrono > 0.5:
                        
                        fire()
                        chrono = time.time()



        LaserToDelete = []

        for i in range(len(lasersY)):
                if lasersY[i] < 0:
                        LaserToDelete.append(i)
                else:
                        lasersY[i] -= 5


        for i in LaserToDelete:
                del lasersX[i]
                del lasersY[i]


        EnemyToDelete = []

        for i in range(len(enemyY)):
                if enemyY[i] > windowHeight  :
                        EnemyToDelete.append(i)
                        scor = scor - 1
                        dificulty+=1
                else:
                        enemyY[i] += 2
                
        for i in EnemyToDelete:
                del enemyX[i]
                del enemyY[i]


        if random.randint(0, dificulty) == 1:
                creatEnemy()

        #print(lasersY  )

        isGameOver()

        isEnemyDead()

        screen.fill((0,0,0))
        


        draw()

        pygame.display.update()


pygame.quit()


quit()