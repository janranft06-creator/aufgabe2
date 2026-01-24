from matrix import Matrix
from dialog import Dialog

BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def main():

    dialog = Dialog()

    n,a,b,max_iter,tol = dialog.eingabe()

    matrix = Matrix(max_iter,tol)

    if matrix.pruefe_anwendbarkeit(n,a,b) == True:

        x, iterationen, entfernung = matrix.loese_gls(n,a,b)

        beurteilung, abstand = matrix.beurteilung_erfolg(n,a,b,x)
        print(f"\nEin näherungsweise passender Vektor x:")
        for i in range(n):
            print(f"x({i+1}) = {x[i]}")
        print(f"Die Anzahl der vollendeten Iterationen: {iterationen}")
        print(f"Die hinterbliebende euklidische Entfernung: {entfernung}")
        print(f"Die Berechnung war {beurteilung}, da der mittlere Abstand von b' zu b {abstand} ist.")
        if beurteilung == "nicht erfolgreich":
            print("Die Matrix hat keine Lösung")

    else:
        print("Die Datei entsprach nicht den Vorgaben")
        return main()

if __name__ == "__main__":
    main()