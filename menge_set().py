menge_1 = set()                  # tworzymy zbior losowo uporzadkowanych elementow., tu (pusty)
print(menge_1)

menge_2 = set("Graz")            # "rozbijamy" ciag na poszczegolne elementy., tu(tekst na litery)
print(menge_2)

menge_2.add(1)                   # dodawanie elementow., tu (1)
print(menge_2)

menge_2.pop()                    # usuwa pierwszy (losowy) element zbioru
print(menge_2)

menge_2.clear()                  # oprozniamy zbior (menge_2)
print(menge_2)

menge_3 = {"Graz", "Frankfurt"}  # tworzymy zbior przez wypisanie w klamrac jego elememtow
print(menge_3)