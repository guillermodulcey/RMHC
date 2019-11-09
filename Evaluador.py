from Funcion import Funcion
import math as m

class Evaluador():
    def __init__(self, longitudEntera, longitud):
        self.longitudEntera = longitudEntera
        self.longitud = longitud

    def calcularFitness(self,arreglo):
        parteEntera = 0
        for i in range(0,self.longitudEntera):
            parteEntera += m.pow(2,i) * arreglo[i]

        parteDecimal = 0
        contador = 1
        for i in range(self.longitudEntera,self.longitud):
            parteDecimal += m.pow(2,-contador) * arreglo[i]
            contador += 1

        numero = parteEntera+parteDecimal
        return numero