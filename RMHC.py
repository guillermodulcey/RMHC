from Individuo import Individuo
from Evaluador import Evaluador
from Funcion import Funcion

import math as m
import random as r
import copy as c

class RMHC():

    def __init__(self, semilla, probabilidad, evaluador: Evaluador):
        r.seed(semilla)

        self.probabilidad = probabilidad
        self.e = evaluador
        
        self.individuo = Individuo(self.e.longitud, semilla)
        
        self.valor, self.best = self.e.calcularFitness(self.individuo.arreglo)

    def mutar(self):
        if self.probabilidad > r.random():
            posicion = self.elegirPosicion()
            mutacion = self.individuo.mutar(posicion)
            valor, fitnessMutacion = self.e.calcularFitness(mutacion)
            if self.best <= fitnessMutacion:
                self.best = fitnessMutacion
                self.individuo.arreglo = mutacion
                self.valor = valor

    def elegirPosicion(self):
        return int(r.random() * self.individuo.longitud)

f = Funcion(-4,-1,1)
e = Evaluador(5, True, f)

for seed in range(0,100):
    x = RMHC(seed,1,e)
    for i in range(0,10000):
        x.mutar()
    print("Mejor: "+str(x.valor))
    print("valor funcion: "+str(x.best))
    print("ARREGLO: " + str(x.individuo.arreglo))