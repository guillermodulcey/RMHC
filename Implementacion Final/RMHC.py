from Heuristic import Heuristic
from ObjectiveFunction import ObjectiveFunction

import math as m
import sys as s
import random as r
import copy

class RMHC(Heuristic):

    def __init__(self, maximizar, funcion: ObjectiveFunction, probabilidad):
        self.maximizar = maximizar
        self.longitudVariable = 0
        self.probabilidad = probabilidad

        self.funcion = funcion

        self.best = ""
        self.s = ""

    def recombine(self):
        posicion = self.__elegirAlAzar()
        slist = list(self.s)
        if slist[posicion] == "1":
            slist[posicion] = "0"
        else:
            slist[posicion] = "1"
        return "".join(slist) 

    def initialization(self,precision):
        self.s = ""
        longitudEntera = self.__calcularLongitudEntera()
        self.longitudVariable = longitudEntera + precision
        longitudTotal = self.longitudVariable * self.funcion.cantidadVariables
        for i in range(0,longitudTotal):
            self.s += str(r.randint(0,1))
        self.valores, self.best = self.decode(self.s)

    def decode(self,s):
        valores = []
        for i in range(0,self.funcion.cantidadVariables):
            variable = self.longitudVariable * i
            valor = self.__obtenerValor(self.__decodificarValor(s, variable))
            valores.append(valor)
        return valores,self.__retornarFitness(valores)

    def execute(self, precision, semilla, evaluaciones):
        r.seed(semilla)
        self.valores = []
        self.initialization(precision)
        for j in range(1,evaluaciones):
            if self.probabilidad > r.random():
                mutacion = self.recombine()
                valores, fitnessMutacion = self.decode(mutacion)
                if self.best <= fitnessMutacion:
                    self.best = fitnessMutacion
                    self.s = mutacion
                    self.valores = valores
        if(not self.maximizar):
            self.best = -self.best
        return self.valores, self.best

    ####### Metodos auxiliares #####

    def __elegirAlAzar(self):
        return int(r.random() * len(self.s))

    def __obtenerValor(self, numero):
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
            valor, valido = self.funcion.evaluate(valores)
            if self.maximizar:
                if valido:
                    return valor
            else:
                if valido:
                    return -valor
        return -s.float_info.max

    def __calcularLongitudEntera(self):
        cantidadEnteros = self.funcion.rangoFinal - self.funcion.rangoInicial + 1
        return m.ceil(m.log2(cantidadEnteros))

    def __decodificarValor(self, s, variable):
        parteEntera = 0
        longitudEntera = self.__calcularLongitudEntera()

        contador = longitudEntera - 1
        for i in range(0 + variable,longitudEntera + variable):
            parteEntera += m.pow(2,contador) * int(s[i])
            contador -= 1
        parteDecimal = 0
        contador = 1
        for i in range(longitudEntera + variable, self.longitudVariable + variable):
            parteDecimal += m.pow(2,-contador) * int(s[i])
            contador += 1
        return parteEntera+parteDecimal