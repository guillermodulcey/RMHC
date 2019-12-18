from ObjectiveFunction import ObjectiveFunction
import math as m

class DeJong(ObjectiveFunction):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        super(DeJong, self).__init__(rangoInicial,rangoFinal,cantidadVariables)

    def evaluate(self,valores: list) -> float:
        resultado = 0
        for i in range(0,len(valores)+0):
            resultado += m.pow(valores[i],2)
        return resultado, True