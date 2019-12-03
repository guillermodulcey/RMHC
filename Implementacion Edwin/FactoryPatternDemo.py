from SenoCoseno import SenoCoseno
from ServicioPolinomial import ServicioPolinomial
from HeuristicFactory import HeuristicFactory

import math

f = ServicioPolinomial(0,2*math.pi,"x^2+y^3+cos(x)")

hf = HeuristicFactory(f)

hf.getHeuristic("RMHC", True).execute(10,100,10000)