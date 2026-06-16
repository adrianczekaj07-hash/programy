class Konto:

    def __str__(self):               # dodatkowa funkcja zwracajaca string zawierajacy (swoj) stan konta
        return str(self.kontostand)
    

    def __init__(self, kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp

    def einzahlen(self, betrag):
        pass

    def auszahlen(self, betrag):
        pass
