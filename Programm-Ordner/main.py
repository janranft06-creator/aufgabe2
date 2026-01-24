from matrix import Matrix
from dialog import Dialog

def main():

    dialog = Dialog()

    dimension, a_matrix, b_vektor, max_iteration, min_epsilon = dialog.eingabe()

    matrix = Matrix(max_iteration, min_epsilon)

    if matrix.pruefe_anwendbarkeit(dimension, a_matrix, b_vektor) == True:

        x_vektor, end_iteration, end_epsilon = matrix.loese_gls(dimension, a_matrix, b_vektor)

        beurteilung_ergebnis, abstand_b_b_neu = matrix.beurteilung_berechnung(dimension, a_matrix, b_vektor, x_vektor)
        print(f"\nEin näherungsweise passender Vektor x:")
        for i in range(dimension):
            print(f"x({i+1}) = {x_vektor[i]}")
        print(f"Die Anzahl der vollendeten Iterationen: {end_iteration}")
        print(f"Die hinterbliebende euklidische Entfernung: {end_epsilon}")
        print(f"Die Berechnung war {beurteilung_ergebnis}, da der mittlere Abstand von b' zu b {abstand_b_b_neu} ist.")

    else:
        print("Die Datei entsprach nicht den Vorgaben")
        return main()

if __name__ == "__main__":
    main()