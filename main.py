from matrix import Matrix
from dialog import Dialog

def main():

    dialog = Dialog()

    dimension,a,b,max_iter,tol = dialog.eingabe()

    matrix = Matrix(max_iter,tol)

    if matrix.pruefe_anwendbarkeit(dimension,a,b) == True:

        x, iterationen, entfernung = matrix.loese_gls(dimension,a,b)

        beurteilung, abstand = matrix.beurteilung_loesungsvektor(dimension,a,b,x)
        print(f"\nEin näherungsweise passender Vektor x:")
        for i in range(dimension):
            print(f"x({i+1}) = {x[i]}")
        print(f"Die Anzahl der vollendeten Iterationen: {iterationen}")
        print(f"Die hinterbliebende euklidische Entfernung: {entfernung}")
        print(f"Die Berechnung war {beurteilung}, da der mittlere Abstand von b' zu b {abstand} ist.")

    else:
        print("Die Datei entsprach nicht den Vorgaben")
        return main()

if __name__ == "__main__":
    main()