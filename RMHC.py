from Individuo import Individuo
from Evaluador import Evaluador
from SenoCoseno import SenoCoseno

import math as m
import random as r
import copy as c

class RMHC():

    def __init__(self, semilla, probabilidad, evaluador: Evaluador):
        r.seed(semilla)

        self.probabilidad = probabilidad
        self.e = evaluador
        
        self.individuo = Individuo(self.e.longitudTotal, semilla)
        
        self.valor, self.best = self.e.calcularFitness(self.individuo)

    def ejecutar(self):
        if self.probabilidad > r.random():
            posicion = self.__elegirAlAzar()
            mutacion = c.deepcopy(self.individuo).mutar(posicion)
            valor, fitnessMutacion = self.e.calcularFitness(mutacion)
            if self.best <= fitnessMutacion:
                self.best = fitnessMutacion
                self.individuo = mutacion
                self.valor = valor

    def __elegirAlAzar(self):
        return int(r.random() * self.individuo.longitud)

f = SenoCoseno(0,2,2)
e = Evaluador(0, True, f)

for seed in range(0,100):
    x = RMHC(seed,1,e)
    for i in range(0,10000):
        x.ejecutar()
    print("Mejor: "+str(x.valor))
    print("valor funcion: "+str(x.best))
    print("ARREGLO: " + str(x.individuo.arreglo))