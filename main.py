import pygame
import sys
import getopt

pack = "default"

try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:", ["pack="])
except getopt.GetoptError:
    print("main.py -p [texture pack]")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-h":
        print("main.py -p [texture pack]")
        sys.exit()
    elif opt in ("-p", "--pack"):
        pack = arg

pygame.init()
mainScreen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("The Return Of The Crabs")

minigameMenu = False
menu = True

class graphics:
    print("Loading textures")
    title = pygame.image.load("textures/" + pack + "/menu/menu/title.png")
    gameMenu = pygame.image.load("textures/" + pack + "/menu/minigamemenu/menu.png")
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
            print("game not done")
            run = False
        if keys[pygame.K_l]:
            print("game not done")
            run = False
        if keys[pygame.K_b]:
            print("game not done")
            run = False

    pygame.display.update()
