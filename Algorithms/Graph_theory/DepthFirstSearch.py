class AdjacencyNode:
    def __init__(self, nodes=None):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes


#Global variables
    
node0 = AdjacencyNode([1,3])
node1 = AdjacencyNode([0,2,3])
node2 = AdjacencyNode([1,4])
node3 = AdjacencyNode([0,1])
node4 = AdjacencyNode([2,5,6])
node5 = AdjacencyNode([4,6,7])
node6 = AdjacencyNode([4,5])
node7 = AdjacencyNode([5,8])
node8 = AdjacencyNode([8])
graph = [node0, node1, node2, node3, node4, node5, node6, node7, node8]


numNodes = 9
visited = [False, False, False, False, False, False, False, False, False]


def dfs(at):
    if visited[at]:
        return
    print(at)
    visited[at] = True
    curNode = graph[at]
    neighbours = curNode.getNodes()
    for next in neighbours:
        dfs(next)


startNode = 0
dfs(startNode)


