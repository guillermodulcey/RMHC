from Funcion import Funcion

import random as r
import copy as c

class Individuo():

    def __init__(self, longitud, semilla):
        self.longitud = longitud
        self.arreglo = []

        r.seed(semilla)
        self.__generarIndividuo()

    def mutar(self,posicion):
        auxiliar = c.copy(self.arreglo)
        auxiliar[posicion] = abs(auxiliar[posicion]-1)
        return auxiliar

    def __generarIndividuo(self):
        for i in range(0,self.longitud):
            self.arreglo.append(r.randint(0,1))