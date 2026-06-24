from Konto import *

class Programm:

    def main():
        konto = Konto(100, "Girokonto")
        print(type(konto))
        print(type(5))
        Tier = type("Tier", (), {"alter": 3})
        tier = Tier()
        print(type(tier))

    def __init__(self):
        Programm.main()
Programm()

''' Klasy(class) mozna rowniez instancjowac 
dynamicznie za pomoca komendy type(), gdzie:

Nazwa klasy = type("Nazwa klasy", (Metaklasy), {nazwa wlasnosci/funkcje obiektu: dzialanie})

tu ( Tier = type("Tier", (), {"alter": 3})  )
kolejnie tworzymy obiekt dynamicznie stworzonej klasy:
tu ( tier = Tier() )

i jak widzimy przy pomocy polecenia type() (tu print(type(tier)) )
mozemy podgladnac iz nasz nowy obiekt nalezy do klasy Tier


'''
