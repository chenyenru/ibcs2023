from collections import namedtuple
from typing import List


Coord = namedtuple("Coord", ["x", "y"])


class Quad:
    def __init__(self, right: int, bottom: int, max_cap: int, right_end: int = 0, bottom_end: int = 0):
        # North West
        self.nw = None
        # North East
        self.ne = None
        # South West
        self.sw = None
        # South East
        self.se = None
        # Right
        self.right_start = right
        self.right_end = right_end
        self.right = right_end
        # Bottom
        self.bottom_start = bottom
        self.bottom_end = bottom_end
        self.bottom = bottom_end
        # Children Quad Tree List
        self.children: List[Coord] = []

    def divide(self, max_cap):
        """
        Divides this quad into four equal quads
        throw children to different quadrants
        """
        self.nw = Quad(right=self.right/2, right_end=self.right_end, bottom=self.bottom /
                       2, bottom_end=self.bottom_end)
        self.ne = Quad(right=self.right,
                       right_bottom=self.right/2,
                       bottom=self.bottom/2,
                       bottom_end=self.bottom)
        self.sw = Quad(right=self.right/2, bottom=self.bottom)
        self.se = Quad(right=self.right, bottom=self.bottom)
        subquads = [self.nw, self.ne, self.sw, self.se]
        for subquad in subquads:
            for d in self.children:
                if (d.x in range(subquad.right_start-1, subquad.nw.right_start)) and (d.y in range(subquad.bottom_start, subquad.bottom_end)):
                    subquad.children += self.children.pop(d)
            # return self.nw, self.ne, self.sw, self.se
            if subquad.children >
        return self

    def __len__(self):
        return len(self.children)

    def __str__(self):
        cd = [f"({c.x}, {c.y})" for c in self.children]

        return f"""Quad ({self.right}, {self.bottom}): {len(self.children)}
        {', '.join(cd)}
NW:{self.nw}
NE:{self.ne}
SW:{self.sw}
SE:{self.se}
"""


class QuadTree:
    def __init__(self, right: int, bottom: int, max_cap: int = 5):
        self._max_cap = max_cap
        self._root = Quad(right=right, bottom=bottom)

    def add(self, child: Coord):
        """
        self._max_cap
        self._root
        """
        self._root.children.append(child)
        if len(self._root) > self._max_cap:
            while len(self._root.children) > self._max_cap:
                self._root.divide()
            return self
        elif len(self._root) < self._max_cap:
            while len()
            pass
        else:
            pass

        pass

    def __str__(self):
        return str(self._root)


if __name__ == "__main__":
    qt = QuadTree(1024, 1024)

    qt.add(Coord(256, 256))
    qt.add(Coord(768, 256))
    qt.add(Coord(256, 768))
    qt.add(Coord(768, 768))
    qt.add(Coord(256, 100))
    qt.add(Coord(256, 200))
    qt.add(Coord(256, 300))
    qt.add(Coord(256, 400))
    qt.add(Coord(100, 400))
    qt.add(Coord(200, 400))
    qt.add(Coord(300, 400))
    qt.add(Coord(400, 400))
    print(qt)
    print("─" * 50)
