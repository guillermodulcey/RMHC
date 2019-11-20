from ObjectiveFunction import ObjectiveFunction
import math as m

class SenoCoseno(ObjectiveFunction):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        super(SenoCoseno, self).__init__(rangoInicial,rangoFinal,cantidadVariables)

    def evaluate(self,valores: list) -> float:
        return m.cos(valores[0]) + m.sin(valores[1])