from pathlib import Path

class Dialog:

    def __init__(self):
        self.daten_ordner = Path(__file__).resolve().parent.parent / "Datei-Ordner"


    def eingabe(self):

        auswahl = input("\nWählen Sie `importieren` oder `eingeben`: ").strip()

        if auswahl == "importieren":
            try:
                dimension, matrixa, vektorb = self.einlesen_datei()
            except Exception as e:
                print(f"{e}")
                    
        if auswahl == "eingeben":
            dimension, matrixa, vektorb = self.schreiben_datei()

        if auswahl == "importieren" or auswahl == "eingeben":

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
                except ValueError:
                    print("Die Iterationen sind falsch!")
                    continue
            
                break
                

            while True:
                eingabe_toleranz = input("Genauigkeit (Enter = Standard): ").strip()

                if eingabe_toleranz == "":
                    toleranz = toleranz_standard
                    break

                try:
                    toleranz = float(eingabe_toleranz)
                    if toleranz <= 0:
                        raise ValueError 
                except ValueError:
                    print("Die Toleranz ist falsch!\n")
                    continue

                break   

            return dimension, matrixa, vektorb, max_iteration, toleranz
        
        else:
             print("\nDie Eingabe war Fehlerhaft")
             return self.eingabe()

        

    
    def einlesen_datei(self):
        
        # falls nur "input1" eingegeben wurde -> ".txt" ergänzen        
        dateiname = input("\nBitte geben Sie den Dateinamen ein: ").strip()

        if not dateiname.endswith(".txt"): 
            dateiname += ".txt"
            
        # Der Name wird fest mit dem "Datei-Ordner" verknüpft
        datei_pfad = self.daten_ordner / dateiname
        
        if not datei_pfad.exists():
            print(f"Datei '{dateiname}' wurde im Datei-Ordner nicht gefunden.")
            return self.einlesen_datei()

        try:
            with open(datei_pfad, mode="r", encoding="utf-8") as file:
                    
                    # 1. erste Zeile: die Größe der Matrix
                    dimension = int(file.readline().strip())

                    if dimension == 0:
                        raise Exception("\nDie Datei konnte nicht korrekt eingelesen werden.\n\n"
                        "Erwartetes Dateiformat:\n\n"
                        "1. Zeile: Dimension n der Matrix (Ganzzahl)\n"
                        "2. Danach die Zeilen der Matrix A, mit n Elementen getrennt durch Leerzeichen\n"
                        "3. Letzte Zeile: Vektor b mit n Zahlen\n\n"
                        "Beispiel für dimension = 3:\n\n"
                        "3\n"
                        "1 2 3\n"
                        "4 5 6\n"
                        "7 8 9\n"
                        "1 2 3\n\n"
                        "Bitte korrigieren Sie die Datei und versuchen Sie es erneut.\n")

                    # 2. N Zeilen als Matrix einlesen
                    matrixa = []
                    for _ in range(dimension):
                        zeile = file.readline().strip().split()
                        matrixa.append(list(map(float, zeile)))

                    # 3. Letzte Zeile als Vektor einlesen
                    zeileb = file.readline().strip().split()
                    vektorb = list(map(float, zeileb))
                    
        except Exception:
            return None

        return dimension, matrixa, vektorb

    def datei_fehler(self):
        print("\nDie Datei entspricht nicht den Vorgaben und kann nicht verwendet werden.")
        print("Bitte eine andere Datei auswählen oder die Datei korrigieren.\n")


    def schreiben_datei(self):
        # 1. Dateinamen abfragen
        dateiname = input("\nSpeichern unter dem Dateinamen: ").strip()
        if not dateiname.endswith(".txt"): 
            dateiname += ".txt"
            
        # Pfad im "Datei-Ordner" festlegen
        datei_pfad = self.daten_ordner / dateiname
        
        # 2. Dimension abfragen
        while True:
            dimension_eingabe = input("\nBitte geben Sie die Anzahl der Dimensionen ein: ").strip()
            if dimension_eingabe.isdigit():
                dimension = int(dimension_eingabe)
                break
            print("Ungültige Größe. Bitte schreiben Sie eine positive Ganzzahl.")
            
        # 3. Matrix A abfragen
        print("\nGeben Sie jetzt die Matrix A zeilenweise ein.")
        print(f"Pro Zeile genau {dimension} Zahlen, getrennt durch Leerzeichen.")
        matrixa = []
        for i in range(dimension):
            while True:
                zeile = input(f"A Zeile {i+1}: ").strip()
                teile = zeile.split()
                if len(teile) != dimension:
                    print(f"Fehler: Bitte genau {dimension} Werte eingeben!")
                    continue
                try:
                    werte = list(map(float, teile))
                    matrixa.append(werte)
                    break
                except ValueError:
                    print("Fehler: Bitte nur Zahlen eingeben!")

        # 4. Vektor b abfragen
        print("\nGeben Sie jetzt den Vektor b ein.")
        print(f"Genau {dimension} Zahlen, getrennt durch Leerzeichen.")
        while True:
            zeileb = input("b: ").strip()
            teileb = zeileb.split()
            if len(teileb) != dimension:
                print(f"Fehler: Bitte genau {dimension} Zahlen eingeben!")
                continue
            try:
                vektorb = list(map(float, teileb))
                break
            except ValueError:
                print("Fehler: Ungültige Zahl im Vektor b. Bitte erneut eingeben!")

        # 5. Datei im "Datei-Ordner" speichern
        try:
            with open(datei_pfad, mode="w", encoding="utf-8") as file:
                # Größe schreiben
                file.write(str(dimension) + "\n")
                # Matrix A schreiben
                for zeile in matrixa:
                    zeile_string = " ".join(map(str, zeile))
                    file.write(zeile_string + "\n")
                # Vektor b schreiben
                vektor_string = " ".join(map(str, vektorb))
                file.write(vektor_string + "\n")
                
            print(f"\nDatei '{dateiname}' wurde erfolgreich im Datei-Ordner erstellt.")
        except Exception as e:
            print(f"Fehler beim Speichern der Datei: {e}")
            return self.schreiben_datei()

        return dimension, matrixa, vektorb