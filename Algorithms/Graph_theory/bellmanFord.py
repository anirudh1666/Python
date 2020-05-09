# Bellman-Ford algorithm

class Edge:

    def __init__(self, to=None, before=None, weight=None):
        self.to = to
        self.before = before
        self.weight = weight

    def getWeight(self):
        return self.weight

    def getTo(self):
        return self.to

    def getFrom(self):
        return self.before


# Graph
edge0 = Edge(1, 0, 5)
edge1 = Edge(2, 1, 20)
edge2 = Edge(3, 2, 10)
edge3 = Edge(2, 3, -15)
edge4 = Edge(4, 2, 75)
edge5 = Edge(9, 4, 100)
edge6 = Edge(5, 1, 30)
edge7 = Edge(6, 5, 5)
edge8 = Edge(6, 1, 60)
edge9 = Edge(7, 6, -50)
edge10 = Edge(8, 7, -10)
edge11 = Edge(8, 5, 50)
edge12 = Edge(4, 5, 25)
graph = [edge0, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8 ,edge9, edge10, edge11, edge12]


# Global variables
numOfEdges = 13
numOfNodes = 10
startNode = 0
distance = [1000000 for x in range(numOfNodes)]    # Large value for infinity


def bellmanFord(startNode):
    global numOfEdges
    distance[startNode] = 0
    prev = [None for x in range(numOfNodes)]
    for x in range(numOfNodes):
        for edge in graph:
            edgeWeight = edge.getWeight()
            edgeTo = edge.getTo()
            edgeFrom = edge.getFrom()
            if distance[edgeFrom] + edgeWeight < distance[edgeTo]:  # Relax edge
                prev[edgeTo] = edgeFrom
                distance[edgeTo] = distance[edgeFrom] + edgeWeight
    for x in range(numOfNodes):
        for edge in graph:
            edgeWeight = edge.getWeight()
            edgeTo = edge.getTo()
            edgeFrom = edge.getFrom()
            if distance[edgeFrom] + edgeWeight < distance[edgeTo]:  # Detect any negative cycles
                distance[edgeTo] = -10000000
    return (distance, prev)

def findShortestPath(startNode, endNode):    # Find the lowest cost path to endNode from startNode
    bellman = bellmanFord(startNode)
    prev = bellman[1]
    path = []
    curNode = endNode
    while curNode != None:
        path.append(curNode)
        curNode = prev[curNode]
    path.reverse()
    return path

print("Running Bellman-Ford algorithm. If you get -10000000 it means that node is part of negative cycle")
print()
print(findShortestPath(0, 8))
        
