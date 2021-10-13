import pygame
from point import *
from manager import *
from random import randint
from UI.setup import *
from utils import SumDistance

pygame.init()

manager = Manager()
antColonyTypes = ["ACS", "ELITIST", "MAX-MIN"]
# manager.ChangeAntColonyVariation("ELITIST")

selectedIndex = 2

pause = True
started = False
rightMouseClicked = False
GenerateToggle = False
reset = False

PauseButton.state = pause
ResetButton.state = reset
RandomButton.state = GenerateToggle

showUI = False
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
                started = True
            if event.key == pygame.K_RETURN:
                showUI = not showUI

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rightMouseClicked = True


    # Choose one method between the 3 below: bruteForce, lexicagraphic order, genetic algorithm
    if selectedIndex == 0:
        if pause == False:
            manager.BruteForce()
        manager.DrawPoints()
        manager.DrawShortestPath()
        # manager.Percentage(manager.PossibleCombinations)
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
    else:
        manager.AntColonyOptimization(pause)
        # print(selectedIndex-3)
        manager.ChangeAntColonyVariation(antColonyTypes[selectedIndex-3])
        manager.Percentage(iterations)

    manager.ShowText(selectedIndex, started)

    # UI
    if showUI:
        panel.Render(manager.screen)
        AlgorithmChoice.Render(manager.screen, rightMouseClicked)
        if pause != PauseButton.state:
            PauseButton.state = pause

        PauseButton.Render(manager.screen, rightMouseClicked)
        ResetButton.Render(manager.screen, rightMouseClicked)
        RandomButton.Render(manager.screen, rightMouseClicked)

        pause = PauseButton.state
        reset = ResetButton.state

        if reset == True:
            reset = False
            ResetButton.state = False
            temp = manager.Points.copy()
            manager = Manager(temp)
            manager.OptimalRoutes = manager.Points.copy()
            manager.recordDistance = SumDistance(manager.Points)
            manager.ResetAntColony(manager.antColony.variation)
            manager.ResetGenetic()

        GenerateToggle = RandomButton.state
        if GenerateToggle == True:
            manager.RandomPoints()
            GenerateToggle = False
            RandomButton.state = False

        if pause == True:
            PauseButton.text = "Continue"
        else:
            PauseButton.text = "Pause"

        if rightMouseClicked:
            selectedIndex = AlgorithmChoice.currentIndex


    # point scale animation increment
    manager.scaler += 1
    if manager.scaler > manager.max_radius:
        manager.scaler = manager.max_radius

    pygame.display.flip()
    rightMouseClicked = False
pygame.quit()
