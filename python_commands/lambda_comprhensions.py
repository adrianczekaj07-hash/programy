lbd_1 = lambda x : x * x                    # definiujemy prosta funkcje lambda, gdzie kazdemu x-wi przyporzadkowana jest jego wartosc f(x)=x^2 (x kwadrat)
print(lbd_1(2))

x = (2, 3, 4, 5, 7, 8, 11, 13, 15)          # generujemy elementy za pomoca funkcji l i argumentow wylistowanych wtupel x.
l = lambda x : x % 2
for i in x:
    print(l(i))

numbers_1 = (2, 3, 4, 5, 7, 8, 11, 13, 15)  # mozemy generowac w ten sposob listy (jak tu) czy zbiory (jak ponizej)
squares_1 = [n % 2 for n in numbers_1]
print(squares_1)

numbers_2 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
unique_numbers = {n for n in numbers_2}    # kazdemu elementowi listy (numbers_2) przypada jego wartosc (generujemy zbior wartosci)
print(unique_numbers)

names_1 = ["Florian", "Felix", "Ralph", "Andrea"]
name_lenghts = {names_1: len(names_1) for names_1 in names_1} # generujemy slownik, gdzie kazdemu elementowi listy(names_1) przyporzadkowana jest wielkosc (dlugosc samych imion)
print(name_lenghts)