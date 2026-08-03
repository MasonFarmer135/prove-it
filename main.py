import pygame
import sys

#Initilizing Pygame
pygame.init()

#Screen
windowWidth = 1200
windowHeight = 600

window = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Prove It")
display = 1

font1 = pygame.font.SysFont("onyx", 560, bold = False)
zoomNum = 0
windowUpdate = True

running = True
while running == True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()

        elif (event.type == pygame.VIDEORESIZE):
            windowWidth = window.get_width()
            windowHeight = window.get_height()
            windowUpdate = True

            if (windowWidth >= windowHeight):
                font1 = pygame.font.SysFont("onyx", windowWidth, bold = False)

            elif (windowHeight > windowWidth):
                font1 = pygame.font.SysFont("onyx", windowHeight, bold = False)

            if (windowWidth < 1200 and windowHeight < 600):
                windowWidth = 1200
                windowHeight = 600
                window = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

            elif (windowWidth < 1200):
                windowWidth = 1200
                window = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

            elif (windowHeight < 600):
                windowHeight = 600
                window = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

        if (display == 1):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    print ("display = 2")

    if (display == 1):
        window.fill("#374318")
        
        text1 = font1.render("Prove It", True, ("#DEEDB7"))
        text1Center = text1.get_rect(center = (windowWidth / 2, windowHeight / 2))

        font3 = pygame.font.SysFont("onyx", 280, bold = False)
        text3 = font3.render("Loading..", True, ("#DEEDB7"))
        text3Center = text3.get_rect(center = (windowWidth / 2, windowHeight / 2))

        if (windowUpdate == True):
            if (windowWidth >= windowHeight):
                font1 = pygame.font.SysFont("onyx", windowHeight - zoomNum, bold = False)
                text1Width, text1Height = pygame.surface.Surface.get_size(text1)
                if (windowWidth > text1Width and windowHeight > text1Height):
                    zoomNum = 0
                    windowUpdate = False

                else:
                    zoomNum = zoomNum + 1

            if (windowHeight > windowWidth):
                font1 = pygame.font.SysFont("onyx", windowWidth - zoomNum, bold = False)
                text1Width, text1Height = pygame.surface.Surface.get_size(text1)
                if (windowWidth > text1Width and windowHeight > text1Height):
                    zoomNum = 0
                    windowUpdate = False

                else:
                    zoomNum = zoomNum + 1

        if (windowUpdate != True):
            window.blit(text1, text1Center)

            font2 = pygame.font.SysFont("onyx", text1Width // 20, bold = False)
            text2 = font2.render('Click "Enter" to continue', True, ("#8B986A"))
            text2Center = text2.get_rect(center = (windowWidth / 2 + windowWidth / 3, windowHeight / 2 + text1Height / 2.4))
            window.blit(text2, text2Center)

        else:
            window.blit(text3, text3Center)

    pygame.display.update()