from Funcion import Funcion
from Individuo import Individuo

import sys as s
import math as m

class Evaluador():
    def __init__(self, longitud, maximizar, funcion: Funcion):
        self.funcion = funcion
        self.longitudEntera = self.__calcularLongitudEntera()
        self.longitud =  self.longitudEntera + longitud
        self.longitudTotal = self.longitud * self.funcion.cantidadVariables
        self.maximizar = maximizar

    def calcularFitness(self,arreglo: Individuo):
        valores = []
        for i in range(0,self.funcion.cantidadVariables):
            variable = self.longitud * i
            valor = self.obtenerValor(self.__decodificarValor(arreglo,variable))
            valores.append(valor)
        return valores,self.__retornarFitness(valores)

    def obtenerValor(self, numero):
        return self.funcion.rangoInicial + numero

    def __verificarRango(self, valores: list):
        enRango = True
        for i in range(0,len(valores)):
            if valores[i] < self.funcion.rangoInicial or valores[i] > self.funcion.rangoFinal:
                enRango = False
                break
        return enRango

    def __retornarFitness(self, valores: list):
        if self.__verificarRango(valores):
            if self.maximizar:
                return self.funcion.funcion(valores)
            else:
                return -self.funcion.funcion(valores)
        else:
            return -s.float_info.max

    def __calcularLongitudEntera(self):
        cantidadEnteros = self.funcion.rangoFinal - self.funcion.rangoInicial + 1
        return m.ceil(m.log2(cantidadEnteros))

    def __decodificarValor(self, arreglo: Individuo, variable):
        parteEntera = 0
        contador = self.longitudEntera - 1
        for i in range(0 + variable,self.longitudEntera + variable):
            parteEntera += m.pow(2,contador) * arreglo.arreglo[i]
            contador -= 1
        parteDecimal = 0
        contador = 1
        for i in range(self.longitudEntera + variable,self.longitud + variable):
            parteDecimal += m.pow(2,-contador) * arreglo.arreglo[i]
            contador += 1
        return parteEntera+parteDecimal

