rivers =[
    [1,0,0,1,0],
    [1,0,1,0,0],
    [0,0,1,0,1],
    [1,0,1,0,1],
    [1,0,1,1,0]
]
h = len(rivers)
w = len(rivers[1])
size = 0
for i in rivers:
    size += sum(i)

class Graph:
    def __init__(self, size):
        self.size = size
        self.g = []
        for i in range(size):
            l = [0]*size
            self.g.append(l)

    def add_edge(self,edge):
        self.g[edge[0]][edge[1]] = 1

    def __str__(self):
        s = ""
        for i in self.g:
            for j in i:
                s+=str(j)
                s+= ' '
            s+='\n'
        return s

def get_neighbors(x,y):
    neighbors = [[x+1,y], [x,y+1], [x-1,y], [x,y-1]]
    i = 0
    n = 4
    while i<n:
        aux = neighbors[i]

        if aux[0] <0 or aux[0] > h-1 or aux[1] < 0 or aux[1] > w - 1:
            neighbors.pop(i)
            n -= 1
        else:
            i += 1

    return neighbors

g = Graph(size)
node = 0


ap = []
for i in range(h):
    l = [0] * w
    ap.append(l)

lenght = []

def DF (x,y):
    ap[x][y] = 1
    #print(x,y)
    lenght[-1] += 1
    neighbors = get_neighbors(x,y)
    for i in neighbors:
        a = i[0]
        b = i[1]
        if rivers[a][b] == 1 and ap[a][b] == 0:
            DF(a,b)



for i in range(h):
    for j in range(w):
        if rivers[i][j] == 1 and ap[i][j] == 0:
            lenght.append(0)
            DF(i,j)

lenght.sort()
print(lenght)



