import math


def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal


perimeter, area, diagonal = square(int(input("Enter side of a square: ")))
print("Perimeter:", perimeter)
print("Area:", area)
print("Diagonal:", diagonal)
