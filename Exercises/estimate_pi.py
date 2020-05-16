# This program estimates the value of PI to
# a number of digits specificed by user.
# Made by Anirudh Lakra.

import random
import math

def estimate_pi(precision):

    hit = 0
    miss = 0
    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        new_x = abs(x - 0.5)
        new_y = abs(y - 0.5)
        distance = math.hypot(new_x, new_y)

        if distance < 0.5:
            hit += 1
        else:
            miss += 1
        total = hit + miss
        if total == 1000:
            break

    pi = (hit / total) * 4
    new_pi = round(pi, precision)
    return new_pi




print("This program estimates the value of PI using Monte-Carlo method.")
prec = int(input("Enter the precision here: "))
pi = estimate_pi(prec)
print("PI: " + str(pi))
