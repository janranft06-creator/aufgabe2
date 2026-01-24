from pathlib import Path

class Dialog:

    def __init__(self):
        self.datei = None

    def eingabe(self):

        auswahl = input("\nWählen Sie `importieren` oder `eingeben`: ")

        if auswahl == "importieren" or auswahl == "eingeben":
            if auswahl == "importieren":
                result = self.einlesen_datei()
                
                if result is None:
                    print(
        "\nDie Datei konnte nicht korrekt eingelesen werden.\n\n"
        "Erwartetes Dateiformat:\n\n"
        "1. Zeile: Größe n der Matrix (Ganzzahl)\n"
        "2. Danach die Zeilen der Matrix A, mit n Elementen getrennt durch Leerzeichen\n"
        "3. Letzte Zeile: Vektor b mit n Zahlen\n\n"
        "Beispiel für n = 3:\n\n"
        "3\n"
        "1 2 3\n"
        "4 5 6\n"
        "7 8 9\n"
        "1 2 3\n\n"
        "Bitte korrigieren Sie die Datei und versuchen Sie es erneut.\n"
    )
                    return self.eingabe()
                
                groesse, matrixa, vektorb = result    
                    
            if auswahl == "eingeben":
                groesse, matrixa, vektorb = self.schreiben_datei()


            max_iteration_standard = 100
            toleranz_standard = 1e-6

            eingabe_iteration = "jaa"
            while eingabe_iteration != int:
                eingabe_iteration = int(input("\nMaximale Iterationen (Enter = Standard): "))

            eingabe_toleranz = input("Genauigkeit (Enter = Standard): ")

            max_iteration = int(eingabe_iteration) if eingabe_iteration else max_iteration_standard
            toleranz = float(eingabe_toleranz) if eingabe_toleranz else toleranz_standard

            return groesse, matrixa, vektorb, max_iteration, toleranz
        
        else:
             print("\nDie Eingabe war Fehlerhaft")
             return self.eingabe()

        

    
    def einlesen_datei(self):
        
        dateiname = input("\nBitte geben Sie den TXT-Dateinamen ein.\nFormat: Schreibe `input` oder  `input.txt`: ").strip()
    
     # falls nur "input1" eingegeben wurde -> ".txt" ergänzen
        if not dateiname.endswith(".txt"):
            dateiname = dateiname + ".txt"

        datei_pfad = Path(dateiname)

        if not datei_pfad.exists():
            print("Datei existiert nicht. Bitte überprüfen Sie, ob", datei_pfad,"richtig geschrieben ist oder existiert!")
            return self.einlesen_datei()

        try:
            with open(datei_pfad, mode="r", encoding="utf-8") as file:
                    
                    # 1. erste Zeile: die Größe der Matrix
                    groesse = int(file.readline().strip())

                    # 2. N Zeilen als Matrix einlesen
                    matrixa = []
                    for _ in range(groesse):
                        zeile = file.readline().strip().split()
                        matrixa.append(list(map(float, zeile)))

                    # 3. Letzte Zeile als Vektor einlesen
                    zeileb = file.readline().strip().split()
                    vektorb = list(map(float, zeileb))
                    
        except Exception:
            return None

        return groesse, matrixa, vektorb

    def datei_fehler(self):
        print("\nDie Datei entspricht nicht den Vorgaben und kann nicht verwendet werden.")
        print("Bitte eine andere Datei auswählen oder die Datei korrigieren.\n")


    def schreiben_datei(self):

        dateiname_schreib = input("\nBitte geben Sie den Dateinamen an (z.B. input1 oder input1.txt): ").strip()

        # falls nur "input1" eingegeben wurde -> ".txt" ergänzen
        if not dateiname_schreib.endswith(".txt"):
            dateiname_schreib = dateiname_schreib + ".txt"

        datei_pfad = Path(dateiname_schreib)

        #Größe der Matrix festlegen
        groesse = input("\nBitte geben Sie die Größe der Matrix ein (n): ").strip()
        
        if not groesse.isdigit():
            print("Ungültige Größe. Bitte schreiben sie eine Ganzzahlige Zahl.")
            return self.schreiben_datei()

        groesse = int(groesse)

        print("\nGeben Sie jetzt die Matrix A zeilenweise ein.")
        print("Pro Zeile genau", groesse, "Zahlen, getrennt durch Leerzeichen.")
        print("Beispiel:", "1 -2 3.5" if groesse == 3 else "1 -2 3.5 ...")

        matrixa = []
        
        #Schreiben der Anzahl groesse an Zeilen für die Matrix
        for i in range(groesse):
            
            while True:
                zeile = input(f"A Zeile {i+1}: ").strip()
                teile = zeile.split()

                if len(teile) != groesse:
                    print("Fehler: Bitte genau", groesse, "Werte eingeben!")
                    continue

                try:
                    listea = list(map(float, teile))
                except ValueError:
                    print("Fehler: Bitte nur Zahlen eingeben!.")
                    continue

                matrixa.append(listea)
                break
                

        print("\nGeben Sie jetzt den Vektor b ein.")
        print("Genau", groesse, "Zahlen, getrennt durch Leerzeichen.")

        while True:
            zeileb = input("b: ").strip()
            teileb = zeileb.split()

            if len(teileb) != groesse:
                print("Fehler: Bitte genau",groesse, "Zahlen eingeben!")
                continue

            try:
                vektorb = list(map(float, teileb))
            except ValueError:
                print("Fehler: Ungültige Zahl im Vektor b. Bitte erneut eingeben!")
                continue
            
            break
    
        try:
            with open(datei_pfad, mode="w", encoding="utf-8") as file:

                # 1. Größe
                file.write(str(groesse) + "\n")

                # 2. Matrix A
                for i in range(groesse):
                    zeile_out = ""
                    for j in range(groesse):
                        zeile_out = zeile_out + str(matrixa[i][j]) + " "
                    file.write(zeile_out.strip() + "\n")

                # 3. Vektor b
                zeile_out = ""
                for i in range(groesse):
                    zeile_out = zeile_out + str(vektorb[i]) + " "
                file.write(zeile_out.strip() + "\n")

            print(f"\nDatei '{dateiname_schreib}' wurde erstellt und mit Ihren Werten gefüllt.")

        except FileNotFoundError:
            print("Datei konnte nicht erstellt werden. Bitte erneut.")
            return self.schreiben_datei()

        return groesse, matrixa, vektorb