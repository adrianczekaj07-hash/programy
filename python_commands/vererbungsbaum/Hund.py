from Saeugetier import *
class Hund(Saeugetier):
    def __init__(self, alter):
        Tier.__init__(self, alter)
    
    def ballen(self):
        print("Wau")
        
