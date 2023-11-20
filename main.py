from utils import *
from algo import *

from random import randint


class GraphModel:
    def __init__(self, k=0, vertices=0, arestas=0, graph=[], solucao=[], cost=0):
        self.k = k
        self.vertices = vertices
        self.arestas = arestas
        self.graph = graph
        self.solucao = solucao
        self.cost = cost

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
            currentCost = 0
            if (self.solucao[i] != 0):
                for j in range(self.vertices):
                    if (self.solucao[j] != 0):
                        currentCost += self.graph[i][j]
                if (currentCost == 0):
                    return -1
                cost += currentCost
        return int(cost / 2)

    def createInitialSolution(self):
        self.cost = -1;
        while self.cost == -1:
            self.generateRandomSol()
            self.cost = self.getCost()


if __name__ == "__main__":
    folder = input("Introduza a pasta (vazio se estiver na mesma)\n--> ")
    file = input("Introduza o nome do ficheiro\n-->")
    numOfRuns = input("Introduza o numero de iteracoes\n-->")
    path = folder + "/" + file
    model = GraphModel()
    if(path == "/" and numOfRuns == ""):
        path = "text files/test.txt"
        numOfRuns = 10
    readFile(path, model)
    model.printGraph()
    print(model.k)
    print(model.vertices)
    print(model.arestas)
    model.createInitialSolution()
    print("Initial Solution:", model.solucao)
    print("Inital Cost:", model.cost)
