''' w zbiorach set() elementy nie moga sie powtarzac(jak w funkcji)'''

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

citis_1 = frozenset(["Frankfurt", "Basel", "Freiburg"])  # tworzy nieedytowalna liste (nie mozemy nawet dodawac czy odejmowac elementow)

menge_4 = menge_3.copy()         # tworzy plaska kopie zbioru
print(menge_4)

citis_2 = citis_1.copy()
print(citis_2)

x = {"a", "b", "c", "d", "e"}
y = {"b", "c"}
z = {"c", "d"}

print(x.difference(y))                 # wyswietla roznice zbiorow x \ y
print(x.difference(y).difference(z))   # wyswietla roznice roznicy (x \ y) \ z

print(x.difference_update(y))

