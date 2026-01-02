import math
from os import read
from typing import List, Tuple

class Matrix:

    def __init__(self,epsillon:float,anzahl:int):
        self.epsillon = epsillon
        self.anzahl = anzahl

    def pruefe_anwendbarkeit(self):
        pass

    def einlesen_datei(self):
        with open("input.txt") as file:
            matrixa = []
        
            groesse = int(file.readline())

            for i in range(groesse):
                zeilea: str = file.readline()
                a: list[str] = zeilea.split()
                aa = map(float,a)
                listea:list[float] = list(aa)
                matrixa.append(listea)

            zeileb: str = file.readline()
            b: list[str] = zeileb.split()
            bb = map(float,b)
            vektorb: list[float] = list(bb)

        return groesse,matrixa,vektorb

    def loese_gls(self,n,a,b):
        
        iteration = 0

        xn:list[float] = [0 for i in range(n)]

        x:list[float] = [0 for i in range(n)]

        for u in range(self.anzahl):

            for i in range(n):
                s1 = 0
                s2 = 0
                    
                #erste Summe

                for j in range(i):
                    s1 += a[i][j]*x[j]

                #zweite Summe

                for j in range(i+1,n):
                    s2 += a[i][j]*x[j]


                xn[i] = (1/a[i][i]) * (b[i]-s1-s2)

            euklid = sum(math.sqrt(((x[i]) - (xn[i]))**2) for i in range(len(x)))

            if self.epsillon > euklid and iteration != 0:
                return x,iteration+1,euklid

            for i in range(n):
                x[i] = xn[i]

            iteration += 1
        return x,iteration+1,euklid
