import math

from models import *


def length(p1: Point, p2: Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def center_of_mass(polygon: Polygon):
    """
    Задание 9
    Найти центр тяжести многоугольника заданного целочисленными координатами своих N вершин.
    (Центр тяжести считается по линейной мере границы.)
    В этом случае масса ребра пропорциональна его длине. Таким образом каждое ребро мы можем заменить на точечную массу (пропорциональную длине ребра).
    :param polygon: Полигон
    :return Point: Центр массы
    """
    n = len(polygon.points)
    full_len = 0
    center = Point(0, 0)

    for i in range(n):
        p1 = polygon.points[i]
        p2 = polygon.points[(i + 1) % n]
        vector_len = length(p1, p2)
        center.x += vector_len * (p1.x + p2.x) / 2
        center.y += vector_len * (p1.y + p2.y) / 2
        full_len += vector_len

    center.x /= full_len
    center.y /= full_len

    return center


def test1_sqare():
    p1 = Point(-1, 1)
    p2 = Point(1, 1)
    p3 = Point(1, -1)
    p4 = Point(-1, -1)
    polygon = Polygon([p1, p2, p3, p4])

    center = center_of_mass(polygon)

    if center.x != 0 and center.y != 0:
        print(f'{test1_sqare.__name__} is Failed, Point: {center}')
    else:
        print(f'{test1_sqare.__name__} is OK')


test1_sqare()
