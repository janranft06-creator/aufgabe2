import math

BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

class Matrix:
        
    def __init__(self,anzahl:int,epsillon:float):
        self.anzahl = anzahl
        self.epsillon = epsillon

    # In dieser Methode wird geprüft, ob das Verfahren anwendbar ist.     
    def pruefe_anwendbarkeit(self,dimension,a,b):

        if type(dimension) == int:
            groesse = True
        else:
            groesse = False

        zaele = 0

        for i in range(dimension):

            if len(a[i]) == dimension:
                zaele += 1

        if zaele == dimension:
            matrixa = True
        else:
            matrixa = False
            print("\n Die Matrix A hat nicht die geforderte Form")
            print(a)

        if len(b) == dimension:
            vektorb = True
        else:
            vektorb = False
            print("\nDer Vektor b hat nicht die geforderte Größe")
            print(b)

        zaele1 = 0

        for i in range(dimension):
            if a[i][i] != 0:
                zaele1 += 1

        if zaele1 == dimension:
            diagonale = True
        else:
            diagonale = False
            print("\nEs existiert ein aii = 0")

        if groesse == True and matrixa == True and vektorb == True and diagonale == True:
            return True

        else:
            return False

    # In dieser Methode wird die Iterationsvorschrift angewendet.  
    def loese_gls(self,dimension,a,b):
        
        iteration = 0

        x:list[float] = [0 for i in range(dimension)]
        xn:list[float] = [0 for i in range(dimension)]

        for u in range(self.anzahl):

            for i in range(dimension):
                summe_1 = 0
                summe_2 = 0
                    
                for j in range(i):
                    summe_1 += a[i][j]*x[j]

                for j in range(i+1,dimension):
                    summe_2 += a[i][j]*x[j]


                xn[i] = (1/a[i][i]) * (b[i]-summe_1-summe_2)

            euklidische_distanz = math.sqrt(sum(((x[i]) - (xn[i]))**2 for i in range(len(x))))

            iteration += 1

            if self.epsillon > euklidische_distanz and iteration != 0:
                return x,iteration,euklidische_distanz

            for i in range(dimension):
                x[i] = xn[i]

        return x,iteration,euklidische_distanz

    # In dieser Methode wird festgestellt, ob die Berechnung erfolgreich war.  
    def beurteilung_loesungsvektor(self,dimension,a,b,x):

        forderung = 0.01

        bn = []

        for i in range(dimension):
            bn.append(0)

        for i in range(dimension):
            for o in range(dimension):
                bn[i] += a[i][o] * x[o]

        abstand = math.sqrt(sum(((bn[i]) - (b[i]))**2 for i in range(dimension)))   

        if forderung >= abstand:
                beurteilung = f"{GREEN}{BOLD}erfolgreich{RESET}"

        else:
            beurteilung = f"{RED}{BOLD}nicht erfolgreich{RESET}"

        return beurteilung,abstand