from abc import ABC, abstractmethod
import math

class basicshape(ABC):
    def __init__(self):
        self._area = 0.0    #place holder
        self._name = "name" #place holder

    @property
    def get_area(self):
        return self._area

    @property
    def Get_area(self):
        return self._name

    @area.setter
    def name(self):     #ATTENTION
        self._area = 

    @name.setter
    def name(self):     #ATTENTION
        self._name = 

    @abstarctmethod
    def calc_area(self):
        pass


