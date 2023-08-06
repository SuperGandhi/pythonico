import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        dx = self._x - float(x)
        dy = self._y - float(y)
        return math.hypot(dx, dy)

    def distance_from_point(self, point):
        if not isinstance(point, Point):
            raise ValueError("Invalid point object")
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, point1, point2, point3):
        if not isinstance(point1, Point) or not isinstance(point2, Point) or not isinstance(point3, Point):
            raise ValueError("Invalid point object")
        self._points = [point1, point2, point3]

    def perimeter(self):
        side1 = self._points[0].distance_from_point(self._points[1])
        side2 = self._points[1].distance_from_point(self._points[2])
        side3 = self._points[2].distance_from_point(self._points[0])
        return side1 + side2 + side3

# Prueba de la clase Triangle
try:
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(0, 4)

    triangle = Triangle(point1, point2, point3)
    print(triangle.perimeter())  # Output: 12.0
except ValueError as e:
    print("Error:", e)
