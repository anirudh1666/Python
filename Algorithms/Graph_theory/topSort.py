# Topological sort algorithm
# Uses DFS and once it reaches a node that has all visited nodes add
# it to the topological order.

graph = {
         0 : [1,2,3],
         1 : [2],
         2 : [8,10],
         3 : [4,5],
         4 : [5],
         5 : [6,7],
         6 : [],
         7 : [],
         8 : [5,9],
         9 : [7],
         10 : [9],
         11 : [1,12],
         12 : [2]
         }

# Global variables
numNodes = 12
visited = [False for x in range(13)]
topSortPath = [None for x in range(13)]
index = 12


def topSort():
    global index
    for x in range(numNodes):
        if not visited[x]:
            index = dfs(x, topSortPath)
    return topSortPath

def dfs(at, topSortPath):
    if visited[at]:
        return
    visited[at] = True
    neighbours = graph.get(at)
    for nodes in neighbours:
        index = dfs(nodes, topSortPath)
    topSortPath[index] = at
    return index - 1

print(topSort())
