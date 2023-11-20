

def readFile(nome, fileData):

    for line in open(nome,"r"):

        if line[0] == "k":
            fileData.k = line[2]
        elif line[0:6] == "p edge":
            fileData.vertices = int(line[7])
            fileData.arestas =  int(line[9])
            fileData.fillGraph()
        elif line[0] == "e":
            values = line.split(" ")
            x = int(values[1])-1
            y = int(values[2])-1
            content = values[3].strip("\n")
            fileData.graph[x][y] = content
            fileData.graph[y][x] = content


