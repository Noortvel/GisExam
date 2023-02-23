from models import *


def all_integer_points(polygon: Polygon) -> list[Point]:
    """
    Задание8
    Дан многоугольник на плоскости. Найти множество точек с целочисленными координатами лежащих на границе этого многоугольника.
    :param polygon: Многоугольник
    :return list[Point]: Список целочисленных точек на границах
    """

    def greatest_common_divisor(a, b):
        """Поиск наибольшего общего делителя"""
        while b > 0:
            a, b = b, a % b
        return a

    points_set = set()
    """
    Идем по всем отрезкам P(i), P(i+1) и считаем целочисленные координаты
    по формуле
    n = НОД(|x₂ − x₁|, |y₂ − y₁|)
    dx = (x₂ − x₁) / n
    dy = (y₂ − y₁) / n
    """
    for i in range(len(polygon.points)):
        p1 = polygon.points[i]
        p2 = polygon.points[(i + 1) % len(polygon.points)]
        delta_x = (p2.x - p1.x)
        delta_y = (p2.y - p1.y)
        gcd = greatest_common_divisor(abs(delta_x), abs(delta_y))
        dx = delta_x / gcd
        dy = delta_y / gcd
        for j in range(gcd + 1):
            points_set.add(Point(p1.x + (dx * j), p1.y + (dy * j)))
    return list(points_set)


def ratio_part(value: float):
    return value - int(value)


def is_decimaled(value: float):
    return ratio_part(value) > 0.00001


def assert_polygon_is_int(result_points: list[Point], func_name: str = 'assert_polygon_is_int'):
    is_ok = True
    failed_point = None
    for point in result_points:
        if is_decimaled(point.x) or is_decimaled(point.y):
            is_ok = False
            failed_point = point
            break
    if is_ok:
        print(f'{func_name} is OK')
    else:
        print(f'{func_name} is OK, point: {failed_point}')


def test1_check_segment():
    p1 = Point(0, 0)
    p2 = Point(3, 3)
    polygon = Polygon([p1, p2])

    result_points = all_integer_points(polygon)

    assert_polygon_is_int(result_points, test1_check_segment.__name__)


def test2_check_square():
    p1 = Point(0, 0)
    p2 = Point(0, 1)
    p3 = Point(1, 1)
    p4 = Point(1, 0)
    polygon = Polygon([p1, p2, p3, p4])

    result_points = all_integer_points(polygon)

    assert_polygon_is_int(result_points, test2_check_square.__name__)


def test3_check_octagon():
    p1 = Point(-20, 0)
    p2 = Point(-10, 10)
    p3 = Point(0, 20)
    p4 = Point(10, 10)
    p5 = Point(20, 0)
    p6 = Point(10, -10)
    p7 = Point(0, -20)
    p8 = Point(-10, -10)

    polygon = Polygon([p1, p2, p3, p4, p5, p6, p7, p8])

    result_points = all_integer_points(polygon)

    assert_polygon_is_int(result_points, test3_check_octagon.__name__)


def test4_check_big_rectangle():
    p1 = Point(0, 0)
    p2 = Point(0, 10)
    p3 = Point(10, 10)
    p4 = Point(10, 0)
    polygon = Polygon([p1, p2, p3, p4])

    result_points = all_integer_points(polygon)

    assert_polygon_is_int(result_points, assert_polygon_is_int.__name__)

    if len(result_points) == 40:
        print('OK points count')
    else:
        print(f'FAILED points count = {len(result_points)}')


test1_check_segment()
test2_check_square()
test3_check_octagon()
test4_check_big_rectangle()
