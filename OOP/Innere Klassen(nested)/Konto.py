class Konto:

    def __init__(self, kontostand, kontotyp):
        self.kontostand = kontostand
        self.kontotyp = kontotyp
        self.eigentuemer = self.Eigentuemer("Ralph")

    class Eigentuemer:
        def __init__(self, name):
            self.name = name
            
        