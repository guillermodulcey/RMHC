from Funcion import Funcion

import sys as s
import math as m

class Evaluador():
    def __init__(self, longitudEntera, longitud, rangoInicial, rangoFinal, maximizar):
        self.longitudEntera = longitudEntera
        self.longitud = longitud
        self.rangoInicial = rangoInicial
        self.rangoFinal = rangoFinal
        self.maximizar = maximizar

    def calcularFitness(self,arreglo):
        parteEntera = 0
        contador = self.longitudEntera - 1
        for i in range(0,self.longitudEntera):
            parteEntera += m.pow(2,contador) * arreglo[i]
            contador -= 1

        parteDecimal = 0
        contador = 1
        for i in range(self.longitudEntera,self.longitud):
            parteDecimal += m.pow(2,-contador) * arreglo[i]
            contador += 1

        numero = parteEntera+parteDecimal
        
        if self.maximizar:
            if self.verificarRango(numero):
                return Funcion.funcion(numero)
            else:
                return s.float_info.min
        else:
            if self.verificarRango(numero):
                return -Funcion.funcion(numero)
            else:
                return -s.float_info.max

    def verificarRango(self, numero):
        if numero < self.rangoInicial or numero > self.rangoFinal:
            return False
        else:
            return True