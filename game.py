import pygame

# load images 
drawbg = pygame.image.load("./sprites/bg.png")

# Init main function
def main():
    # Init PyGame module
    pygame.init()
    # Program Settings
    icon = pygame.image.load("./sprites/icon32x32.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Debt Collector")

    # Makes game run at 528x640 resolution
    screen = pygame.display.set_mode((528,640))

    # Running loop
    running = True

    while running:
        # Checks all events occuring in PyGame
        for event in pygame.event.get():
            # draw images
            screen.blit(drawbg,(0,0))
            pygame.display.flip()
            # If user quits then exit
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()
