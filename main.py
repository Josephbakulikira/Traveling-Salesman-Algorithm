import pygame
from point import *
from manager import *
from random import randint

pygame.init()

manager = Manager()


run = True
while run:
    manager.Background()
    delta_time = manager.SetFps()
    manager.UpdateCaption()

    # handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_t:
                manager.showIndex = not manager.showIndex

    # Choose one method between the 3 below: bruteForce, lexicagraphic order, genetic algorithm
    
    # manager.BruteForce()
    # manager.Lexicographic()
    manager.GeneticAlgorithm()

    manager.DrawPoints()
    manager.DrawShortestPath()
    manager.Percentage()

    pygame.display.flip()

pygame.quit()
