from Kunde import *
from Kono import *
class Programm:
    def main():
        konto_1 = Konto(1000, "Girokonto")
        kunde_1 = Kunde("Hans", "Dampf", 42, "Man", "Milchstrasse 125, 777 Irgendwo", konto_1)
        print("Kontostand bei Beginn:\t", kunde_1.konto.kontostand) # dziala dieki zastosowaniu komendy property()
        kunde_1.konto.einzahlen(123)
        print("Neuer Kontostand:\t", kunde_1.konto.getKontostand())

    
    def __init__(self):
        Programm.main()

Programm()

