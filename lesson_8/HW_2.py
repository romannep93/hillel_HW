import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def calculate_area(self):
        if self._is_valid_triangle():
            a = self._calculate_distance(self.point1, self.point2)
            b = self._calculate_distance(self.point2, self.point3)
            c = self._calculate_distance(self.point3, self.point1)
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        else:
            raise ValueError("Invalid triangle coordinates")

    def _is_valid_triangle(self):
        area = 0.5 * (-self.point2.y * self.point3.x + self.point1.y * (-self.point2.x + self.point3.x) +
                      self.point1.x * (self.point2.y - self.point3.y) + self.point2.x * self.point3.y)
        return area != 0

    def _calculate_distance(self, point1, point2):
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)


class Square:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def calculate_area(self):
        if self._is_valid_square():
            side = self._calculate_distance(self.point1, self.point2)
            area = side ** 2
            return area
        else:
            raise ValueError("Invalid square coordinates")

    def _is_valid_square(self):
        d1 = self._calculate_distance(self.point1, self.point2)
        d2 = self._calculate_distance(self.point2, self.point3)
        d3 = self._calculate_distance(self.point3, self.point4)
        d4 = self._calculate_distance(self.point4, self.point1)
        diagonal1 = self._calculate_distance(self.point1, self.point3)
        diagonal2 = self._calculate_distance(self.point2, self.point4)
        return d1 == d2 == d3 == d4 and diagonal1 == diagonal2 == math.sqrt(2) * d1

    def _calculate_distance(self, point1, point2):
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

# Тест


point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(0, 4)
point4 = Point(3, 4)

triangle = Triangle(point1, point2, point3)
square = Square(point1, point2, point3, point4)

try:
    triangle_area = triangle.calculate_area()
    print("Area of triangle:", triangle_area)
except ValueError as e:
    print(e)

try:
    square_area = square.calculate_area()
    print("Area of square", square_area)
except ValueError as e:
    print(e)
