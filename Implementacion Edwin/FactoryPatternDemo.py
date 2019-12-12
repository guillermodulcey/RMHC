from SenoCoseno import SenoCoseno
from ServicioPolinomial import ServicioPolinomial
from HeuristicFactory import HeuristicFactory

import math

f = ServicioPolinomial(0,2*math.pi,"sen(x)+cos(y)")

hf = HeuristicFactory(f)

precision = 10
semilla = 2
iteraciones = 10000

null 

for i in range(0,10):
    semilla = i
    print(str(hf.getHeuristic("RMHC", False).execute(precision,semilla,iteraciones)))
    print(str(hf.getHeuristic("ECLECTIC", False, null).execute(precision,semilla,iteraciones)))
