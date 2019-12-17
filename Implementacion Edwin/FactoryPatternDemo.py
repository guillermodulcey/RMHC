
from HeuristicFactory import HeuristicFactory
from FunctionFactory import FunctionFactory

import math

funciones = FunctionFactory()

#f = funciones.getHeuristic("HANSEN",0,10)
#f = funciones.getHeuristic("POLINOMIO",-1,1,0,"sqrt(c)+y")
#f = funciones.getHeuristic("DEJONG",-5,5,2)
#f = funciones.getHeuristic("AXISPARALLEL",-5,5,2)
f = funciones.getHeuristic("ROTATEDHYPER",-5,5,2)

hf = HeuristicFactory(f)

precision = 10
semilla = 4
iteraciones = 10000

for i in range(0,10):
    semilla = i
    print("RMHC: "+str(hf.getHeuristic("RMHC", False).execute(precision,semilla,iteraciones)))
    print("ECLECTIC: "+str(hf.getHeuristic("ECLECTIC", False, 200).execute(precision,semilla,iteraciones)))
