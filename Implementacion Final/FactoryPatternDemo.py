
from HeuristicFactory import HeuristicFactory
from FunctionFactory import FunctionFactory

import math

funciones = FunctionFactory()

#f = funciones.getHeuristic("HANSEN",0,10)
f = funciones.getHeuristic("POLINOMIO",0,50,0,"x")
#f = funciones.getHeuristic("DEJONG",-5,5,2)
#f = funciones.getHeuristic("AXISPARALLEL",-5,5,2)
#f = funciones.getHeuristic("ROTATEDHYPER",0,10,2)

hf = HeuristicFactory(f)

precision = 10
semilla = 4
iteraciones = 10

#for i in range(0,10):
#    semilla = i
print("RMHC: "+str(hf.getHeuristic("RMHC", True).execute(precision,semilla,iteraciones)))

print("----")
f = funciones.getHeuristic("POLINOMIO",0,50,0,"x+2")
hf = HeuristicFactory(f)

print("RMHC: "+str(hf.getHeuristic("RMHC", True).execute(precision,semilla,iteraciones)))

print("----")

funciones_ = FunctionFactory()
f_ = funciones_.getHeuristic("POLINOMIO",0,50,0,"x")
hf_ = HeuristicFactory(f_)

print("RMHC: "+str(hf_.getHeuristic("RMHC", True).execute(precision,semilla,iteraciones)))
#    print("ECLECTIC: "+str(hf.getHeuristic("ECLECTIC", False, 200).execute(precision,semilla,iteraciones)))
