class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return int(self.x + self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'


class Polygon:
    def __init__(self, points: list[Point]):
        self.points = points
