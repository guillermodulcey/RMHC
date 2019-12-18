from ObjectiveFunction import ObjectiveFunction
from RMHC import RMHC
from EclecticGeneticAlgorithm import EclecticGeneticAlgorithm

class HeuristicFactory():
    def __init__(self, funcion: ObjectiveFunction):
        self.funcion = funcion

    def getHeuristic(self, nombreHeuristica, maximizar, poblacion=100, probabilidadMutacion=0.001, probabilidadCruce=0.9):
        if nombreHeuristica == "RMHC":
            probabilidadMutacion = 1
            return RMHC(maximizar,self.funcion,probabilidadMutacion)
        if nombreHeuristica == "ECLECTIC":
            return EclecticGeneticAlgorithm(maximizar, self.funcion,probabilidadMutacion, probabilidadCruce, poblacion)