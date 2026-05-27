dict_1 = {"vorname" : "Otto", "nachname" : "Hans"} # definiujemy slownik za pomoca klamr{} oraz klucza i przypisanej mu wartosci {key : value}

print(dict_1["vorname"])                           # po wywolaniu klucza, program zwraca przypisana mu wartosc., tu("Otto")

for v in dict_1:                                   # w obu przypadkach mozemy wywolac wszystkie elementy slownika, wyswietlajac ich klucze
    print(v)
for v in dict_1.keys():
    print(v)

for v in dict_1.values():                          # mozemy za pomoca funkcji .values() wywolac elementy slownika wyswietlajac ich wartosci.
    print(v)

dict_1.update({"vorname":"William"})               # zmiana wartosci przy danym kluczu
print(dict_1["vorname"])