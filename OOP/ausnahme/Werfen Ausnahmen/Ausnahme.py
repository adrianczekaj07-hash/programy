class Ausnahme:
    i = 0
    def verifiziere(self):

        while True:
            try:
                geheimzahl = int(input("Bitte Geheimzahl eingeben:\n"))
                if (geheimzahl % 7 != 0):
                    self.i += 1

                else:
                    print("Zugang gestattet")
                    return
                
            except (ValueError):
                print("Nur Zahlen eingeben")
                self.i += 1

            if (self.i > 2):
                raise BaseException()
            
            if(input("Ende mit  q - weiter mit jeder anderen Taste: ")=="q"):
                break
            
