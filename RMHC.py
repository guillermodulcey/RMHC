from Individuo import Individuo
from Evaluador import Evaluador

import math as m
import random as r
import copy as c

class RMHC():

    def __init__(self, longitudEntera ,longIndividuo, semilla, probabilidad, maximizar, rangoInicial, rangoFinal):
        r.seed(semilla)

        self.individuo = Individuo(longIndividuo, semilla)
        self.probabilidad = probabilidad
        self.maximizar = maximizar

        self.e = Evaluador(longitudEntera,longIndividuo, rangoInicial, rangoFinal, maximizar)
        
        self.best = self.e.calcularFitness(self.individuo.arreglo)

    def mutar(self):
        if self.probabilidad > r.random():
            posicion = int(r.random() * self.individuo.longitud)
            mutacion = self.individuo.mutar(posicion)
            fitnessMutacion = self.e.calcularFitness(mutacion)
            if self.best <= fitnessMutacion:
                self.best = fitnessMutacion
                self.individuo.arreglo = mutacion

for s in range(0,100):
    x = RMHC(10,10,s,1,False,1,7)
    for i in range(0,10000):
        x.mutar()
    print("Mejor: "+str(x.e.calcularFitness(x.individuo.arreglo)))
    print("ARREGLO: " + str(x.individuo.arreglo))