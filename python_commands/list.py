liste_1 = [3, 99, "Ein Text"]           # definiowanie listy za pomoca [] oraz elementow 
liste_2 = [42, 65, [45, 89], 88]

print(liste_1)

liste_1[0] = 98                         # mozna dowolnie zmieniac listy po zdefiniowaniu pierwotnej
print(liste_1)                          # elementy listy maja numeracja (od zerowej pozycji pierwszego elementu) ==> liste_1[0] pierwszy element
                                        # listy (liste_1)

liste_1.append(100)                     # dodajemy elementy listy
print(liste_1)

liste_1.pop(len(liste_1) - 1)           # usuwamy ostatni element listy (liste_1)., poz[-1]
print(liste_1)

liste_2.remove(88)                      # usuwa element 88 z listy
print(liste_2)

liste_1.insert(1, "Zweite Stelle")      # umieszczamy dowolny mozliwy element na wybrana pozycje listy .insert(x, y) x-pozycja w liscie, y-element listy 
print(liste_1)

print(liste_1[-1])                      # dziala jak (peek) funkcja (nie usuwa elementu po jego zidentyfikowaniu., inaczej niz (pop)!)
print(liste_1)

liste_2.extend([90, 91, 92])            # dodaje na koncu listy elementy., tu lista trzy elementowa 
print(liste_2)

liste_3 = [93, 94, 95]                  # definiujemy liste/tupel/..., ktory kolejnie mozemy dodac do innej listy
liste_2.extend(liste_3)
print(liste_2)

liste_1.extend("Me too")               # po dodaniu str zostaje on pociety na pojedyncze rejestry literowe, ktore dodane sa do konca rozszerzanej listy.
print(liste_1)

liste_2 += [96]                        # dodawanie elementow listy za pomoca operatora (+)
liste_2 = liste_2 + [97]
print(liste_2)

liste_4 = ["red", "green", "blue", "yellow", "green"]     # definiujemy liste z elementami, ktore sie powtarzaja
print(liste_4.count("green"))           # zlicza ile razy element "green" wystepuje w liscie

print(liste_4.index("green"))           # zwraca index pierwszego wystapienia elementu "green" w lisci., tu 1
print(liste_4.index("green", 2, 5))     # zwraca index pierwszego wystapienia elementu "green" w lisci, zaczynajac od pozycji 2, 
                                        # akonczac na pozycji 5., tu 4
liste_4.insert(2, "purple")             # wstawia element "purple" na pozycje 2 w liscie
print(liste_4)

liste_4.insert((len)(liste_4), "orange")# wstawia element "orange" na koniec listy, poniewaz len(liste_4) zwraca dlugosc listy, 
print(liste_4)                          # a wiec pozycje za ostatnim elementem (jak funkcja .append())


