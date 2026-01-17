from matrix import Matrix
from dialog import Dialog

def main():

    dialog = Dialog()

    n,a,b,max_iter,tol = dialog.eingabe()

    matrix = Matrix(max_iter,tol)

    if matrix.pruefe_anwendbarkeit(n,a,b) == True:

        x, iterationen, entfernung = matrix.loese_gls(n,a,b)

        beurteilung, abstand = matrix.beurteilung_erfolg(n,a,b,x)

        print(f"Ein näherungsweise passender Vektor x: {x}")
        print(f"Die Anzahl der vollendeten Iterationen: {iterationen}")
        print(f"Die hinterbliebende euklidische Entfernung: {entfernung}")
        print(f"Die Berechnung war {beurteilung}, da der mittlere Abstand von b' zu b {abstand} ist.")
    else:
        print("Die Datei entsprach nicht den Vorgaben")

if __name__ == "__main__":
    main()