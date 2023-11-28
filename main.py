from utils import *
from algo import *

from random import randint
import time


class GraphModel:
    def __init__(self):
        self.k = self.vertices = self.arestas = self.cost = self.bestCost = self.numOfRuns = 0
        self.graph = [[]]
        self.solucao = []
        self.path = ""
        self.bestSolution = []
        self.tempSolution = []

    def fillGraph(self):
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]

    def printGraph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.graph[i][j], end=" ")

            print()

    def generateRandomSol(self):
        changedCount = 0
        self.cleanSol()
        while changedCount < self.k:
            random_index = randint(0, self.vertices - 1)
            if self.solucao[random_index] == 0:
                self.solucao[random_index] = 1
                changedCount += 1

    def cleanSol(self):
        self.solucao = [0 for _ in range(self.vertices)]

    def getCost(self):
        cost = 0
        for i in range(self.vertices):
            if self.solucao[i] != 0:
                currentCost = sum(self.graph[i][j] for j in range(self.vertices) if self.solucao[j] != 0)
                if currentCost == 0:
                    return -1
                cost += currentCost

        return cost // 2

    def createInitialSolution(self):

        start = time.time()
        self.cost = -1
        while self.cost == -1:
            self.generateRandomSol()
            self.cost = self.getCost()

        end = time.time()
        self.bestSolution = list(self.solucao)
        self.bestCost = self.cost
        return "{:.5f}".format(end - start)

    def initModel(self):

        file = input("Introduza o nome do ficheiro\n-->")
        self.numOfRuns = int(input("Introduza o numero de iteracoes\n-->"))
        self.path = "text files/" + file
        start = time.time()
        readFile(self.path, self)
        end = time.time()
        return "{:.5f}".format(end - start)

    def create_neighbour(self):

        tempValue = -1  # para entrar no loop
        index1 = index2 = 0
        while (tempValue != 0):
            index1 = randint(0, self.vertices - 1)
            tempValue = self.solucao[index1]

        tempValue = 0
        while (tempValue != 1):
            index2 = randint(0, self.vertices - 1)
            tempValue = self.solucao[index2]

        self.solucao[index1] = 1
        self.solucao[index2] = 0

    def create_neighbour2(self):
        self.create_neighbour()
        tempSol = list(self.solucao)
        while tempSol == self.solucao:
            self.create_neighbour()

    def create_admissible_neighbour(self):
        tempCost = -1
        while tempCost == -1:
            self.create_neighbour2()
            tempCost = self.getCost()

    def hill_climbing(self):
        for i in range(self.numOfRuns):
            self.create_admissible_neighbour()
            self.cost = self.getCost()
            if self.cost <= self.bestCost:
                self.bestSolution = list(self.solucao)
                self.bestCost = self.cost


if __name__ == "__main__":
    print("Testes aqui")
    nRuns = 30
    bestEver = 0
    bestSol = []
    mbf = 0.0
    model = GraphModel()
    timeInit = model.initModel()
    model.printGraph()
    print(f"Path: {model.path:>45}")
    print(f"K: {model.k:>48}")
    print(f"Vertex Number: {model.vertices:>36}")
    print(f"Edge Number: {model.arestas:>38}")
    timeCreateSol = model.createInitialSolution()
    print(f"Inital Cost: {model.cost:>38}")
    print(f"Initialization Time: {timeInit:>21} seconds.")
    print(f"Initial Solution Creation Time: {timeCreateSol:>10} seconds.")
    totalTime = float(timeInit) + float(timeCreateSol)
    print(f"Time Elapsed: {str(totalTime):>28} seconds.")
    print(f"Initial Solution: {str(model.solucao):>33}")
    model.create_admissible_neighbour()
    print("Solucao admissivel" + str(model.solucao))

    for i in range(nRuns):
        print("Run " + str(i) + ": ", end="")
        model.hill_climbing()
        if i == 0:
            bestEver = model.bestCost
            bestSol = list(model.bestSolution)
        elif model.bestCost < bestEver:
            bestEver = model.bestCost
            bestSol = (model.bestSolution)
        mbf += model.bestCost
        print(model.bestSolution)
        print("Best Cost: " + str(model.bestCost))

    mbf /= nRuns
    print("MBF: " + str(mbf))
    print("Best Ever: " + str(bestEver))
    print("Best solution: " + str(bestSol))
    print("xau")
