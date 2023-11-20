def readFile(nome, GraphModel):
    for line in open(nome, "r"):
        values = line.split(" ")
        if line[0] == "k":
            GraphModel.k = int(values[1])
        elif line[0:6] == "p edge":
            GraphModel.vertices = int(values[2])
            GraphModel.arestas = int(values[3])
            GraphModel.fillGraph()
        elif line[0] == "e":
            x = int(values[1]) - 1
            y = int(values[2]) - 1
            content = int(values[3].strip("\n"))
            GraphModel.graph[x][y] = content
            GraphModel.graph[y][x] = content
