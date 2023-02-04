from queue import PriorityQueue

class path:
    def __init__(self,path):
        self.path=path
        self.pathCost(g)

    def pathCost(self, g):
        cost = 0
        for i, val in enumerate(self.path[1:]):
            cost += g.graph[self.path[i]][val]
        cost += g.h(self.path[-1])
        self.cost=cost

class graph:
    def __init__(self):
        self.graph = dict()

    def addEdge(self, v, u):
        self.graph[v] = u

    def h(self, a):
        hur = {'A': 12, 'B': 8, 'C': 12, 'D': 3, 'Z': 3, 'X': 0}
        return hur[a]

    def bestfs(self, s, g):
        openpq=PriorityQueue()
        closedq=[]
        openpq.put((self.h(s),s))
        while True:
            tem = openpq.get()
            for c in self.graph[tem[1]]:
                openpq.put((self.h(c),c))
            closedq.append(tem[1])
            if closedq[-1]==g:
                return path(closedq)

g = graph()
g.addEdge('A', {'B': 10, 'C': 6})
g.addEdge('B', {'Z': 8, 'D': 5})
g.addEdge('C', {'D': 20})
g.addEdge('D', {'X': 4})
g.addEdge('Z', {'X': 3})
g.addEdge('X', {})

finPath=g.bestfs('A', 'X')
print("Best First path from A to X :"," -> ".join(finPath.path),"\nCost :",finPath.cost)