import matplotlib.pyplot as plt

from dcel.dcel import Dcel
from dcel.dcel import Vertex
from dcel.dcel import Hedge
from models import Point


def nearest_linar_choise(target, a, b):
    dt0 = abs(target - a)
    dt1 = abs(target - b)
    if dt0 <= dt1:
        return 0
    return 1


def binary_search_closest(arr, x, key):
    """
    :param arr:
    :param x:
    :param key:
    :return index of arr:
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    if len(arr) == 2:
        return nearest_linar_choise(x, key(arr[0]), key[arr[1]])

    while low <= high:
        mid = (high + low) // 2
        val = key(arr[mid])
        if val < x:
            low = mid + 1
        elif val > x:
            high = mid - 1
        else:
            return mid

    if low == high:
        return low
    else:
        return nearest_linar_choise(x, key(arr[high]), key(arr[low]))


def binary_search(arr, x, key):
    """
    :param arr:
    :param x:
    :param key:
    :return index of arr:
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        val = key(arr[mid])
        if val < x:
            low = mid + 1
        elif val > x:
            high = mid - 1
        else:
            return mid

    return -1


class Slab:
    def __init__(self, x_pos):
        self.hedges: [Hedge] = []
        self.x_pos = x_pos


class SlabSearchAlgorithm:
    def __init__(self, dcel: Dcel):
        self.dcel = dcel
        sorted_by_x = list(set([v.x for v in dcel.vertices]))
        sorted_by_x.sort(key=lambda x: x)

        self.slabs: [Slab] = []
        for x in sorted_by_x:
            self.slabs.append(Slab(x))

        for s in self.slabs:
            shedges = set()
            for he in dcel.hedges:
                x_min = min(he.v1.x, he.v2.x)
                x_max = max(he.v1.x, he.v2.x)
                if x_min <= s.x_pos <= x_max:
                    shedges.add(he)

            s.hedges = list(shedges)
            s.hedges.sort(key=lambda h: h.origin.y)

    def find_hedge(self, point: Point) -> Hedge:
        slab_indx = binary_search_closest(self.slabs, point.x, key=lambda x: x.x_pos)
        slab = self.slabs[slab_indx]
        hedge_indx = binary_search_closest(slab.hedges, point.y, key=lambda h: h.origin.y)
        hedge = slab.hedges[hedge_indx]
        return hedge

    def find_face(self, point: Point):
        hedge = self.find_hedge(point)
        current = hedge.nexthedge
        face_loop = [hedge]
        while current != hedge:
            face_loop.append(current)
            current = current.nexthedge

        verts_loop = []
        for h in face_loop:
            verts_loop.append(h.origin)

        faces = self.dcel.findpoints(verts_loop)
        return faces


def test1():
    verts = [(0, 0), (0, 3), (3, 0),
             (6, 3), (6, 0)
             ]
    el = [(0, 1), (1, 2), (2, 0),
          (2, 3), (3, 4), (4, 2)]

    dcel_g = Dcel(vl=verts, el=el)
    alg = SlabSearchAlgorithm(dcel_g)
    p1 = Point(1, 1)
    p2 = Point(5, 1)

    x_verts = [v.x for v in dcel_g.vertices]
    y_verts = [v.y for v in dcel_g.vertices]
    x_edge = [e.origin.x for e in dcel_g.hedges]
    y_edge = [e.origin.y for e in dcel_g.hedges]

    hedge1 = alg.find_hedge(p1)
    hedge2 = alg.find_hedge(p2)

    verts1 = hedge1.face.vertexlist()
    x_verts1 = [v.x for v in verts1]
    x_verts1.append(x_verts1[0])
    y_verts1 = [v.y for v in verts1]
    y_verts1.append(y_verts1[0])

    verts2 = hedge2.face.vertexlist()
    x_verts2 = [v.x for v in verts2]
    x_verts2.append(x_verts2[0])
    y_verts2 = [v.y for v in verts2]
    y_verts2.append(y_verts2[0])

    #plt.figure()
    plt.axis([-1, 8, -1, 8])
    plt.fill(x_verts1, y_verts1, 'r')

    #plt.figure()
    plt.axis([-1, 8, -1, 8])
    plt.fill(x_verts2, y_verts2, 'b')

    plt.show()


test1()
