class Tier:
    anzahl = 0

    def __init__(self):
        Tier.anzahl += 1

    @classmethod
    def AnzahlTiere(cls):
        return cls.anzahl
    
