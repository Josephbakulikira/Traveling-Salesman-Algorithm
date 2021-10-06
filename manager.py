import pygame
from random import randint
from point import Point
from utils import *

offset          = 50
width, height   = 800, 800
pygame.font.init()
class Manager(object):
    size            = (width, height)
    fps             = 60
    screen          = pygame.display.set_mode(size)
    clock           = pygame.time.Clock()

    Black           = (0, 0, 0)
    White           = (255, 255, 255)
    Yellow          = (255, 255, 0)
    Highlight           = (80, 170, 120)
    LineThickness   = 2

    showIndex       = True
    n_points        = 5

    PossibleCombinations = Factorial(n_points)
    print("possible combinations : {}".format(Factorial(n_points)))
    Points          = [Point(randint(offset, width-offset), randint(offset, height-offset)) for i in range(n_points)]
    Order           = [i for i in range(n_points)]
    counter         = 0
    def __init__(self):
        self.recordDistance  = SumDistance(self.Points)
        self.OptimalRoutes          = []

    def SetFps(self):
        self.clock.tick(self.fps)

    def UpdateCaption(self):
        frameRate = int(self.clock.get_fps())
        pygame.display.set_caption("Traveling SalesPerson - Fps : {}".format(frameRate))


    def BruteForce(self):
        i1 = randint(0, self.n_points-1)
        i2 = randint(0, self.n_points-1)
        self.Points[i1], self.Points[i2] = self.Points[i2], self.Points[i1]

        dist = SumDistance(self.Points)
        if dist < self.recordDistance:
            self.recordDistance  = dist
            self.OptimalRoutes   = self.Points.copy()
            print("Shortest distance : {}" .format(self.recordDistance))

    def Lexicographic(self):
        self.Order = LexicalOrder(self.Order)
        nodes = []
        for i in self.Order:
            nodes.append(self.Points[i])

        self.counter += 1

        if self.counter > self.PossibleCombinations:
            self.counter = self.PossibleCombinations

        dist = SumDistance(nodes)
        if dist < self.recordDistance:
            self.recordDistance = dist
            self.OptimalRoutes  = nodes.copy()
            print("Shortest distance : {}" .format(self.recordDistance))

    def Percentage(self):
        percent = (self.counter/self.PossibleCombinations) * 100
        textColor   = (255, 255, 255)
        # textFont    = pg.font.Font("freesansbold.ttf", size)
        textFont    = pygame.font.SysFont("Arial", 20)
        textSurface = textFont.render(str(round(percent, 4)), False, textColor)
        self.screen.blit(textSurface, (width//2, 50))
    def DrawShortestPath(self):
        if len(self.OptimalRoutes) > 0:
            for n in range(self.n_points):
                if n+1 < self.n_points:
                    pygame.draw.line(self.screen, self.Highlight,
                                    (self.OptimalRoutes[n].x, self.OptimalRoutes[n].y),
                                    (self.OptimalRoutes[n+1].x, self.OptimalRoutes[n+1].y),
                                    self.LineThickness)
                self.OptimalRoutes[n].Draw(self, self.showIndex, True, n)
    def DrawPoints(self):
        for point in self.Points:
            point.Draw(self)

    def DrawLines(self):
        for i, point in enumerate(self.Points):
            if i+1 < self.n_points:
                    pygame.draw.line(self.screen, self.White, (point.x, point.y), (self.Points[i+1].x, self.Points[i+1].y), self.LineThickness)

    def Background(self):
        self.screen.fill(self.Black)
