dict_1 = {"vorname" : "Otto", "nachname" : "Hans"} # definiujemy slownik za pomoca klamr{} oraz klucza i przypisanej mu wartosci {key : value}

print(dict_1["vorname"])                           # po wywolaniu klucza, program zwraca przypisana mu wartosc., tu("Otto")

print(dict_1.get("vorname"), "Hans")               # mozemy tez uzyc funkcji .get() do wywolania wartosci przypisanej do klucza, tu("Otto")



dict_2 = dict(vorname = "Otto", nachname = "Hans") # mozemy tez zdefiniowac slownik za pomoca funkcji dict() i przypisac wartosci do kluczy za pomoca znaku rownosci
print(dict_2)
dict_2.clear()                                     # funkcja .clear() usuwa wszystkie elementy slownika, pozostawiajac go pustym
print("dict_2 nach clear(): ", dict_2) 

for v in dict_1:                                   # w obu przypadkach mozemy wywolac wszystkie elementy slownika, wyswietlajac ich klucze
    print(v)
for v in dict_1.keys():
    print(v)

for v in dict_1.values():                          # mozemy za pomoca funkcji .values() wywolac elementy slownika wyswietlajac ich wartosci.
    print(v)

dict_1.update({"vorname":"William"})               # zmiana wartosci przy danym kluczu
print(dict_1["vorname"])

''' Verschachtelte Dictionaries '''

en_de = {"eins": "one", "zwei": "two", "drei": "three"} # slownik z tlumaczeniem niemiecko-angielskim
de_fr = {"eins": "un", "zwei": "deux", "drei": "trois"} # slownik z tlumaczeniem niemiecko-francuskim
dictionary = {"en_de": en_de, "de_fr": de_fr}           # slownik zawierajacy dwa inne slowniki
print(dictionary["de_fr"]["zwei"])                      # wywolanie elementu slownika zawierajacego inny slownik, tu("deux")
print(dictionary)


einkaufs_liste = {}
artikel = None
while artikel != "":   
    artikel = input("Geben Sie einen Artikel ein (oder drücken Sie Enter zum Beenden): ")
    if artikel != "":
        preis = float(input("Geben Sie den Preis für ein: "))
        einkaufs_liste[artikel] = preis

print("Einkaufsliste: ", einkaufs_liste)

