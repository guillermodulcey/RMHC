from ObjectiveFunction import ObjectiveFunction
from RMHC import RMHC

class HeuristicFactory():
    def __init__(self, funcion: ObjectiveFunction):
        self.funcion = funcion

    def getHeuristic(self, nombreHeuristica, maximizar):
        if nombreHeuristica == "RMHC":
            return RMHC(maximizar,self.funcion,1)