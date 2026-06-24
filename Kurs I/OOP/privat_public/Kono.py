class Konto:
    def __init__(self, kontostand, kontotyp):
        self.__kontostand = kontostand
        self.__kontotyp = kontotyp
    
    def einzahlen(self, betrag):
        self.__kontostand = self.__kontostand + betrag

    def auszahlung(self, betrag):
        self.__kontostand = self.__kontostand - betrag

    def getKontostand(self):
        return self.__kontostand
    
   
    @property                      # alternatywny zapis tej metody { kontostand = property(getKontostand) }
    def kontostand(self):
        return self.__kontostand
    


''' (__kontostand) poprzes (__) podwojny podkreslnik przed zmienna ustanawiamy
ja privat, przez co nie mozemy bezposrednio jej zmieniac czy wywolywac., musimy do tego uzyc 
komend getFunkcja() (zwraca wartosc prywatnej zmiennej),
czy setFunkcja() (nadaje zawartej jej prywatnej zmiennej wartosc) '''

