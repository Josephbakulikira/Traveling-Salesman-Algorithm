import pygame
from point import *
from manager import *
from random import randint

pygame.init()

manager = Manager()
manager.ChangeAntColonyVariation("ELITIST")
selectedIndex = 3

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

    if selectedIndex == 0:
        manager.BruteForce()
        manager.DrawPoints()
        manager.DrawShortestPath()
        manager.Percentage(manager.PossibleCombinations)
    elif selectedIndex == 1:
        manager.Lexicographic()
        manager.DrawPoints()
        manager.DrawShortestPath()
        manager.Percentage(manager.PossibleCombinations)
    elif selectedIndex == 2:
        manager.GeneticAlgorithm()
        manager.DrawPoints()
        manager.DrawShortestPath()
    elif selectedIndex == 3:
        manager.AntColonyOptimization()
        manager.Percentage(iterations)

    manager.ShowTextDistance()

    # point scale animation increment
    manager.scaler += 1
    if manager.scaler > manager.max_radius:
        manager.scaler = manager.max_radius

    pygame.display.flip()

pygame.quit()
