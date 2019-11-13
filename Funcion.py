from abc import ABC, abstractmethod

class Funcion(ABC):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        self.rangoInicial = rangoInicial
        self.rangoFinal = rangoFinal
        self.cantidadVariables = cantidadVariables

    @abstractmethod
    def funcion(self,valores: list) -> float:
        pass