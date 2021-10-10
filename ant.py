import pygame
import math
import random

class Edge:
    def __init__(self, a, b, heuristic, pheromone):
        self.a = a
        self.b = b
        self.heuristic = heuristic
        self.pheromone = pheromone

class Ant:
    def __init__(self, edges, alpha, beta, n_nodes):
        """
        alpha -> parameter used to control the importance of the pheromone trail
        beta  -> parameter used to control the heuristic information during selection
        """
        self.edges = edges
        self.tour = None
        self.alpha = alpha
        self.beta = beta
        self.n_nodes = n_nodes
        self.distance = 0.0

    def NodeSelection(self):
        """
        Constructing solution
        an ant will often follow the strongest
        pheromone trail when constructing a solution.

        state -> is a point on a graph or a City

        Here, an ant would be selecting the next city depending on the distance
        to the next city, and the amount of pheromone on the path between
        the two cities.
        """
        roulette_wheel = 0
        states = [node for node in range(self.n_nodes) if node not in self.tour]
        heuristic_value = 0
        for new_state in states:
            heuristic_value += self.edges[self.tour[-1]][new_state].heuristic
        for new_state in states:
            A = math.pow(self.edges[self.tour[-1]][new_state].pheromone, self.alpha)
            B = math.pow((heuristic_value/self.edges[self.tour[-1]][new_state].heuristic), self.beta)
            roulette_wheel += A * B
        random_value = random.uniform(0, roulette_wheel)
        wheel_position = 0
        for new_state in states:
            A = math.pow(self.edges[self.tour[-1]][new_state].pheromone, self.alpha)
            B = math.pow((heuristic_value/self.edges[self.tour[-1]][new_state].heuristic), self.beta)
            wheel_position += A * B
            if wheel_position >= random_value:
                return new_state

    def UpdateTour(self):
        self.tour = [random.randint(0, self.n_nodes - 1)]
        while len(self.tour) < self.n_nodes:
            self.tour.append(self.NodeSelection())
        return self.tour

    def CalculateDistance(self):
        self.distance = 0
        for i in range(self.n_nodes):
            self.distance += self.edges[self.tour[i]][self.tour[(i+1)%self.n_nodes]].heuristic
        return self.distance
