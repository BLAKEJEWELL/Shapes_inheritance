from abc import ABC, abstractmethod #might not need this
from rectangle import rectangle
import math
from Basicshape import basicshape

class square(rectangle):
    def __init__(self, s):
        self._side = float(s)
        super().__init__(s, s)

    @property 
    def side(self):
        return self._side
    @side.setter
    def side(self, val): #ATTENTION
        self._side = val
        

    




