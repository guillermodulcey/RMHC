from ObjectiveFunction import ObjectiveFunction
import math as m

class SenoCoseno(ObjectiveFunction):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        super(SenoCoseno, self).__init__(rangoInicial,rangoFinal,cantidadVariables)

    def evaluate(self,valores: list) -> float:
        resultado = 0
        resultado += 100*m.pow((valores[1]-m.pow(valores[0],2)),2) + m.pow(1-valores[0],2)
        return resultado