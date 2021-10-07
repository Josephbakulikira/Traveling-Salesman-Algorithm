import pygame
from point import *
from manager import *
from random import randint

pygame.init()

manager = Manager()

q = 3

run = True
while run:
    manager.Background()
    manager.SetFps()
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

    # manager.BruteForce()
    # manager.Lexicographic()
    manager.GeneticAlgorithm()

    manager.DrawPoints()
    manager.DrawShortestPath()
    manager.Percentage()

    pygame.display.flip()

pygame.quit()
