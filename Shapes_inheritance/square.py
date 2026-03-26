from abc import ABC, abstractmethod #might not need this
from rectangle import rectangle
import math
from Basicshape import basicshape

class square(rectangle):
    def __init__(self, s, n = "square"):
        super().__init__(s, s, n)
        self._side = float(s)
        self.name = n

    @property 
    def side(self):
        return self._side
    @side.setter
    def side(self, s): #ATTENTION
        self._side = float(s)
        self._length = float(s)
        self._width = float(s)
        self.calc_area()
        

    




