# OOP/shapes.py

# Class - describes an object groups data and functions
# Member - parts of a class data member member method
# Method - some data or function that is part of a class
# Object or Instance - a variable fo type class

from math import pi


class Circle:
    def __init__(self, r: float):
        """
        This is a documentation string
        Constructor for a circle

        Args:
            r: the radius of the circle
        """
        self._r = r  # the underscore tells the developers that this is a private attribute, and that people shouldn't mess with it
        print(f"This is the constructor: r:{r}")

    @property  # this is an accessor that lets us read the property
    def r(self):
        return self._r

    @r.setter
    def r(self, r: float):
        if r <= 0:
            raise ValueError("radius must be > 0")
        self._r = r

    @property
    # the java way
    def circumference(self):
        return self._r * pi * 2

    @property
    def area(self):
        return self._r ** 2 * pi

    def __str__(self):
        return f"r: {self.r}\ncircumference: {self.circumference}\narea: {self.area}"

    def __gt__(self, other):
        return self._r > other._r

    def __lt__(self, other):
        return self._r < other._r

    def __eq__(self, other):
        if type(other) == Circle:
            return self._r == other._r
        if type(other) == float or type(other) == int:
            return self.area == other

        # see if other has area attribute. if not, just return False
        area = getattr(other, "area", None)
        if callable(area):
            return self.area == other.area
            if area is not None:
                return self.area == other.area
            return False


class Rectangle:
    def __init__(self, w: float, h: float):
        """
        This class creates a rectangle
        Args:
            w: width
            h: height
        """
        self._w = w
        self._h = h

        print(f"these are the constructors: width: {w}, height: {h}")

    @property
    def h(self):
        return self._h

    @property
    def w(self):
        return self._w

    @h.setter
    def h(self, h: float):
        if h <= 0:
            raise ValueError("h should be positive number")
        self._h = h

    @w.setter
    def w(self, w: float):
        if w <= 0:
            raise ValueError("w should be positive number")
        self._w = w

    @property
    def circumference(self):
        return self._w * 2 + self._h * 2

    @property
    def area(self):
        return self._w * self._h

    def __str__(self):
        return f"\nwidth: {self.w}\nheight: {self.h}\ncircumenference: {self.circumference}\narea: {self.area}"


def main():
    c = Circle(5)
    c2 = Circle(10)
    c3 = Circle(20)
    print(c3.r)  # with accessor, we can now directly access "r"

    # with __str__, we can now get important information simply by printing out c
    print(c)

    if c > c2:
        print("c is larger than c2")
    else:
        print("c2 is larger than c1")
    r = Rectangle(5, 6)
    print(r)


if __name__ == "__main__":
    main()
