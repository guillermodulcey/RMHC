from ObjectiveFunction import ObjectiveFunction
import math as m

class RotatedHyper(ObjectiveFunction):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        super(RotatedHyper, self).__init__(rangoInicial,rangoFinal,cantidadVariables)

    def evaluate(self,valores: list) -> float:
        resultado = 0
        resultado2 = 0
        for i in range(0,len(valores)):
            for j in range(0,i):
                resultado2 += valores[j]
            resultado += m.pow(resultado2,2)
        return resultado, True