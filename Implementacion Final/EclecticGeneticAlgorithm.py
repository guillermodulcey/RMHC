from Heuristic import Heuristic
from ObjectiveFunction import ObjectiveFunction

from ServicioPolinomial import ServicioPolinomial
from SenoCoseno import SenoCoseno

import random as r
import math as m
import sys as s
import numpy as np

class EclecticGeneticAlgorithm(Heuristic):
    def __init__(self, maximizar, funcion: ObjectiveFunction, pm,  pc, n):
        self.maximizar = maximizar
        self.funcion = funcion

        self.n = n
        self.pc = pc
        self.pm = pm
        self.l = 0
        self.p = [ ]

        self.valoresVariables = [ ]
        self.valoresFitness = [ ]

        self.duplicated = False

    def recombine(self,metodo: str,locus = 0, posicion = 0):
        if metodo == "MUTAR":
            bits = self.__escogerBits()
            for bit in bits:
                self.p[bit] = self.__mutar(bit,bits[bit])
        if metodo == "COMBINAR":
            individuoA = self.n+posicion
            individuoB = (2*self.n-1)-posicion
            self.p[individuoA],self.p[individuoB] = self.__cruzar(individuoA,individuoB,locus)

    def initialization(self,precision, cantidad):
        for i in range(0,cantidad):
            individuo = self.__inicializarIndividuo(precision)
            self.p.append(individuo)
        self.l = len(self.p[0])
        self.b2m = m.ceil(self.l * self.n * self.pm)

    def decode(self,p):
        valoresFitness = []
        valoresVariables = []
        for i in range(0,len(p)):
            valoresIndividuo = []
            for j in range(0,self.funcion.cantidadVariables):
                variable = self.longitudVariable * j
                valor = self.__obtenerValor(self.__decodificarValor(p[i], variable))
                valoresIndividuo.append(valor)
            valoresFitness.append(self.__retornarFitness(valoresIndividuo))
            valoresVariables.append(valoresIndividuo)
        return valoresVariables,valoresFitness

    def execute(self,precision,iteraciones,semilla):
        r.seed(semilla)
        #Inicializar
        self.initialization(precision,self.n)
        #Evaluar
        self.valoresVariables,self.valoresFitness = self.decode(self.p)
        #Ordenar
        self.__quickSort(self.valoresFitness,0,len(self.valoresFitness)-1)
        contador = 0
        while contador < iteraciones:
            self.__duplicar(self.p)
            for i in range(0,int(self.n/2)):
                aleatorio = r.random()
                if aleatorio > self.pc:
                    locus = r.randint(0,self.l-1)
                    self.recombine("COMBINAR",locus,i)
            #Mutar
            self.recombine("MUTAR")
            #Evaluar
            self.valoresVariables,self.valoresFitness = self.decode(self.p)
            #Ordenar
            self.__quickSort(self.valoresFitness,0,len(self.valoresFitness)-1)
            self.__eliminarPeores(self.p)
            contador += 1
        if(not self.maximizar):
            self.valoresFitness = self.__convert(self.valoresFitness)
        return self.valoresVariables[0], self.valoresFitness[0]

    ####### Metodos auxiliares #####
    def __cruzar(self,individuoA: str,individuoB :str,locus):
        izquierdaA = []
        medioB = []
        l_2 = m.ceil(self.l/2)
        aleatorio = r.randint(l_2,self.l-1)

        listA = list(self.p[individuoA])
        listB = list(self.p[individuoB])

        derechaA = listA[aleatorio:len(listA)]
        derechaB = listB[aleatorio:len(listB)]

        izquierdaA = listA[0:l_2-len(derechaA)+1]
        izquierdaB = listB[0:l_2-len(derechaB)+1]

        medioA = listA[len(izquierdaA):aleatorio]
        medioB = listB[len(izquierdaA):aleatorio]

        nuevoA = "".join(izquierdaA) + "".join(medioB) + "".join(derechaA)
        nuevoB = "".join(izquierdaB) + "".join(medioA) + "".join(derechaB)
        
        return nuevoA,nuevoB

    def __mutar(self,individuo,bit):
        slist = list(self.p[individuo])
        if slist[bit] == "1":
            slist[bit] = "0"
        else:
            slist[bit] = "1"
        return "".join(slist) 

    def __escogerBits(self):
        bits = { }
        for i in range(0,self.b2m):
            individuo = r.randint(0,self.n-1)
            bitIndividuo = r.randint(0,self.l-1)
            bits.update({individuo : bitIndividuo})
        return bits

    def __eliminarPeores(self,p):
            del p[self.n:2*self.n]
            del self.valoresFitness[self.n:2*self.n]
            del self.valoresVariables[self.n:2*self.n]

    def __duplicar(self,p):
             p.extend(p)

    def __inicializarIndividuo(self,precision: int):
        s = ""
        longitudEntera = self.__calcularLongitudEntera()
        self.longitudVariable = longitudEntera + precision
        longitudTotal = self.longitudVariable * self.funcion.cantidadVariables
        for i in range(0,longitudTotal):
            s += str(r.randint(0,1))
        return s

    def __calcularLongitudEntera(self):
        cantidadEnteros = self.funcion.rangoFinal - self.funcion.rangoInicial + 1
        return m.ceil(m.log2(cantidadEnteros))
    
    def __obtenerValor(self, numero):
        return self.funcion.rangoInicial + numero

    def __decodificarValor(self, s, variable):
        parteEntera = 0
        longitudEntera = self.__calcularLongitudEntera()

        contador = longitudEntera - 1
        for i in range(0 + variable,longitudEntera + variable):
            parteEntera += m.pow(2,contador) * int(s[i])
            contador -= 1
        parteDecimal = 0
        contador = 1
        for i in range(longitudEntera + variable, self.longitudVariable + variable):
            parteDecimal += m.pow(2,-contador) * int(s[i])
            contador += 1
        return parteEntera+parteDecimal
    
    def __retornarFitness(self, valores: list):
        if self.__verificarRango(valores):
            valor, valido = self.funcion.evaluate(valores)
            if self.maximizar:
                if valido:
                    return valor
            else:
                if valido:
                    return -valor
        return -s.float_info.max
    
    def __verificarRango(self, valores: list):
        enRango = True
        for i in range(0,len(valores)):
            if valores[i] < self.funcion.rangoInicial or valores[i] > self.funcion.rangoFinal:
                enRango = False
                break
        return enRango

    def __convert(self,lst): 
        lst = np.array(lst) 
        return list(-lst)

    #### quicksort ###

    def __intercambiarElemento(self, arreglo: list, izquierda, derecha):
        temporal = arreglo[izquierda]
        arreglo[izquierda] = arreglo[derecha]
        arreglo[derecha] = temporal

    def __particiones(self, arreglo: list, izquierda, derecha) -> int:
        pivote = arreglo[derecha]
        i = (izquierda - 1)
        for j in range(izquierda,derecha):
            if arreglo[j] > pivote: 
                i += 1
                self.__intercambiarElemento(arreglo,i,j)
                self.__intercambiarElemento(self.valoresVariables,i,j)
                self.__intercambiarElemento(self.p,i,j)
        self.__intercambiarElemento(arreglo,i+1,derecha)
        self.__intercambiarElemento(self.valoresVariables,i+1,derecha)
        self.__intercambiarElemento(self.p,i+1,derecha)

        return i+1
    
    def __quickSort(self, arreglo: list, izquierda, derecha):
        index = 0
        if (derecha > izquierda):
            index = self.__particiones(arreglo, izquierda, derecha)
            self.__quickSort(arreglo,izquierda,index-1)
            self.__quickSort(arreglo,index+1,derecha)
        return arreglo