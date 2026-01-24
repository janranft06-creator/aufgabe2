import math

BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

class Matrix:
        
    def __init__(self, max_iteration:int, min_epsilon:float):
        self.max_iteration = max_iteration
        self.min_epsilon = min_epsilon

    # In dieser Methode wird geprüft, ob das Verfahren anwendbar ist.     
    def pruefe_anwendbarkeit(self,dimension, a_matrix, b_vektor):

        if not type(dimension) == int:
            return False

        zaele = 0

        for i in range(dimension):

            if len(a_matrix[i]) == dimension:
                zaele += 1

        if zaele != dimension:
            print("\n Die Matrix A hat nicht die geforderte Form")
            return False
            
        if len(b_vektor) != dimension:
            print("\nDer Vektor b hat nicht die geforderte Größe")
            return False
            
        zaele = 0

        for i in range(dimension):
            if a_matrix[i][i] != 0:
                zaele += 1

        if zaele != dimension:
            print("\nEs existiert ein aii = 0")
            return False

        else:
            return True

    # In dieser Methode wird die Iterationsvorschrift angewendet.  
    def loese_gls(self,dimension,a_matrix,b_vektor):
        
        iteration = 0

        x_vektor:list[float] = [0 for i in range(dimension)]
        x_neu_vektor:list[float] = [0 for i in range(dimension)]

        for u in range(self.max_iteration):

            for i in range(dimension):
                summe_1 = 0
                summe_2 = 0
                    
                for j in range(i):
                    summe_1 += a_matrix[i][j]*x_vektor[j]

                for j in range(i+1,dimension):
                    summe_2 += a_matrix[i][j]*x_vektor[j]


                x_neu_vektor[i] = (1/a_matrix[i][i]) * (b_vektor[i]-summe_1-summe_2)

            summen_quadrat = 0

            for i in range(dimension):
                differenz = x_vektor[i] - x_neu_vektor[i]
                summen_quadrat += differenz**2

            euklidische_distanz = math.sqrt(summen_quadrat)

            iteration += 1

            if self.min_epsilon > euklidische_distanz and iteration != 0:
                return x_vektor, iteration, euklidische_distanz

            for i in range(dimension):
                x_vektor[i] = x_neu_vektor[i]

        return x_vektor,iteration,euklidische_distanz

    # In dieser Methode wird festgestellt, ob die Berechnung erfolgreich war.  
    def beurteilung_berechnung(self,dimension, a_matrix, b_vektor, x_vektor):

        epsilon_gefordert = 0.01

        b_neu_vektor = []

        for i in range(dimension):
            b_neu_vektor.append(0)

        for i in range(dimension):
            for o in range(dimension):
                b_neu_vektor[i] += a_matrix[i][o] * x_vektor[o]   

        summen_quadrat = 0

        for i in range(dimension):
            differenz = b_vektor[i] - b_neu_vektor[i]
            summen_quadrat += differenz**2

        abstand_b_b_neu = math.sqrt(summen_quadrat)

        if epsilon_gefordert >= abstand_b_b_neu:
                beurteilung_ergebnis = f"{GREEN}{BOLD}erfolgreich{RESET}"

        else:
            beurteilung_ergebnis = f"{RED}{BOLD}nicht erfolgreich{RESET}"

        return beurteilung_ergebnis, abstand_b_b_neu