class Konto:
    def __init__(self, kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp
    
    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def auszahlen(self, betrag):
        pass

        