from Heuristic import Heuristic
from ObjectiveFunction import ObjectiveFunction

class EGA(Heuristic):
	
	def __init__(self, semilla, pm,  pc, n):
		super(DE, self).__init__(semilla)
		self.pm = pm
		self.pc = pc
		self.n = n

    def recombine(self):
        pass

    def initialization(self,longitud):
        pass
    
    def decode(self):
        pass
