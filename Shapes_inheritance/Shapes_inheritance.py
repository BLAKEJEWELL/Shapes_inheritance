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

    print("---Polymorphism Check---")
    for a in shapes:
        print(f"{a.name} area: {a.area:.3f}")

    print(" \n--Getter/setter check---")
    c = shapes[1]
    print(f"{c.name} current: {c.radius} {c.area:.3f}")
    c.radius *= 3
    print(f"{c.name} tripled: {c.radius} {c.area:.3f} \n")
    
    r = shapes[3]
    print(f"{r.name} current: {r.length} {r.width} {r.area:.3f}")
    r.length *= 3
    r.width *= 3
    print(f"{r.name} tripled: {r.length} {r.width} {r.area:.3f} \n")

    s = shapes[4]
    print(f"{s.name} current: {s.side} {s.area:.3f}")
    s.side *= 3
    print(f"{s.name} tripled: {s.side} {s.area:.3f}")

test()