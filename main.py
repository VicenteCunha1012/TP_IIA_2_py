from utils import *

class fileData:
    def __init__(self, k=0, vertices=0, arestas=0, graph=[]):
        self.k = k
        self.vertices = vertices
        self.arestas = arestas
        self.graph = graph

    def fillGraph(self):
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]

    def printGraph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.graph[i][j],end=" ")

            print()


if __name__ == "__main__":
    data = fileData()
    readFile("test.txt",data)
    data.printGraph()
    print(data.k)
    print(data.vertices)
    print(data.arestas)