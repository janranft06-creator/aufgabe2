from matrix import Matrix
from dialog import Dialog

def main():

    dialog = Dialog()

    datei = dialog.lesen()

    matrix = Matrix(epsillon=0.0005,anzahl=10)

    eingelesen = matrix.einlesen_datei()

    n = eingelesen[0]
    a = eingelesen[1]
    b = eingelesen[2]

    loesung = matrix.loese_gls(n,a,b)
    x = loesung[0]
    iterationen = loesung[1]
    entfernung = loesung[2]

    erfolg = matrix.beurteilung_erfolg(n,a,b,x)
    beurteilung = erfolg[0]
    abstand = erfolg[1]

    print(f"Ein näherungsweise passender Vektor x: {x}")
    print(f"Die Anzahl der vollendeten Iterationen: {iterationen}")
    print(f"Die hinterbliebende euklidische Entfernung: {entfernung}")
    print(f"Die Berechnung war {beurteilung}, da der mittlere Abstand von b' zu b {abstand} ist.")

if __name__ == "__main__":
    main()