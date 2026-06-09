a_b = "******************************************************************************************************************************************************************"

class Katze:                            # definiujemy objekt (Katze)
    name = "Herbi"                      # przypisujemy mu wlasnosci(name)
    alter = 6                           # kolejna wlasnosc obiektu (alter)
    def lautgeben(self):                # przypisujemy obiektowi jego funkcje(self), jest to funkcja bez parametru
        print("Miau")

obj = Katze()                            # przypisujemy objektowi zmienna (obj) // inicjacja obiektu
print(type(obj))                         # wywolujemy klasse objektu, tu ( zmienna nalerzy do podgrupy - zmiennych objektu(Katze))
obj.lautgeben()                          # wywolujemy funkcje objektu., tu (wydruk "Miau")
print(obj.name)                          # mozemy rowniez wylistowac konkretne wlasnosci obiektu
print(obj.alter)


print(a_b)

'''
                                          Inicjalizacja objektu w "magiczny" sposob !!!!!
'''
class Tier:
    def __init__(self, name, alter, typ):  # generujemy objekt dzialajacy(funkcja(self)) na sobiei posiadajacym trzy cechy (wlasnosci objektu)
        self.name = name
        self.alter = alter
        self.typ = typ
    def spricht(self, text):
        print(text)
    x = (2, 3, 4, 5, 7, 8, 11, 13, 15)

obje = Tier("Herby", 6, "Katze")           # inicjalizacja objektu poprzez nadanie mu konkretnych cech.
print(obje.typ)
obje.spricht("Miau")

print(a_b)

'''
                                           Wprowadzenie zmiennej prywatnej(przypisanej jedynie do obiektu)
'''
class Person:
    __alter = 42                           # zmienna prywatna (private) funkcjonuje jedynie w obrebie definicjiobjektu
    def getAlter(self):
        return self.__alter

objek = Person()
print(objek.getAlter())
print(a_b)

'''
                                                      Dziedziczenie cech objektu(Vererbung)!!!
'''
class Lebewesen:                           # (w koorelacji do subclasse to jest Superclasse)
    alter = 45

class Mensch(Lebewesen):                   # podczas definiowania objektu(Mensch), zaznaczamy z jakiego innego objektu(juz zdefiniowanego), nasz nowy objekt(Mensch) ...
    name = "Hans"                          # ... powinien dziedziczyc wlasnosci., tu (alter = 45) (subclasse)

objekt = Mensch()
print(objekt.alter, objekt.name)




