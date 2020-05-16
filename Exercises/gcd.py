# This program calculates GCD of
# two numbers. Made by Anirudh Lakra.

def GCD(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


first_num = int(input("Enter a number: "))
second_num = int(input("Enter a second number: "))
print("GCD: " + str(GCD(first_num, second_num)))
