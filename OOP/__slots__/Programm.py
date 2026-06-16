from Konto import *

class Programm:

    def einzahlen(self, betrag):
        self.kontostand += betrag

    def main():

        konto = Konto(1000, "Girokonto")                      
        print("__slots__:", konto.__slots__)


    def __init__(self):
        Programm.main()
Programm()

''' 
mozemy sami zdefiniowac rejestr obiektu (__slots__ = ["kontostand", "kontotyp"])
co blokuje powstawanie dynamicznego(edytowalnego) rejestru __dict__ a jedynie 
daje nam "dostep" do apriorycznie okreslonych wlasnosci
'''