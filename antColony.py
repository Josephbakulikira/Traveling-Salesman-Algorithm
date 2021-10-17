import pygame
from ant import *
from utils import translateValue
pygame.font.init()
textColor   = (0, 0, 0)
# textFont    = pg.font.Font("freesansbold.ttf", size)
textFont    = pygame.font.SysFont("Arial", 20)

class AntColony(object):
    def __init__(self, variation="ACS", size=5, elitist_weight=1.0, minFactor=0.001, alpha=1.0, beta=3.0,
                 rho=0.1, phe_deposit_weight=1.0, pheromone=1.0, max_iterations=100, nodes=None, labels=None):
        self.variation = variation
        self.size = size
        self.elitist_weight = elitist_weight
        self.minFactor = minFactor
        self.alpha = alpha
        self.rho = rho
        self.phe_deposit_weight = phe_deposit_weight
        self.max_iterations = max_iterations
        self.n_nodes = len(nodes)
        self.nodes = nodes
        self.edges = [[None for j in range(self.n_nodes)] for i in range(self.n_nodes)]
        for x in range(self.n_nodes):
            for y in range(self.n_nodes):
                heuristic = math.sqrt(
                    math.pow(self.nodes[x].x-self.nodes[y].x, 2) +
                    math.pow(self.nodes[x].y-self.nodes[y].y, 2)
                )
                self.edges[x][y] = self.edges[y][x] = Edge(x, y, heuristic, pheromone)
        self.ants = [Ant(self.edges, alpha, beta, self.n_nodes) for i in range(self.size)]

        # global Best route
        self.best_tour = []
        self.best_distance = float("inf")

        self.local_best_route = []
        self.local_best_distance = float("inf")

    def AddPheromone(self, tour, distance, heuristic=1):
        pheromone_to_add = self.phe_deposit_weight / distance
        for i in range(self.n_nodes):
            self.edges[tour[i]][tour[(i + 1) % self.n_nodes]].pheromone += heuristic

    def ACS(self):
        # for step in range(self.max_iterations):
        for ant in self.ants:
            self.AddPheromone(ant.UpdateTour(), ant.CalculateDistance())
            if ant.distance < self.best_distance:
                self.best_tour = ant.tour
                self.best_distance = ant.distance

        for x in range(self.n_nodes):
            for y in range(x + 1, self.n_nodes):
                self.edges[x][y].pheromone *= (1 - self.rho)

    def ELITIST(self):
        """
        In elitist ACO systems, either the best current, or global best ant,
        deposits extra pheromone during it's local pheromone update procedure.
        This encourages the colony to refine it's search around solutions
        which have a track record of being high quality. If all goes well,
        this should result in better search performance.
        """
        # for step in range(self.max_iterations):
        for ant in self.ants:
            self.AddPheromone(ant.UpdateTour(), ant.CalculateDistance())
            if ant.distance < self.best_distance:
                self.best_tour = ant.tour
                self.best_distance = ant.distance
        self.AddPheromone(self.best_tour, self.best_distance, self.elitist_weight)
        for x in range(self.n_nodes):
            for y in range(self.n_nodes):
                self.edges[x][y].pheromone *= (1-self.rho)

    def MAX_MIN(self, counter):
        """
        The MaxMin algorithm is similar to the elitist ACO algorithm in that
        it gives preference to high ranking solutions.
        However, in MaxMin instead of simply giving extra weight to elite solutions,
        only the best current, or best global solution, is allowed to deposit a pheromone trail.
        """
        _best_distance = float("inf")
        _best_tour = None
        for ant in self.ants:
            ant.UpdateTour()
            if ant.CalculateDistance() < _best_distance:
                _best_tour = ant.tour
                _best_distance = ant.distance
        if (counter + 1) / self.max_iterations <= 0.75:
            self.AddPheromone(_best_tour, _best_distance)
            max_pheromone = self.phe_deposit_weight / _best_distance
        else:
            if _best_distance < self.best_distance:
                self.best_tour = _best_tour
                self.best_distance = _best_distance
            self.AddPheromone(self.best_tour, self.best_distance)
            max_pheromone = self.phe_deposit_weight / self.best_distance
        min_pheromone = max_pheromone * self.minFactor

        for x in range(self.n_nodes):
            for y in range(1+x, self.n_nodes):
                self.edges[x][y].pheromone *= (1 - self.rho)
                if self.edges[x][y].pheromone > max_pheromone:
                    self.edges[x][y].pheromone = max_pheromone
                elif self.edges[x][y].pheromone < min_pheromone:
                    self.edges[x][y].pheromone = min_pheromone
        self.local_best_route = _best_tour
        self.local_best_distance = _best_distance

    def Simulate(self, counter):
        if self.variation == "ACS":
            self.ACS()
        elif self.variation == "ELITIST":
            self.ELITIST()
        elif self.variation == "MAX-MIN":
            self.MAX_MIN(counter)

    def Draw(self, manager):
        # Draw Best Routes
        for i in range(len(self.best_tour)):
            a = self.nodes[self.best_tour[i]]
            b = self.nodes[self.best_tour[(i+1) % len(self.best_tour)]]
            pygame.draw.line(manager.screen, manager.Highlight, a.GetTuple(), b.GetTuple(), manager.LineThickness)
        # Draw Pheromones
        if self.variation == "MAX-MIN":
            for ant in self.ants:
                for edge in ant.edges:
                    for e in edge:
                        r = g = b = int(min((e.pheromone)*math.pow(10, 5), 255))
                        thickness = int(translateValue(e.pheromone, 0, 255, 1, 8))
                        pygame.draw.line(manager.screen, (r, g, 0), self.nodes[e.a].GetTuple(), self.nodes[e.b].GetTuple(), thickness)
        else:
            for ant in self.ants:
                for edge in ant.edges:
                    for e in edge:
                        r = g = b = int(min((e.pheromone)*2, 255))
                        thickness = int(translateValue(e.pheromone, 0, 255, 1, 8))
                        pygame.draw.line(manager.screen, (r, g, 0), self.nodes[e.a].GetTuple(), self.nodes[e.b].GetTuple(), thickness)


        for node in self.nodes:
            pygame.draw.circle(manager.screen, manager.White, node.GetTuple(), manager.scaler)

        for i in self.best_tour:
            textSurface = textFont.render(str(i), True, textColor)
            textRectangle = textSurface.get_rect(center=(self.nodes[self.best_tour[i]].x, self.nodes[self.best_tour[i]].y))
            manager.screen.blit(textSurface, textRectangle)
