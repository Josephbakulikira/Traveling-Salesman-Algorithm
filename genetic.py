from utils import *
from random import randint

class Genetic:
    def __init__(self, population=[], populationSize=0):
        self.population = population
        self.size = populationSize
        self.fitness = [0 for i in range(populationSize)]
        self.record = float("inf")
        self.currentDist = float("inf")
        self.current = None
        self.fitest = []
        self.fitestIndex = 0
        self.mutation_rate = 0.01

    def CalculateFitness(self, points):
        for i in range(self.size):
            nodes = []
            for j in self.population[i]:
                nodes.append(points[j])
            #print(nodes)
            dist = SumDistance(nodes)
            if dist < self.currentDist:
                self.current = self.population[i]

            if dist < self.record :
                self.record = dist
                self.fitest = self.population[i]
                self.fitestIndex = i
                #print(f"Shortest distance: {dist}")
            self.fitness[i] = 1/ (dist+1)
        self.NormalizeFitnesss()

    def NormalizeFitnesss(self):
        s = 0
        for i in range(self.size):
            s += self.fitness[i]
        for i in range(self.size):
            self.fitness[i] = self.fitness[i]/s

    def Mutate(self, genes):
        for i in range(len(self.population[0])):
            if (randint(0, 100)/100) < self.mutation_rate:
                a = randint(0, len(genes)-1)
                b = randint(0, len(genes)-1)
                genes[a], genes[b] = genes[b], genes[a]

    def CrossOver(self, genes1, genes2):
        start = randint(0, len(genes1)-1)
        end   = randint(start-1, len(genes2)-1)
        try:
            end = randint(start+1, len(genes2)-1)
        except:
            pass
        new_genes = genes1[start:end]
        for i in range(len(genes2)):
            p = genes2[i]
            if p not in new_genes:
                new_genes.append(p)
        return new_genes

    def NaturalSelection(self):
        nextPopulation = []
        for i in range(self.size):
            generation1 = PickSelection(self.population, self.fitness)
            generation2 = PickSelection(self.population, self.fitness)
            genes = self.CrossOver(generation1, generation2)
            self.Mutate(genes)
            nextPopulation.append(genes)
        self.population = nextPopulation
