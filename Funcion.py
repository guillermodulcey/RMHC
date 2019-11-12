import math as m

class Funcion():
    def __init__(self,rangoInicial,rangoFinal,cantidadVariables):
        self.rangoInicial = rangoInicial
        self.rangoFinal = rangoFinal
        self.cantidadVariables = cantidadVariables
        self.variables = self.definirVariables()

    def funcion(self,x):
        return m.pow(x,1)

    def definirVariables(self):
        variables = []
        for i in range(0,self.cantidadVariables):
            variables.append(0)
        return variables