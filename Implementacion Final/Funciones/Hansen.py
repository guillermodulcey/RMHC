from ObjectiveFunction import ObjectiveFunction
import math as m

class Hansen(ObjectiveFunction):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        super(Hansen, self).__init__(rangoInicial,rangoFinal,cantidadVariables)

    def evaluate(self,valores: list) -> float:
        resultado = 0
        for i in range(0,5):
            resultado2 = 0
            for j in range(0,5):
                resultado2 += (j+1)*m.cos((j+2)*valores[1]+j+1)
            resultado += (i+1)*m.cos(i*valores[0]+i+1)*resultado2
        return resultado, True