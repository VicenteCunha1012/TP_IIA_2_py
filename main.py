from utils import *
from algo import *

from random import randint
import time
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def submit():
    filename = filename_entry.get()
    iterations = iterations_entry.get()

    # You can add your logic or processing here
    iterations_label.config(text="Introduziste: " + iterations)
    filename_label.config(text="Introduziste: " + filename)
    print(f"File Name: {filename}")
    print(f"Number of Iterations: {iterations}")


def plot_graph():
    # Sample data for the plot
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(x_data, y_data, label='Sample Plot')

    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Sample Plot')

    # Display legend
    ax.legend()

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()


# Create the main window
window = tk.Tk()
window.title("Tkinter Example")

# Set the initial size of the window
window.geometry("600x400")  # Width x Height

# Create and place labels and entry widgets
filename_label = tk.Label(window, text="Nome do Ficheiro:")
filename_label.pack(pady=5)

filename_entry = tk.Entry(window, width=30)
filename_entry.pack(pady=5)

iterations_label = tk.Label(window, text="Numero de Iteracoes:")
iterations_label.pack(pady=5)

iterations_entry = tk.Entry(window, width=30)
iterations_entry.pack(pady=10)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Button to plot the graph
plot_button = tk.Button(window, text="Plot Graph", command=plot_graph)
plot_button.pack()

# Start the main loop
window.mainloop()

'''
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
    model.create_admissible_neighbour()
    print("Solucao admissivel" + str(model.solucao))



    model.hill_climbing()

    print("Best cost" + str(model.bestCost))
    print("Best solution" + str(model.bestSolution))





'''