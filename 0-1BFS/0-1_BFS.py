import collections
V = 1000
INT_MAX = 2 ** 31 - 1
Q = collections.deque()
graph = [[] for _ in range(V)]
dist = [0] * V



def distbfs(i, v):
    global dist, graph
    return dist[v] + graph[v][i][1]

def zeronOneBFS(s, n):
    '''
    To print shortest distance from given source (here, 0) to every other node 
    '''
    global dist, graph, Q
    i = 0
    while (i < n):
        if i == source:
            dist[i] = 0
            Q.append(i)
        else:
            dist[i] = INT_MAX
        i += 1

    while Q:
        v = Q.pop()
        for i in range(len(graph[v])):
            if dist[graph[v][i][0]] > distbfs(i, v):
                dist[graph[v][i][0]] = distbfs(i, v)
                if (graph[v][i][1] == 0):
                    Q.appendleft(graph[v][i][0])
                else:
                    Q.append(graph[v][i][0])
    
    for i in range(n):
        print(dist[i])

def addEdge(u, v, wt):
    global graph
    print(u, v, wt)
    graph[u].append((v, wt))
    graph[v].append((u, wt))

def create_graph():
    for _ in range(e):
        u, v, wt = input().split()
        u, v, wt = int(u), int(v), int(wt)
        addEdge(u, v, wt)


n = int(input("Enter number of vertices"))
e = int(input("Enter number of edges"))
create_graph()
source = 0
zeronOneBFS(source, n)
