from abc import ABC, abstractmethod

class ObjectiveFunction(ABC):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        self.rangoInicial = rangoInicial
        self.rangoFinal = rangoFinal
        self.cantidadVariables = cantidadVariables

    @abstractmethod
    def evaluate(self,valores: list) -> float:
        pass