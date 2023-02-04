class node:
    def __init__(self,value=None):
        self.child=[]
        self.A=None
        self.B=None
        self.value=value

def makeTree(value):
    root=node()
    if len(value)>1:
        r = value[0:int(len(value)/2)+(len(value)%2)]
        print(r)
        root.child.append(makeTree(r))
        l = value[int(len(value)/2)+(len(value)%2):len(value)]
        # if len(l)>1:
        print(l,"left")
        root.child.append(makeTree(l))
    else:
        root.value=value[0]
    return root

# depth first traversal
def dfs(root):
    print(root.value)
    for i in root.child:
        dfs(i)

aList = [int(i) for i in input("Please enter a list of numbers : ").split()]
print(aList)
root = makeTree(aList)
dfs(root)
