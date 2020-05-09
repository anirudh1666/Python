# Using dfs to find number of connected components in a graph
import numpy as np

class AdjacencyNode:
    def __init__(self, nodes=None):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes

#Global variables
    
node0 = AdjacencyNode([4,8,13,14])
node1 = AdjacencyNode([5])
node2 = AdjacencyNode([9,15])
node3 = AdjacencyNode([9])
node4 = AdjacencyNode([0,8])
node5 = AdjacencyNode([1,16,17])
node6 = AdjacencyNode([7,11])
node7 = AdjacencyNode([6,11])
node8 = AdjacencyNode([0,4,14])
node9 = AdjacencyNode([2,3,15])
node10 = AdjacencyNode([15])
node11 = AdjacencyNode([6,7])
node12 = AdjacencyNode()
node13 = AdjacencyNode([0,14])
node14 = AdjacencyNode([0,8,13])
node15 = AdjacencyNode([2,9,10])
node16 = AdjacencyNode([5])
node17 = AdjacencyNode([5])
graph = [node0, node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, node16, node17]
count = 0                            # Number of components
visited = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
components = np.zeros(len(graph))

def computeComponents():
    for x in range(len(graph)):
        if not visited[x]:
            global count
            count += 1
            print("count: " + str(count) + " Current Node: " + str(x))
            dfs(x)
    return count

def dfs(at):
    if visited[at]:
            return
    components[at] = count
    curNode = graph[at]
    neighbours = curNode.getNodes()
    if neighbours == None:
        return
    visited[at] = True
    for nodes in neighbours:
        dfs(nodes)


print(computeComponents())





















    


