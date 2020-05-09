# Breadth first search algorithm that finds the shortest path to an edge.

class AdjacencyNode:
    def __init__(self, nodes=None):
        self.nodes = nodes

    def getNodes(self):
        return self.nodes


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0


# Global variables

node0 = AdjacencyNode([7,11,9])
node1 = AdjacencyNode([])
node2 = AdjacencyNode([])
node3 = AdjacencyNode([2,4])
node4 = AdjacencyNode([])
node5 = AdjacencyNode([])
node6 = AdjacencyNode([5])
node7 = AdjacencyNode([3,6])
node8 = AdjacencyNode([12])
node9 = AdjacencyNode([8,10])
node10 = AdjacencyNode([1])
node11 = AdjacencyNode([])
node12 = AdjacencyNode([2])
node13 = AdjacencyNode([])
graph = [node0, node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13]
visited = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
numNodes = len(graph)



def bfs(startNode, endNode):
    prev = solve(startNode)
    return reconstructPath(startNode, endNode, prev)


def solve(startNode):
    queue = Queue()
    queue.enqueue(startNode)
    visited[startNode] = True
    prev = [None] * numNodes
    prev[0] = startNode
    while not queue.isEmpty():
        curNode = queue.dequeue()
        node = graph[curNode]
        neighbours = node.getNodes()
        for nodes in neighbours:
            if not visited[nodes]:
                queue.enqueue(nodes)
                visited[nodes] = True
                prev[nodes] = curNode
    return prev


def reconstructPath(startNode, endNode, prev):
    path = []
    curNode = endNode
    path.append(curNode)
    while prev[curNode] != None and curNode != startNode:
        print(curNode)
        parent = prev[curNode]
        path.append(parent)
        curNode = parent
    path.reverse()
    if path[0] == startNode:
        return path
    return []


startNode = 0
endNode = 13
print(bfs(startNode, endNode))
            























