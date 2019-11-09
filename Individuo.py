from Funcion import Funcion

import random as r
import copy as c

class Individuo():

    def __init__(self, longitud, semilla):
        self.longitud = longitud

        self.arreglo = []

        r.seed(semilla)
        for i in range(0,longitud):
            self.arreglo.append(r.randint(0,1))

    def mutar(self,posicion):
        auxiliar = c.copy(self.arreglo)
        if auxiliar[posicion] == 0:
            auxiliar[posicion] = 1
        else:
            auxiliar[posicion] = 0
        return auxiliar