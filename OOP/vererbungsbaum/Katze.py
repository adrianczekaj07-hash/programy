from Saeugetier import *

class Katze(Saeugetier):
    def __init__(self, alter, name):
        Tier.__init__(self, alter)
        self.__name = name
    
    def __getName(self):
        return self.__name
    
    name =property(__getName)

    def miauen(self):
        print("Miau")
        
