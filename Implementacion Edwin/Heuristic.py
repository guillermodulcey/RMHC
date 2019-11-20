from abc import ABC, abstractmethod

import random as r

class Heuristic(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def recombine(self):
        pass

    @abstractmethod
    def initialization(self,longitud):
        pass
    
    @abstractmethod
    def decode(self):
        pass