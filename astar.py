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

    def aStar(self, s, g):
        pQueue = [[path([s])]]
        finPath=None
        while True: # generation 
            i=pQueue[-1]
            print(i)
            if len(i)==1:
                k=i[0]
                pQueue.remove(i)
            else:
                tmList=[a.cost for a in i]
                k=i[tmList.index(min(tmList))]
                i.remove(k)
            tpList=[]
            for j in self.graph[k.path[-1]]:
                print(k.path+[j])
                tmPath=path(k.path+[j])
                if j==g:
                    if finPath==None or finPath.cost>tmPath.cost:
                        finPath=tmPath
                    elif finPath.cost<tmPath.cost:
                        return finPath
                else:
                    tpList.append(tmPath)
            if tpList!=[]:
                pQueue.append(tpList)
            if pQueue==[]:
                return finPath

g = graph()
g.addEdge('A', {'B': 10, 'C': 6})
g.addEdge('B', {'Z': 8, 'D': 5})
g.addEdge('C', {'D': 20})
g.addEdge('D', {'X': 4})
g.addEdge('Z', {'X': 3})
g.addEdge('X', {})

finPath=g.aStar('A', 'X')
print("A* path from A to X :"," -> ".join(finPath.path),"\nCost :",finPath.cost)