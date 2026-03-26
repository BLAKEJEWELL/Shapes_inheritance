from abc import ABC, abstractmethod
import math

class basicshape(ABC):
    def __init__(self, name = "shape"):
        self._area = 0.0    
        self._name = name 

    @property
    def area(self):
        return self._area
    @property
    def name(self):
        return self._name

    @area.setter
    def area(self, val):     
        self._area = val
    @name.setter
    def name(self,val):     
        self._name = val

    @abstractmethod
    def calc_area(self):
        pass


