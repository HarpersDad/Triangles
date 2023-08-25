import math

def findHeight(a, b, c, area):
    base = 0

    if a <= b:
        base = b
        if b <= c:
            base = c
    else:
        base = a
        if a <= c:
            base = c

    h = (2 * area) / base

    print("Height: ", h)


# find area of a triangle
def findArea(a, b, c):

    s = (a + b + c) / 2

    sA = s-a
    sB = s-b
    sC = s-c

    sS = s * sA * sB * sC

    area = math.sqrt(sS)

    print("Area: ", area)

    findHeight(a, b, c, area)


def main():
    sideA = input("Enter side A: ")
    sideB = input("Enter side B: ")
    sideC = input("Enter side C: ")

    findArea(int(sideA), int(sideB), int(sideC))


main()
