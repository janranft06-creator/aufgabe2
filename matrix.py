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

            for i in range(groesse):                            #z.b. txt:         1 2 3 4 5
                zeilea: str = file.readline()                   #                 "1 2 3 4 5"
                a: list[str] = zeilea.split()                   #                 "1","2","3","4","5"
                aa = map(float,a)                               #                  1.,2.,3.,4.,5.
                listea:list[float] = list(aa)                   #                 [1.,2.,3.,4.,5.]
                matrixa.append(listea)                          #                [[1.,2.,3.,4.,5.],[1.,2.,3.,4.,5.]]

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

    def beurteilung_erfolg(self,n,a,b,x):

        forderung = 0.05

        bn = []

        for i in range(n):
            bn.append(0)

        for i in range(n):
            for o in range(n):
                bn[i] += a[i][o] * x[o]

        abstand = sum(math.sqrt(((bn[i]) - (b[i]))**2) for i in range(n))   

        if forderung >= abstand:
                beurteilung = "erfolgreich"

        else: beurteilung = "nicht erfolgreich"

         

        return beurteilung,abstand