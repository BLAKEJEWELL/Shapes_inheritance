from abc import ABC, abstractmethod #might not need this
import math
from Basicshape import basicshape

class Circle(basicshape):
    def __init__(self,x,y,r, n = "circle"):
        super().__init__(n)
        self._x_center = float(x)
        self._y_center = float(y)
        self._radius = float(r)
        self.calc_area()

    def calc_area(self):
        self.area = math.pi * (self._radius**2)

    @property
    def x_center(self):
        return self._x_center
    @property
    def y_center(self):
        return self._y_center
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        self._radius = float(val)
        self.calc_area()


    




