from Funcion import Funcion

import sys as s
import math as m

class Evaluador():
    def __init__(self, longitud, maximizar, funcion: Funcion):
        self.funcion = funcion
        self.longitudEntera = m.ceil(m.log2(funcion.rangoFinal-funcion.rangoInicial+1))
        self.longitud =  self.longitudEntera + longitud
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

        valor = self.obtenerValor(numero)

        return valor,self.retornarFitness(valor)

    def verificarRango(self, numero):
        if numero < self.funcion.rangoInicial or numero > self.funcion.rangoFinal:
            return False
        else:
            return True
    
    def obtenerValor(self, numero):
        return self.funcion.rangoInicial + numero

    def retornarFitness(self, valor):
        if self.verificarRango(valor):
            if self.maximizar:
                return self.funcion.funcion(valor)
            else:
                return -self.funcion.funcion(valor)
        else:
            return -s.float_info.max

