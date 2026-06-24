from MeineAusnahme import *

class Ausnahme:
    i = 0
    def verifiziere(self):

        while True:
            try:

                geheimzahl = int(input("Butte Geheimzahl eingeben:\n"))
                if (geheimzahl != 0000):
                    self.i += 1

                else:
                    print("Zugang gestattet")
                    return
                
            except (ValueError):
                print("Nur Zahlen eingeben")
                self.i += 1

            if (self.i > 2):
                raise MeineAusnahme()
            
            if (input("Ende mit q - weitere mit jeder Taste: ") == "q"):
                break