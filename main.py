import pygame as pygame

class application:
    running = True
    iconPosition = [0, 0]
    iconVelocityY = 5
    iconVelocityX = 5
    iconVelocities = ['+', '+']
    screen = None
    screensaverIconPath = './dvd-logo.png'
    clock = pygame.time.Clock()
    screenSize = None

pygame.display.init()
pygame.mouse.set_visible(False)

application.screenSize = (pygame.display.Info().current_w, pygame.display.Info().current_h)

application.screen = pygame.display.set_mode(application.screenSize, pygame.FULLSCREEN)

while (application.running):
    application.screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                application.running = False
    iconPicture = pygame.image.load(application.screensaverIconPath)
    iconPicture = pygame.transform.scale(iconPicture, (int(200 * (iconPicture.get_size()[0] / iconPicture.get_size()[1])), int(200)))
    iconWidth, iconHeight = iconPicture.get_size()
    iconX, iconY = application.iconPosition
    screenWidth, screenHeight = application.screen.get_size()
    if (iconHeight + iconY > screenHeight):
        application.iconVelocities[1] = '-'
    elif (iconY < 0):
        application.iconVelocities[1] = '+'
    if (iconWidth + iconX > screenWidth):
        application.iconVelocities[0] = '-'
    elif (iconX < 0):
        application.iconVelocities[0] = '+'
    exec('application.iconPosition = [int(application.iconPosition[0]{}application.iconVelocityX), int(application.iconPosition[1]{}application.iconVelocityY)]'.format(*application.iconVelocities))
    application.screen.blit(iconPicture, (application.iconPosition[0], application.iconPosition[1]))
    pygame.display.update()
    application.clock.tick(40)

pygame.quit()
exit()