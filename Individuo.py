from Funcion import Funcion

import random as r

class Individuo():

    def __init__(self, longitud, semilla):
        self.longitud = longitud
        self.arreglo = []

        self.__generarIndividuo()

    def mutar(self,posicion):
        self.arreglo[posicion] = abs(self.arreglo[posicion]-1)
        return self

    def __generarIndividuo(self):
        for i in range(0,self.longitud):
            self.arreglo.append(r.randint(0,1))