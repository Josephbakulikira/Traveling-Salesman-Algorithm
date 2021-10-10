import pygame
from point import *
from manager import *
from random import randint

pygame.init()

manager = Manager()
manager.ChangeAntColonyVariation("ELITIST")
selectedIndex = 2

pause = True
started = False

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
            if event.key == pygame.K_SPACE:
                pause = not pause

    # Choose one method between the 3 below: bruteForce, lexicagraphic order, genetic algorithm
    started = True
    if selectedIndex == 0:
        if pause == False:
            manager.BruteForce()
        manager.DrawPoints()
        manager.DrawShortestPath()
        manager.Percentage(manager.PossibleCombinations)
    elif selectedIndex == 1:
        if pause == False:
            manager.Lexicographic()
        manager.DrawPoints()
        manager.DrawShortestPath()
        manager.Percentage(manager.PossibleCombinations)
    elif selectedIndex == 2:
        if pause == False:
            manager.GeneticAlgorithm()
        manager.DrawPoints()
        manager.DrawShortestPath()
    elif selectedIndex == 3:
        manager.AntColonyOptimization(pause)
        manager.Percentage(iterations)


    manager.ShowText(selectedIndex)

    # point scale animation increment
    manager.scaler += 1
    if manager.scaler > manager.max_radius:
        manager.scaler = manager.max_radius

    pygame.display.flip()

pygame.quit()
