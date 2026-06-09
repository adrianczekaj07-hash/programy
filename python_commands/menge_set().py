''' w zbiorach set() elementy nie moga sie powtarzac(jak w funkcji)'''

menge_1 = set()                  # tworzymy zbior losowo uporzadkowanych elementow., tu (pusty)
print(menge_1)

menge_2 = set("Graz")            # "rozbijamy" ciag na poszczegolne elementy., tu(tekst na litery)
print(menge_2)

menge_2.add(1)                   # dodawanie elementow., tu (1)
print(menge_2)

menge_2.pop()                    # zwraca i usuwa pierwszy (losowy) element zbioru., w razie braku elementow zwraca Blad
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

print(x.difference(y))                 # wyswietla roznice zbiorow x - y
print(x.difference(y).difference(z))   # wyswietla roznice roznicy (x - y) - z


x.difference_update(y)                 # funkcja zabiera z pierwotnego zbioru (x) wszystkie elementy zbioru drugiego (y)
#  x = x - y                           # te samedzialanie
print(x)

x.discard("a")                         # usuwa element "a",gdy dostepny w zbiorze x // gdy nie, komenda nie dokonuje zadnych zmian
# x.remove("a")                        # dziala jak .discard(), ale w przypadku nieodnalezienia elementu wskazanego ("a") zwraca Blad
print(x)

a = {"a", "b", "c", "d"}
b = {"c", "d", "e", "f"}
c = {"g", "h"}
d = {"b", "c"}
e = a

print(a.intersection(b))               # wskazuje czesc wspolna zzbiorow a i b (alternatywny zapis a & b) 

print(a.union(b))                      # wskazuje sume zbiorow a i b (alternatywnie a | b)

print(a.isdisjoint(c))                 # funkcja zwraca True gdy zbiory sa rozlaczne (nie maja wspolnych elementow)
print(a.isdisjoint(b))                 # i vice versa

print(d.issubset(a))                   # zwraca True gdy zbior c zawiera sie w zbiorze a (d <= a)

print(e < a)                           # zwraca True gdy zbior d jest podzbiorem a (tu False) (a zawiera min jeden element ktorego nie zawiera e)
print(d < a)

print(a.issuperset(d))                # zwraca True gdy zbior a jest zbiorem nadrzednym wobec zbioru d (a zawiera d) (a >= d)
print(a > d)                          # istnieje conajmniej jeden element w zbiorze a ktory nie zawiera sie w zbiorze d i (d zawiera sie w a)