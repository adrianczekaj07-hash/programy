class Roboter:

    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr

    def sage_hallo(self):
        print(f"Hallo, maine Name ist {self.name} und ich bin {2026 - int(self.baujahr)} Jahre alt ;)")

if __name__ == "__main__":      # jak ponizej! (True)

    x = Roboter("Marvin", 1979)
    y = Roboter("Caliban", 1993)
    x.sage_hallo()
    y.sage_hallo()

print(__name__)                 # przy uruchomieniu kompilatora pythona tworzony jest index (__name__ = "__main__") (czyli zmienna __name__ zawierajaca "__main__")
                                # stad (__name__ == "__main__") zwraca (True)