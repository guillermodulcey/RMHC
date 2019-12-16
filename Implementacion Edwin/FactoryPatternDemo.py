from SenoCoseno import SenoCoseno
from ServicioPolinomial import ServicioPolinomial
from HeuristicFactory import HeuristicFactory

import math

f = ServicioPolinomial(-1,1,"sqrt(c)")

hf = HeuristicFactory(f)

precision = 10
semilla = 4
iteraciones = 10000



for i in range(0,10):
    semilla = i
    print(str(hf.getHeuristic("RMHC", True).execute(precision,semilla,iteraciones)))
    print(str(hf.getHeuristic("ECLECTIC", True).execute(precision,semilla,iteraciones)))
