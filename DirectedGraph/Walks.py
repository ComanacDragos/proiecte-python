from DirectedGraph import *
from Traversals import *
from queue import PriorityQueue
from Utility import *


def lowest_length_path_forward_breadth_first(graph, start):
    '''
    :param graph: directed graph
    :param start: starting vertex
    :return: lowest length path between a staring node and all accessible nodes, by using a forward breadth-first search from the starting vertex
    '''
    if start not in graph.get_vertices():
        raise VertexException("Vertex doesn't exist")

    queue = []
    predecesors = {}
    lengths = {}
    visited = set()
    queue.insert(0, start)
    visited.add(start)
    lengths[start] = 0
    predecesors[start] = -1

    while len(queue) != 0:
        x = queue.pop()
        for y in graph.parse_outbound(x):
            if y not in visited:
                queue.insert(0, y)
                visited.add(y)
                lengths[y] = lengths[x] + 1
                predecesors[y] = x

    return predecesors


def forward_Dijkstra(graph, start, end):
    '''
    :param graph: directed graph with positive costs
    :param start: starting vertex
    :param end: starting vertex
    :return: a map that maps each accessible vertex to its predecessor on a path from s to it
    '''
    if start not in graph.get_vertices():
        raise VertexException("End vertex doesn't exist\n")
    if end not in graph.get_vertices():
        raise VertexException("End vertex doesn't exist\n")

    queue = PriorityQueue()
    predecesors = {}
    predecesors[start] = -1
    distances = {}
    queue.put((0, start)) # first argument in tuple is priority
    distances[start] = 0
    found = False

    while queue.qsize() != 0 and not found:
        x = queue.get()[1]
        for y in graph.parse_outbound(x):
            if y not in distances.keys() or distances[x] + graph.get_cost(x,y) < distances[y]:
                distances[y] = distances[x] + graph.get_cost(x,y)
                queue.put((distances[y], y))
                predecesors[y] = x
        if x == end:
            found = True

    return  (predecesors, distances)

def printQueque(q):
    list=[]
    while q.qsize():
        x = q.get()
        list.append(x)
        print(x, end=' ')
    print()
    for x in list:
        q.put(x)

def backwards_dijkstra(graph, start, end):
    '''
        :param graph: directed graph with positive costs
        :param start: starting vertex
        :param end: starting vertex
        :return: a map that maps each accessible vertex to its predecessor on a path from s to it
        '''
    if start not in graph.get_vertices():
        raise VertexException("End vertex doesn't exist\n")
    if end not in graph.get_vertices():
        raise VertexException("End vertex doesn't exist\n")

    queue = PriorityQueue()
    successors = {}
    successors[end] = -1
    distances = {}
    queue.put((0, end))  # first argument in tuple is priority
    distances[end] = 0
    found = False

    while queue.qsize() != 0 and not found:
        x = queue.get()[1]
        for y in graph.parse_inbound(x):
            if y not in distances.keys() or distances[x] + graph.get_cost(y, x) < distances[y]:
                distances[y] = distances[x] + graph.get_cost(y, x)
                queue.put((distances[y], y))
                successors[y] = x

        if x == start:
            found = True

    return (successors, distances)

def dynamic_programming_minimum_cost_walk(graph, mxLen, start):
    '''
    :param graph:
    :param mxLen:
    :return: the cost of minimum cost walk of length at most k from s to x, or ∞ if no such walk exists
    '''
    walk = Matrix(mxLen, graph.vertices)

    for i in range(walk.columns):
        walk[0][i] = math.inf

    walk[0][start] = 0

    for k in range(1, mxLen):
        for x in range(graph.vertices):
            mn = math.inf
            for y in graph.parse_inbound(x):
                current = walk[k-1][y] + graph.get_cost(y,x)
                if mn > current:
                    mn = current
            walk[k][x] = min(mn, walk[k-1][x])
    return walk

def Bellman_Ford(graph, start):
    '''
    :param graph:
    :param start: starting vertex
    :return:
    '''
    #Step1: initialize
    prev = {}
    dist = {}
    for x in graph.get_vertices():
        dist[x] = math.inf
    dist[start] = 0
    prev[start] = -1


    edges = graph.get_costs()

    #Step2: "relax" edges
    for i in range(graph.vertices-1):
        for edge in edges.keys():
            x = edge[0]
            y = edge[1]
            if dist[y] > dist[x] + edges[edge]:
                dist[y] = dist[x] + edges[edge]
                prev[y] = x

    #Step3: Check for negative cost cycles
    for edge in edges.keys():
        x = edge[0]
        y = edge[1]
        if dist[y] > dist[x] + edges[edge]:
            return -1

    return (prev, dist)


'''
g=DoubleDictGraph()
loadGraph(g, "Graphs/Example2.txt")
bf = Bellman_Ford(g, 0)
print(bf)
for i in bf[0].keys():
    print(i, bf[0][i])

print()

for i in bf[1].keys():
    print(i, bf[1][i])

loadGraph(g, "Graphs/graph_negative_cost_cycle.txt")
print(Bellman_Ford(g, 0))
'''