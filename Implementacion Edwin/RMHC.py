from Heuristic import Heuristic
from ObjectiveFunction import ObjectiveFunction

import math as m
import sys as s
import random as r

class RMHC(Heuristic):

    def __init__(self, maximizar, funcion: ObjectiveFunction, probabilidad):
        self.maximizar = maximizar
        self.longitudVariable = 0;
        self.probabilidad = probabilidad

        self.funcion = funcion

        self.best = ""
        self.valores = []

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

    def execute(self, precision, iteraciones, evaluaciones):
        for i in range(1,iteraciones):
            r.seed(i)
            self.initialization(precision)
            for j in range(1,evaluaciones):
                if self.probabilidad > r.random():
                    mutacion = self.recombine()
                    valores, fitnessMutacion = self.decode(mutacion)
                    if self.best <= fitnessMutacion:
                        self.best = fitnessMutacion
                        self.s = mutacion
                        self.valores = valores
            print("RMHC\nValores: "+str(self.valores)+"\nValor de la función: "+str(self.best)+"\nCadena: ["+str(self.s)+"]")

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
            if self.maximizar:
                return self.funcion.evaluate(valores)
            else:
                return -self.funcion.evaluate(valores)
        else:
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
