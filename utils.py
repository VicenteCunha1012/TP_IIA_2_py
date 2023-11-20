

def readFile(nome, GraphModel):

    for line in open(nome,"r"):

        if line[0] == "k":
            GraphModel.k = int(line[2])
        elif line[0:6] == "p edge":
            GraphModel.vertices = int(line[7])
            GraphModel.arestas =  int(line[9])
            GraphModel.fillGraph()
        elif line[0] == "e":
            values = line.split(" ")
            x = int(values[1])-1
            y = int(values[2])-1
            content = int(values[3].strip("\n"))
            GraphModel.graph[x][y] = content
            GraphModel.graph[y][x] = content


