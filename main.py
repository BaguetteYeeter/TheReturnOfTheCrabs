import pygame
import sys
import getopt
import random
import math
import time

pack = "default"
score = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:s:", ["pack=", "score="])
except getopt.GetoptError:
    print("main.py -p [texture pack] -s [score]")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print("main.py -p [texture pack] -s [score]")
        sys.exit()
    elif opt in ("-p", "--pack"):
        pack = arg
    elif opt in ("-s", "--score"):
        score = int(arg)

pygame.init()
mainScreen = pygame.display.set_mode((640, 480))
pygame.font.init()
scoreFont = pygame.font.SysFont('Comic Sans MS', 90)

pygame.display.set_caption("The Return Of The Crabs")

minigameMenu = False
menu = True
rave = False
arrowIsActive = 0
hotel = "Trivago"
cutscene = 0

class graphics:
    print("Loading textures")
    title = pygame.image.load("textures/" + pack + "/menu/menu/title.png")
    gameMenu = pygame.image.load("textures/" + pack + "/menu/minigamemenu/menu.png")
    class rave:
        back = pygame.image.load("textures/" + pack + "/rave/back.png")
        crab = pygame.image.load("textures/" + pack + "/rave/crab.png")
        upArrow = pygame.image.load("textures/" + pack + "/rave/up.png")
        downArrow = pygame.image.load("textures/" + pack + "/rave/down.png")
        leftArrow = pygame.image.load("textures/" + pack + "/rave/left.png")
        rightArrow = pygame.image.load("textures/" + pack + "/rave/right.png")
        cutscene1 = pygame.image.load("textures/" + pack + "/rave/cutscenes/cut1.png")
        cutscene2 = pygame.image.load("textures/" + pack + "/rave/cutscenes/cut2.png")
        cutscene3 = pygame.image.load("textures/" + pack + "/rave/cutscenes/cut3.png")
        cutscene4 = pygame.image.load("textures/" + pack + "/rave/cutscenes/cut4.png")
        cutscene5 = pygame.image.load("textures/" + pack + "/rave/cutscenes/cut5.png")
        cutscene6 = pygame.image.load("textures/" + pack + "/rave/cutscenes/cut6.png")
    print("Done")

run = True
while run:
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mainScreen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if menu:
        mainScreen.blit(graphics.title, (0, 0))
        if keys[pygame.K_SPACE]:
            menu = False
            minigameMenu = True
    if minigameMenu:
        mainScreen.blit(graphics.gameMenu, (0, 0))
        if keys[pygame.K_r]:
            minigameMenu = False
            rave = True
        if keys[pygame.K_l]:
            print("game not done")
            run = False
        if keys[pygame.K_b]:
            print("game not done")
            run = False
    if rave:
        mainScreen.blit(graphics.rave.back, (0, 0))

        if arrowIsActive == 0:
            arrowDirection = random.randint(1,4)
            if arrowDirection == 1:
                arrowDirection = "up"
                arrowIsActive = 1
            elif arrowDirection == 2:
                arrowDirection = "down"
                arrowIsActive = 1
            elif arrowDirection == 3:
                arrowDirection = "left"
                arrowIsActive = 1
            elif arrowDirection == 4:
                arrowDirection = "right"
                arrowIsActive = 1
        if arrowDirection == "up":
            mainScreen.blit(graphics.rave.upArrow, (50, 320))

        elif arrowDirection == "down":
            mainScreen.blit(graphics.rave.downArrow, (50, 420))

        elif arrowDirection == "left":
            mainScreen.blit(graphics.rave.leftArrow, (0, 370))

        elif arrowDirection == "right":
            mainScreen.blit(graphics.rave.rightArrow, (100, 370))

        else:
            mainScreen.blit(graphics.rave.crab, (400, 255))

        if keys[pygame.K_UP]:
            if arrowDirection == "up":
                arrowIsActive = 0
                score += 1
                mainScreen.blit(graphics.rave.crab, (400, 185))
            else:
                arrowIsActive = 1
                score -= 1
                mainScreen.blit(graphics.rave.crab, (400, 185))
        elif keys[pygame.K_DOWN]:
            if arrowDirection == "down":
                arrowIsActive = 0
                score += 1
                mainScreen.blit(graphics.rave.crab, (400, 325))
            else:
                arrowIsActive = 1
                score -= 1
                mainScreen.blit(graphics.rave.crab, (400, 325))
        elif keys[pygame.K_LEFT]:
            if arrowDirection == "left":
                arrowIsActive = 0
                score += 1
                mainScreen.blit(graphics.rave.crab, (300, 255))
            else:
                arrowIsActive = 1
                score -= 1
                mainScreen.blit(graphics.rave.crab, (300, 255))
        elif keys[pygame.K_RIGHT]:
            if arrowDirection == "right":
                arrowIsActive = 0
                score += 1
                mainScreen.blit(graphics.rave.crab, (500, 255))
            else:
                arrowIsActive = 1
                score -= 1
                mainScreen.blit(graphics.rave.crab, (500, 255))
        else:
            mainScreen.blit(graphics.rave.crab, (400, 255))

        finalFont = scoreFont.render("SCORE: " + str(score), False, (0, 0, 0))
        mainScreen.blit(finalFont, (0, 0))
        if cutscene == 2:
            mainScreen.blit(graphics.rave.cutscene2, (0, 0))

            if keys[pygame.K_RETURN]:
                pygame.time.delay(10)
                cutscene = 3
        elif cutscene == 3:
            mainScreen.blit(graphics.rave.cutscene3, (0, 0))

            if keys[pygame.K_RETURN]:
                pygame.time.delay(10)
                cutscene = 4
        elif cutscene == 4:
            mainScreen.blit(graphics.rave.cutscene4, (0, 0))

            if keys[pygame.K_RETURN]:
                pygame.time.delay(10)
                cutscene = 5
        elif cutscene == 5:
            mainScreen.blit(graphics.rave.cutscene5, (0, 0))

            if keys[pygame.K_RETURN]:
                pygame.time.delay(10)
                cutscene = 6
        elif cutscene == 6:
            mainScreen.blit(graphics.rave.cutscene6, (0, 0))

            if keys[pygame.K_RETURN]:
                pygame.time.delay(10)
                rave = False
                menu = True
            if keys[pygame.K_r]:
                score = 0
                cutscene = 0
        elif score == 100:
            mainScreen.blit(graphics.rave.cutscene1, (0, 0))

            cutscene = 1
            if keys[pygame.K_RETURN]:
                pygame.time.delay(10)
                cutscene = 2

        if score == 500:
            mainScreen.blit(graphics.rave.cutscene6, (0, 0))
            if keys[pygame.K_RETURN]:
                rave = False
                menu = True
            if keys[pygame.K_r]:
                score = 0

    pygame.display.update()
