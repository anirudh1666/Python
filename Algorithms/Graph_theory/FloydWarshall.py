import numpy as np

# Floyd-Warshall algorithm
# Uses dynamic programming by storing shortest path in a
# n x n matrix. Can reduce running time by using n x n x n matrix
# but space complexity maybe too high.

# Global variables
graph = np.array([[0,float('inf'),6,3,float('inf')],                  # Graph, use float('inf') to represent
                  [3,0,float('inf'),float('inf'),float('inf')],       # unconnected edges.
                  [float('inf'),float('inf'),0,2,float('inf')],
                  [float('inf'),1,1,0,float('inf')],
                  [float('inf'),4,float('inf'),2,0]])
noOfNodes = len(graph)
solution = np.zeros((noOfNodes,noOfNodes))          # Dynamic programming solution with shortest distance to each other.
next = np.zeros((noOfNodes,noOfNodes))              # Used to reconstruct path.

def floydWarshall(matrix, solution, next):
    setup(matrix, solution, next)
    
    for k in range(noOfNodes):
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if solution[row][k] + solution[k][column] < solution[row][column]:
                    solution[row][column] = solution[row][k] + solution[k][column]
                    next[row][column] = next[row][k]

    print("Solution: ")
    print(solution)
    print()
    propagateNegativeCycles(solution, next)        # Detects any negative cycles.
    return (solution, next)
    

# Initialises solution. Assumes shortest path is direct.
def setup(matrix, solution, next):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            solution[row][column] = matrix[row][column]
            if matrix[row][column] != float('inf'):
                next[row][column] = column


# Runs floydWarshall again and if distance can be improved it sets
# distance as -infinity since it is part of negative cycle.
def propagateNegativeCycles(solution, next):
    for k in range(noOfNodes):
        for row in range(len(solution)):
            for column in range(len(solution[0])):
                if solution[row][k] + solution[k][column] < solution[row][column]:
                    solution[row][column] = float('-inf')
                    next[row][column] = -1


# Reconstructs shortest path from startNode to endNode.
def reconstructPath(startNode, endNode, next):
    path = []
    at = startNode
    if solution[startNode][endNode] == float('inf') :
        return path
    while at != endNode:
        if at == -1:
            return None
        path.append(at)
        at = int(next[at][endNode])
    print(next)
    if next[at][endNode] == -1:
        return path
    path.append(endNode)
    return path


print("Running floydWarshall")
print()
solution, next = floydWarshall(graph, solution, next)
print("Shortest path from 0 -> 3")
print(reconstructPath(0, 3, next))

