from SenoCoseno import SenoCoseno
from HeuristicFactory import HeuristicFactory

import math

f = SenoCoseno(0,2*math.pi,2)

hf = HeuristicFactory(f)

hf.getHeuristic("RMHC", True).execute(10,100,10000);