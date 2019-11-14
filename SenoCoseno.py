from Funcion import Funcion
import math as m

class SenoCoseno(Funcion):
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        super(SenoCoseno, self).__init__(rangoInicial,rangoFinal,cantidadVariables)

    def funcion(self,valores: list) -> float:
    	return valores[0]+ valores[1]
        #return m.cos(valores[0]) + m.sin(valores[1])