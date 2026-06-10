from Tier import *

class Katze(Tier):
    def __init__(self, alter):
        Tier.__init__(self, alter)

    def lautgeben(self):          # jesli okreslimy funkcja dziediczona jeszcze raz...zostanie ona nadpisana 
        print("Mau, mau, miiiau")
        '''
        super().lautgeben()       # opcja umozliwiajaca zaczerpanie funkcji(tu lautgeben) z superklasy(ogolnej)
        '''
