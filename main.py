from utils import *
from algo import *

from random import randint
import time


class GraphModel:
    def __init__(self):
        self.k = 0
        self.vertices = 0
        self.arestas = 0
        self.graph = [[]]
        self.solucao = []
        self.cost = 0
        self.path = ""

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
        self.cost = -1;
        while self.cost == -1:
            self.generateRandomSol()
            self.cost = self.getCost()

        end = time.time()
        return "{:.5f}".format(end - start)

    def initModel(self):
        folder = input("Introduza a pasta (vazio se estiver na mesma)\n--> ")
        file = input("Introduza o nome do ficheiro\n-->")
        numOfRuns = input("Introduza o numero de iteracoes\n-->")
        self.path = folder + "/" + file
        if (self.path == "/" and numOfRuns == ""):
            self.path = "text files/test.txt"
            numOfRuns = 10
        start = time.time()
        readFile(self.path, self)
        end = time.time()
        return "{:.5f}".format(end - start)



if __name__ == "__main__":
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


