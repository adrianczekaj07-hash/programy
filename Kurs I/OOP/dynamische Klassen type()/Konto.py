class Konto:

    __slots__ = ["kontostand", "kontotyp"]

    def __init__(self, kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp