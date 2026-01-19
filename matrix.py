import math

class Matrix:
        
    def __init__(self,anzahl:int,epsillon:float):
        self.anzahl = anzahl
        self.epsillon = epsillon
        
    def pruefe_anwendbarkeit(self,n,a,b):
        
        anwendbarkeit = False

        if type(n) == int:
            groesse = True
        else:
            groesse = False

        zaele = 0

        for i in range(n):

            if len(a[i]) == n:
                zaele += 1

        if zaele == n:
            matrixa = True
        else:
            matrixa = False
            print("\n Die Matrix A hat nicht die geforderte Form")
            print(a)

        if len(b) == n:
            vektorb = True
        else:
            vektorb = False
            print("\nDer Vektor b hat nicht die geforderte Größe")
            print(b)

        zaele1 = 0

        for i in range(n):
            if a[i][i] != 0:
                zaele1 += 1

        if zaele1 == n:
            diagonale = True
        else:
            diagonale = False
            print("\nEs existiert ein aii = 0")

        if groesse == True and matrixa == True and vektorb == True and diagonale == True:
            anwendbarkeit = True

        if anwendbarkeit == True:
            return True
        
        else:
            return False

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

            euklid = math.sqrt(sum(((x[i]) - (xn[i]))**2 for i in range(len(x))))

            iteration += 1

            if self.epsillon > euklid and iteration != 0:
                return x,iteration,euklid

            for i in range(n):
                x[i] = xn[i]

        return x,iteration,euklid

    def beurteilung_erfolg(self,n,a,b,x):

        forderung = 0.01

        bn = []

        for i in range(n):
            bn.append(0)

        for i in range(n):
            for o in range(n):
                bn[i] += a[i][o] * x[o]

        abstand = math.sqrt(sum(((bn[i]) - (b[i]))**2 for i in range(n)))   

        if forderung >= abstand:
                beurteilung = "erfolgreich"

        else:
            beurteilung = "nicht erfolgreich"

        return beurteilung,abstand