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

# Prueba de la clase Point
try:
    point1 = Point(3, 4)
    print(point1.getx())  # Output: 3.0
    print(point1.gety())  # Output: 4.0

    point2 = Point(5, 6)
    print(point2.getx())  # Output: 5.0
    print(point2.gety())  # Output: 6.0

    distance1 = point1.distance_from_xy(1, 1)
    print(distance1)  # Output: 3.605551275463989

    distance2 = point1.distance_from_point(point2)
    print(distance2)  # Output: 2.8284271247461903
except ValueError as e:
    print("Error:", e)
