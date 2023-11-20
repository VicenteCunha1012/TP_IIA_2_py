from utils import *
from algo import *

from random import randint
class GraphModel:
    def __init__(self, k=0, vertices=0, arestas=0, graph=[],solucao=[], cost=0):
        self.k = k
        self.vertices = vertices
        self.arestas = arestas
        self.graph = graph
        self.solucao = solucao
        self.cost = cost
    def fillGraph(self):
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]

    def fillSolucao(self):
        self.solucao = [0 for _ in range(self.vertices)]

    def printGraph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.graph[i][j],end=" ")

            print()

    def generateRandomSol(self):
        changedCount = 0;
        while changedCount < self.k:
            random_index = randint(0,self.vertices-1)
            if self.solucao[random_index]== 0:
                self.solucao[random_index] = 1
                changedCount+=1

    def getCost(self):

        for i in range(self.vertices):
            currentCost = 0
            if(self.solucao[i] != 0):
                for j in range(self.vertices):
                    if(self.solucao[j] != 0):
                        currentCost += self.graph[i][j]
                if(currentCost == 0):
                    self.cost = -1
                    return
                self.cost += currentCost

    def createInitialSolution(self):
        self.cost = -1;
        while self.cost == -1:
            self.generateRandomSol()
            self.getCost()






if __name__ == "__main__":
    model = GraphModel()
    readFile("test.txt",model)
    model.printGraph()
    model.fillSolucao()
    print(model.k)
    print(model.vertices)
    print(model.arestas)
    model.createInitialSolution()
    print(model.solucao)