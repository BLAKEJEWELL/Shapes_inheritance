from abc import ABC, abstractmethod 
import math
from Basicshape import basicshape

class rectangle(basicshape):
    def __init__(self,l,w, n = "rectangle"):
        super().__init__(n)
        self._length = float(l)
        self._width = float(w)
        self.calc_area()

    def calc_area(self):
        self.area = self._length * self._width

    @property
    def length(self):
        return self._length
    @property
    def width(self):
        return self._width
    @length.setter
    def length(self, val):
        self._length = float(val)
        self.calc_area()
    @width.setter
    def width(self, val):
        self._width = float(val)
        self.calc_area()




