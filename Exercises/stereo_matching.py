import numpy as np
import cv2 as cv

# Global variables
occlusion = 0.5
variance = 16


# Img1 = columns, img2 = rows
img1 = cv.imread("view1A.png", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("view2A.png", cv.IMREAD_GRAYSCALE)
rows = len(img1[0])
columns = len(img2[0])
disparityMap = np.zeros(img1.shape)

# Builds a cost matrix and a path matrix to find lowest cost path.
def buildMatrix(row):
    costM = np.zeros((rows+1, columns+1))
    costM[0][0] = 0
    for x in range(1, rows+1):               # Assumes rows == columns
        costM[x][0] = x * occlusion
        costM[0][x] = x * occlusion
    for x in range(1, columns+1):
        for y in range(1, rows+1):
            above = costM[y-1][x] + occlusion
            left = costM[y][x-1] + occlusion
            diagonal = costM[y-1][x-1] + matchCost(img1[row][y-1], img2[row][x-1])
            minimum = min(above, left, diagonal)
            costM[y][x] = minimum
    return costM

# Cost of matching two pixels.
def matchCost(pixel1, pixel2):
    avg = (pixel1 + pixel2) / 2
    cost = ((avg - pixel1) * (avg - pixel2)) / variance
    return np.absolute(cost)

def disparityRow(pathM):
    disparityLine = np.zeros(len(disparityMap[0]))
    curY = len(pathM) - 1
    curX = len(pathM[0]) - 1
    while curY != 0 and curX != 0:
        above = pathM[curY-1][curX]
        left = pathM[curY][curX-1]
        diagonal = pathM[curY-1][curX-1]
        minimum = min(above, left, diagonal)
        if minimum == diagonal:
            disparity = np.absolute(curX - curY) + 190
            disparityLine[curY-1] = disparity
            curX -= 1
            curY -= 1
        elif minimum == left:
            curX -= 1
        else:
            curY -= 1
    for x in range(len(disparityLine)):
        if disparityLine[x] == 0:
            disparityLine[x] = 80
    return disparityLine


for row in range(len(img1)):
    pathM = buildMatrix(row)
    disparityMap[row] = disparityRow(pathM)
    print(str(row) + " has been calculated.")
cv.imwrite("viewK.png", disparityMap)
