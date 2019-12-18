from Funciones.ServicioPolinomial import ServicioPolinomial
from Funciones.Hansen import Hansen
from Funciones.DeJong import DeJong
from Funciones.AxisParallel import AxisParallel
from Funciones.RotatedHyper import RotatedHyper

class FunctionFactory():
    def __init__(self):
        pass

    def getHeuristic(self, nombreFuncion, rangoInicial, rangoFinal, cantidadVariables=1, funcion="N"):
        if nombreFuncion == "HANSEN":
            return Hansen(rangoInicial,rangoFinal,2)
        if nombreFuncion == "POLINOMIO":
            return ServicioPolinomial(rangoInicial,rangoFinal,funcion)
        if nombreFuncion == "DEJONG":
            return DeJong(rangoInicial,rangoFinal,cantidadVariables)
        if nombreFuncion == "AXISPARALLEL":
            return AxisParallel(rangoInicial,rangoFinal,cantidadVariables)
        if nombreFuncion == "ROTATEDHYPER":
            return RotatedHyper(rangoInicial,rangoFinal,cantidadVariables)