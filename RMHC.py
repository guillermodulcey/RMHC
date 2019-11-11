from Individuo import Individuo
from Evaluador import Evaluador

import math as m
import random as r
import copy as c

class RMHC():

    def __init__(self, longIndividuo, semilla, probabilidad, maximizar, rangoInicial, rangoFinal):
        r.seed(semilla)

        self.probabilidad = probabilidad
        self.maximizar = maximizar

        self.e = Evaluador(longIndividuo, rangoInicial, rangoFinal, maximizar)
        self.individuo = Individuo(self.e.longitud, semilla)
        
        self.valor, self.best = self.e.calcularFitness(self.individuo.arreglo)

    def mutar(self):
        if self.probabilidad > r.random():
            posicion = int(r.random() * self.individuo.longitud)
            mutacion = self.individuo.mutar(posicion)
            valor, fitnessMutacion = self.e.calcularFitness(mutacion)
            if self.best <= fitnessMutacion:
                self.best = fitnessMutacion
                self.individuo.arreglo = mutacion
                self.valor = valor

for seed in range(0,100):
    x = RMHC(5,seed,1,True,-1,6)
    for i in range(0,10000):
        x.mutar()
    print("Mejor: "+str(x.valor))
    print("valor funcion: "+str(x.best))
    print("ARREGLO: " + str(x.individuo.arreglo))