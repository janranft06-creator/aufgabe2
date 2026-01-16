from pathlib import Path

class Dialog:

    def __init__(self):
        self.datei = None

    def eingabe(self):

        auswahl = input("Wollen Sie ein GLS aus einer Datei importieren, so geben Sie `importieren`ein, oder selber ein GLS eingeben, so geben Sie `eingeben` ein: ")

        if auswahl == "importieren" or auswahl == "eingeben":
            if auswahl == "importieren":
                groesse, matrixa, vektorb = self.einlesen_datei()
            if auswahl == "eingeben":
                self.schreiben_datei()


            max_iter_default = 100
            tol_default = 1e-6

            eingabe_iter = input("Maximale Iterationen (Enter = Standard): ")
            eingabe_tol = input("Genauigkeit (Enter = Standard): ")

            max_iter = int(eingabe_iter) if eingabe_iter else max_iter_default
            tol = float(eingabe_tol) if eingabe_tol else tol_default

            return groesse, matrixa, vektorb, max_iter, tol
        
        print("Die Eingabe war Fehlerhaft")

        

    
    def einlesen_datei(self):
        
        dateiname = input("\nBitte geben Sie den TXT-Dateinamen ein.\nFormat `input`, wenn Dateiname `input.txt`: ")
        datei_pfad = Path(dateiname)
    
        if not datei_pfad.exists():
            raise FileNotFoundError("Datei existiert nicht.")

        with open(datei_pfad, mode="r", encoding="utf-8") as file:
                    # 1. erste Zeile: die Größe der Matrix
                    erste_zeile = file.readline()
                    if not erste_zeile:
                        raise ValueError("Datei ist leer oder die erste Zeile fehlt.")
                    groesse = int(erste_zeile.strip())

                    # 2. N Zeilen als Matrix einlesen
                    matrixa = []
                    for _ in range(groesse):
                        zeilea = file.readline()
                        if not zeilea:
                            raise ValueError(f"Zu wenige Zeilen: erwartet {groesse}, aber Datei endete früher.")
                        # Split, float‑Umwandlung, Liste erzeugen
                        a = zeilea.strip().split()
                        listea = list(map(float, a))
                        matrixa.append(listea)

                    # 3. Letzte Zeile als Vektor einlesen
                    zeileb = file.readline()
                    if not zeileb:
                        raise ValueError("Datei enthält keinen Vektorb.")
                    b = zeileb.strip().split()
                    vektorb = list(map(float, b))

        return groesse, matrixa, vektorb




    def schreiben_datei(self):
         pass

        # filename = input("Dateiname? ")
        # file_path = Path(__file__).parent / filename

        # # Use 'with' for automatic cleanup
        # try:
        #     with open(file_path, mode="w", encoding="utf-8") as file:
        #         file.write("Dies\n")
        #         file.write("ist meine neue Datei :-)")

        # except FileNotFoundError:
        #     print(f"Error: Folder is missing.")