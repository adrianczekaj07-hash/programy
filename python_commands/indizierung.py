text_1 = "Hallo World"
print(text_1[0])                   # wyswietla pierwszy element (poz 0) stingu (text_1)

print(text_1[7])                   # wyswietla 8 znak tego ciagu liter (7 pozycja)

print(text_1[-1])                  # wyswietla ostatnia pozycje ciagu (text_1).,  ujemne pozycje licza znaki od tylu ciagu 
                                   # ostatni znak ciagu (poz -1), przed ostatni (poz -2) itd...
liste_1 = [42, 65, [45, 89], 88] 
print(liste_1[1])                  # wyswietla drugi element listy (poz 1)
print(liste_1[2][0])               # jako, iz trzeci element(poz 2) listy(liste_1) jest rowniez lista, to morzemy wskazac jej element skladowy (tu pierwszy element)

liste_1[0] = 43                    # dokonuje zmiany pierwszego(poz 0) elementu listy (tu z 42 na 43)
print(liste_1)

tupel_1 = (42, 65, (45, 89), 88)   # tupel nie da sie modyfikowac!!!(immutable), indeksowac pozwala sie dokladnie tak samo jak inne grupy elementow., np:
print(tupel_1[0])               