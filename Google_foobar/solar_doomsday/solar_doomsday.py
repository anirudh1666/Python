import math

def solution(area):
    # Naive algorithm
    # 1) Find the next lowest square number <= area.
    # 2) new area = area - square number
    # 3) Repeat until area = 0
    
    ret = []
    while area != 0:
        nearest_squared = math.floor(area ** 0.5)
        nearest_squared = nearest_squared**2
        area = area - nearest_squared
        print('Area: %d  \t Square: %d' %(area, nearest_squared))
        ret.append(int(nearest_squared))
    return ret

print(solution(15324))
print(solution(12))
