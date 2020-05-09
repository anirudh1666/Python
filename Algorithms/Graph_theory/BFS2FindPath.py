# This is dungeon path finder program.
# This what dungeon matrix should represent.
# Finds the shortest number of steps needed to reach the end.
#    ---------------
#    |S| | |#| | | |  
#    | |#| | | |#| |
#    | |#| | | | | |
#    | | |#|#| | | |
#    |#| |#| | |#|E|
#    ---------------
#   # - Rocks cant move there S - Start E - Exit


# Use 2 queues to represent (x,y)
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

sr = 0
sc = 0
rowVector = [1,-1,0,0]
colVector = [0,0,1,-1]
numOfSteps = 0
nodesLeftInQueue = 1
nodesNextInQueue = 0
moves = 0
reachedEnd = False
dungeon = [["S"," "," ","#"," "," "," "],
           [" ","#"," "," "," ","#"," "],
           [" ","#"," "," "," "," "," "],
           [" "," ","#","#"," "," "," "],
           ["#"," ","#"," "," ","#","E"]]
numRows = len(dungeon)
numCols = len(dungeon[0])
xQueue = Queue()
yQueue = Queue()
visited = [[False for x in range(numCols)] for y in range(numRows)]


def solve(sr, sc):
    global nodesLeftInQueue, nodesNextInQueue, numOfSteps, moves
    prevX = Queue()
    prevY = Queue()
    xQueue.enqueue(sc)
    yQueue.enqueue(sr)
    visited[sr][sc] = True
    while not xQueue.isEmpty():
        x = xQueue.dequeue()
        y = yQueue.dequeue()
        if dungeon[y][x] == "E":
            reachedEnd = True
            break
        exploreNeighbours(x,y)
        nodesLeftInQueue -= 1
        if nodesLeftInQueue == 0:
            nodesLeftInQueue = nodesNextInQueue
            #moves = 1
            print((x,y))
            nodesNextInQueue = 0
            numOfSteps += 1
    if reachedEnd == True:
        return numOfSteps
    return -1

def exploreNeighbours(row, col):
    global nodesNextInQueue
    for x in range(4):
        xNeighbour = row + rowVector[x]
        yNeighbour = col + colVector[x]
        if xNeighbour < 0 or yNeighbour < 0:
            continue
        if xNeighbour >= numCols or yNeighbour >= numRows:
            continue
        if visited[yNeighbour][xNeighbour] == True:
            continue
        visited[yNeighbour][xNeighbour] = True
        if dungeon[yNeighbour][xNeighbour] == "#":
            continue
        xQueue.enqueue(xNeighbour)
        yQueue.enqueue(yNeighbour)
        nodesNextInQueue += 1

# Try to find path.
def reconstructPath(prevX, prevY):
    global sr, sc
    path = []
    curX = prevX.dequeue()
    curY = prevY.dequeue()
    path.append((curX, curY))
    while curX != sc or curY != sr:
        print((curX, curY))
        parentX = prevX.dequeue()
        parentY = prevY.dequeue()
        path.append((parentX, parentY))
        curX = parentX
        curY = parentY
    if path[0] == (sc, sr):
        return path
    return []
    
print(solve(sr,sc))
        
