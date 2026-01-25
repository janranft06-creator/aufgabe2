from pathlib import Path


class Dialog:

    def __init__(self):
        self.daten_ordner = Path(__file__).resolve().parent.parent / "data"

    def eingabe(self):

        auswahl = input("\nWählen Sie `importieren` oder `eingeben`: ").strip()

        if auswahl == "importieren":
            try:
                dimension, matrixa, vektorb = self.einlesen_datei()
            except Exception as e:
                print(e)
                return self.eingabe()

        elif auswahl == "eingeben":
            dimension, matrixa, vektorb = self.schreiben_datei()

        else:
            print("\nDie Eingabe war fehlerhaft.")
            return self.eingabe()

        max_iteration_standard = 100
        toleranz_standard = 1e-6

        while True:
            eingabe_iteration = input("\nMaximale Iterationen (Enter = Standard): ").strip()
            if eingabe_iteration == "":
                max_iteration = max_iteration_standard
                break
            try:
                max_iteration = int(eingabe_iteration)
                if max_iteration <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Die Iterationen sind falsch!")

        while True:
            eingabe_toleranz = input("Genauigkeit (Enter = Standard): ").strip()
            if eingabe_toleranz == "":
                toleranz = toleranz_standard
                break
            try:
                toleranz = float(eingabe_toleranz)
                if toleranz <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Die Toleranz ist falsch!")

        return dimension, matrixa, vektorb, max_iteration, toleranz

    def einlesen_datei(self):

        dateiname = input("\nBitte geben Sie den Dateinamen ein: ").strip()
        if not dateiname.endswith(".txt"):
            dateiname += ".txt"

        datei_pfad = self.daten_ordner / dateiname

        if not datei_pfad.exists():
            raise Exception(f"\nDatei '{dateiname}' wurde im Datei-Ordner nicht gefunden.\n")

        if datei_pfad.stat().st_size == 0:
            raise Exception("\nDie Datei ist leer (0 Bytes) und kann nicht eingelesen werden.\n")

        try:
            with open(datei_pfad, mode="r", encoding="utf-8") as file:
                zeilen = [z.strip() for z in file.readlines() if z.strip()]

            if not zeilen:
                raise Exception("\nDie Datei enthält keine verwertbaren Daten.\n")

            try:
                dimension = int(zeilen[0])
                if dimension <= 0:
                    raise ValueError
            except ValueError:
                raise Exception(
                    "\nDie erste Zeile der Datei muss eine positive Ganzzahl sein "
                    "(Dimension der Matrix).\n")

            if len(zeilen) != dimension + 2:
                raise Exception("\nDie Anzahl der Zeilen passt nicht zur angegebenen Dimension.\n")

            print("\nZahlen werden getrennt durch ein Leerzeichen hintereinander eingegeben.\nGeben Sie jetzt die Matrix A ein:")

            matrixa = []
            for i in range(1, dimension + 1):
                try:
                    werte = list(map(float, zeilen[i].split()))
                except ValueError:
                    raise Exception("\nMatrix A enthält ungültige Zahlen.\n")

                if len(werte) != dimension:
                    raise Exception("\nMatrix A hat falsche Dimensionen.\n")

                matrixa.append(werte)

            try:
                vektorb = list(map(float, zeilen[-1].split()))
            except ValueError:
                raise Exception("\nVektor b enthält ungültige Zahlen.\n")

            if len(vektorb) != dimension:
                raise Exception("\nVektor b hat falsche Dimension.\n")

        except Exception as e:
            raise e

        return dimension, matrixa, vektorb

    def schreiben_datei(self):

        dateiname = input("\nSpeichern unter dem Dateinamen: ").strip()
        if not dateiname.endswith(".txt"):
            dateiname += ".txt"

        datei_pfad = self.daten_ordner / dateiname

        while True:
            eingabe = input("\nBitte geben Sie die Anzahl der Dimensionen ein: ").strip()
            if eingabe.isdigit() and int(eingabe) > 0:
                dimension = int(eingabe)
                break
            print("Ungültige Größe.")

        print("\nGeben Sie jetzt die Matrix A ein:")
        matrixa = []
        for i in range(dimension):
            while True:
                zeile = input(f"A Zeile {i + 1}: ").split()
                if len(zeile) != dimension:
                    print("Falsche Anzahl an Werten.")
                    continue
                try:
                    matrixa.append(list(map(float, zeile)))
                    break
                except ValueError:
                    print("Nur Zahlen erlaubt.")

        print("\nGeben Sie jetzt den Vektor b ein:")
        while True:
            zeile = input("b: ").split()
            if len(zeile) != dimension:
                print("Falsche Anzahl an Werten.")
                continue
            try:
                vektorb = list(map(float, zeile))
                break
            except ValueError:
                print("Nur Zahlen erlaubt.")

        with open(datei_pfad, "w", encoding="utf-8") as file:
            file.write(str(dimension) + "\n")
            for zeile in matrixa:
                file.write(" ".join(map(str, zeile)) + "\n")
            file.write(" ".join(map(str, vektorb)) + "\n")

        print(f"\nDatei '{dateiname}' wurde erfolgreich gespeichert.")

        return dimension, matrixa, vektorb
