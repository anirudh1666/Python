# Shortest path algorithm using lazy Dijkstra
# To stop early just check if curNode is endNode and return.
# This makes eager dijkstra
# To optimise further use a D-ary Heap or indexed priority Q.
# Check out https://www.youtube.com/watch?v=09_LlHjoEiY


# Global variables
# (node, edge weight)
graph = {
         0 : [(1,4),(2,1)],
         1 : [(3,1)],
         2 : [(1,2),(3,5)],
         3 : [(4,3)],
         4 : []
         }
startNode = 0
visited = [False for x in range(5)]    # size number of nodes
distance = [10000 for x in range(5)]
prev = [None for x in range(5)]
distance[startNode] = 0
priorityQ = []

def dijkstra(startNode):
    priorityQ.append((startNode,0))    # (Node,distance from start)
    while len(priorityQ) != 0:
        nextNode = poll(priorityQ)
        print("NextNode: " + str(nextNode))
        node = nextNode[0]
        distanceTo = nextNode[1]
        visited[node] = True
        if distance[node] < distanceTo:
            continue
        neighbours = graph.get(node)
        for neighbour in neighbours:
            neighbourNode = neighbour[0]
            neighbourDistance = neighbour[1]
            print("NeighbourNode: " + str(neighbourNode) + " NeighD: " + str(neighbourDistance))
            if visited[neighbourNode]:
                continue
            newDistance = distance[node] + neighbourDistance
            print("NewD: " + str(newDistance) + " distanceCur: " + str(distance[neighbourNode]))
            if newDistance < distance[neighbourNode]:
                distance[neighbourNode] = newDistance
                prev[neighbourNode] = node
                print("Distance: " + str(distance))
                priorityQ.append((neighbourNode, newDistance))
    return (distance, prev)

def findShortestPath(startNode, endNode):
    getPrev = dijkstra(startNode)
    prev = getPrev[1]
    path = []
    if distance[endNode] == 10000:
        return path
    curNode = endNode
    while curNode != None:
        path.append(curNode)
        curNode = prev[curNode]
    path.reverse()
    return path



def poll(queue):
    minValue = (1000,10000)
    for element in queue:
        if element[1] < minValue[1]:
            minValue = element
    queue.remove(minValue)
    return minValue

print(findShortestPath(0, 4))
         

