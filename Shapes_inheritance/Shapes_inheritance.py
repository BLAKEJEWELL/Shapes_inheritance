from abc import ABC, abstractmethod
import math
from Basicshape import basicshape
from Circle import Circle
from rectangle import rectangle
from square import square

def test():
    shapes = [
        Circle(2,2,8, "circle 1"),
        Circle(4,4,13, "circle 2"),
        rectangle(13,2, "rectangle 1"),
        rectangle(46,73, "rectangle 2"),
        square(23, "square 1")
        ]

    for a in shapes:
        print(f"{a.name} area: {a.area}")


test()