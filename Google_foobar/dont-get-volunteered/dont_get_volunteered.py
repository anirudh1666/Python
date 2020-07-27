# This is question 2.2 from Google foobar challenge.
# The challenge is that you are given a start and end position on a
# chess board with 63 squares and you are a knight. Find the smallest
# number of steps needed to reach destination node.
import math

rows = [(0,7), (8,15), (16,23), (24,31), (32,39),
        (40,47), (48,55), (56,63)]

# Auxiliary function to help dequeue.
def dequeue(queue):

    return queue.pop(0)
    

def calc_neighbours(current):

    row = math.floor(current / 8)
    lower, upper = rows[row]
    ret = []

    if current - 1 >= lower and 0 <= current + 15 <= 63:
        # Move down and left.
        ret.append(current + 15)
    if current + 1 <= upper and 0 <= current + 17 <= 63:
        # Move down and right.
        ret.append(current + 17)
    if current - 1 >= lower and 0 <= current - 17 <= 63:
        # Move up and left
        ret.append(current - 17)
    if current + 1 <= upper and 0 <= current - 15 <= 63:
        # Move up and right.
        ret.append(current - 15)
    if current + 2 <= upper and 0 <= current + 10 <= 63:
        # Move right and down.
        ret.append(current + 10)
    if current + 2 <= upper and 0 <= current - 6 <= 63:
        # Move right and up
        ret.append(current - 6)
    if current - 2 >= lower and 0 <= current + 6 <= 63:
        # Move left and down
        ret.append(current + 6)
    if current - 2 >= lower and 0 <= current - 10 <= 63:
        # Move left and up.
        ret.append(current - 10)

    return ret


def make_path(start, dest, prev):
    
    path = []
    current = dest
    path.append(current)
    while prev[current] != None and current != start:
        # Makes path by going back from end node to start node by getting their parent
        # in prev list.
        parent = prev[current]
        path.append(parent)
        current = parent

    return len(path) - 1
    

def solution(start, dest):

    visited = [False] * 64                  # Keeps track of nodes seen.
    prev = [None] * 64                      # Used to reconstruct shortest path.
    queue = []                              # Acts as a queue data structure.

    queue.append(start)
    visited[start] = True
    prev[0] = start
    while len(queue) != 0:
        # This algorithm uses a breadth first search to find shortest path.
        current = dequeue(queue)
        neighbours = calc_neighbours(current)        # Gets squares that can be 
        for squares in neighbours:                   # reached as a knight.
            if not visited[squares]:
                queue.append(squares)
                visited[squares] = True
                prev[squares] = current

    return make_path(start, dest, prev)

