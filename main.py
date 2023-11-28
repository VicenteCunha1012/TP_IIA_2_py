from utils import *
from algo import *

from random import randint
import time
import matplotlib.pyplot as plt
import networkx as nx
#matplotlib.use('TkAgg')  # Use 'TkAgg' or another backend that works on your system






class GraphModel:
    def __init__(self):
        self.k = self.vertices = self.arestas = self.cost = self.bestCost =self.numOfRuns= 0
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
        self.cost = -1;
        while self.cost == -1:
            self.generateRandomSol()
            self.cost = self.getCost()

        end = time.time()
        self.bestSolution = list(self.solucao)
        self.bestCost = self.cost
        return "{:.5f}".format(end - start)

    def initModel(self):
        folder = input("Introduza a pasta (vazio se estiver na mesma)\n--> ")
        file = input("Introduza o nome do ficheiro\n-->")
        self.numOfRuns = input("Introduza o numero de iteracoes\n-->")
        self.path = folder + "/" + file
        if (self.path == "/" and self.numOfRuns == ""):
            self.path = "text files/test.txt"
            self.numOfRuns = 10
        else:
            self.numOfRuns = int(self.numOfRuns)
        start = time.time()
        readFile(self.path, self)
        end = time.time()
        return "{:.5f}".format(end - start)

    def create_neighbour(self):



        tempValue = -1 #para entrar no loop
        index1 = index2 = 0
        while(tempValue!=0):
            index1 = randint(0, self.vertices - 1)
            tempValue = self.solucao[index1]


        tempValue = 0
        while(tempValue!=1):
            index2 = randint(0,self.vertices-1)
            tempValue = self.solucao[index2]

        self.solucao[index1] = 1
        self.solucao[index2] = 0

    def create_admissible_neighbour(self):
        tempCost = -1
        while(tempCost==-1):
            self.create_neighbour()
            tempCost = self.getCost()

    def hill_climbing(self):
        for i in range(self.numOfRuns):
            self.create_admissible_neighbour()
            self.cost = self.getCost()
            if self.cost <= self.bestCost:
                self.bestSolution = list(self.solucao)
                self.bestCost = self.cost
            if(i%1==0):
                print("Iteracao " + str(i))

                print("best cost "+ str(self.bestCost))

    def read_graph_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.k = int(lines[0].split()[1])
            num_vertices, num_edges = map(int, lines[1].split()[2:])

            # Initialize the graph with empty adjacency lists
            self.graph = [[] for _ in range(num_vertices + 1)]

            # Read edge information and add edges to the graph
            for line in lines[2:]:
                if line.startswith('e'):
                    _, u, v, weight = line.split()
                    u, v, weight = map(int, [u, v, weight])
                    self.graph[u].append((v, weight))
                    self.graph[v].append((u, weight))  # Assuming an undirected graph

    '''def visualize_graph(self):
        G = nx.Graph()
        for u in range(1, len(self.graph)):
            for v, weight in self.graph[u]:
                G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)  # You can use other layout algorithms
        labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, node_color='skyblue',
                font_color='black', font_size=8)
        plt.show()'''

    def visualize_graph(self):
        G = nx.Graph()
        for u in range(1, len(self.graph)):
            for v, weight in self.graph[u]:
                G.add_edge(u, v, weight=weight)

        pos = nx.spring_layout(G)

        labels = {node: f"{node}\n" for node in G.nodes}  # Change this line

        nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, node_color='skyblue',
                font_color='black', font_size=8)
        plt.pause(0.001)  # Use plt.pause to display the plot
        plt.show()



if __name__ == "__main__":
    bestEver = 0
    bestSolution = []
    nbf = 0.0

    model = GraphModel()
    timeInit = model.initModel()
    model.printGraph()
    graph_model = GraphModel()
    graph_model.read_graph_from_file('text files/test.txt')
    graph_model.visualize_graph()
    '''
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
    nruns = 30

    for i in range(nruns):

        model.hill_climbing()
        if i==0:
            bestEver = model.bestCost
            bestSolution = model.bestSolution
        elif model.bestCost < bestEver:
            bestEver = model.bestCost
            bestSolution = model.bestSolution
        nbf += model.bestCost

    print("Best cost" + str(model.bestCost))
    print("Best solution" + str(model.bestSolution))



'''

