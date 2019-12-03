from ObjectiveFunction import ObjectiveFunction

import calc as calc
import math as m

class ServicioPolinomial(ObjectiveFunction):
    def __init__(self,rangoInicial,rangoFinal,expresion):
        super(ServicioPolinomial, self).__init__(rangoInicial,rangoFinal,cantidadVariables=0)
        self.expresion = expresion
        self.variables = calc.encontrarVariables(self.expresion)
        self.variables = self.__eliminarRepetidos(self.variables)
        self.cantidadVariables = len(self.variables)

    def evaluate(self,valores: list) -> float:
        variables = self.__asignarValores(self.variables, valores)
        return calc.calcularFuncion(self.expresion, variables)

    ####### Metodos auxiliares #####

    def __asignarValores(self, variables: list, valores: list):
        names = { }
        for i in range(0,len(valores)):
            names.update({variables[i] : valores[i]})
        return names

    def __eliminarRepetidos(self, variables: list):
        sinRepetir = list(dict.fromkeys(variables))
        return sinRepetir