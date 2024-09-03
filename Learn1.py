import pygame

pygame.init() #Used to initialize the pygame module

screen = pygame.display.set_mode((800, 600)) #Sets up the screen

running = True #A boolean variable to control the game loop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
