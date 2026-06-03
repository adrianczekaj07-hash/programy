liste = ["Montag", "Dienstag", "Mittwoch"] 
umgekehrt = []
# liste.reverse()                              # odwacanie porzadku listy
# liste[::-1]                                  # odwacanie porzadku listy 
umgekehrt.append(liste.pop())                  # usuwanie ostatniego elementu listy i dodawanie go do listy umgekehrt
umgekehrt.append(liste.pop())                  # usuwanie ostatniego elementu listy i dodawanie go do listy umgekehrt
umgekehrt.append(liste.pop())                  # usuwanie ostatniego elementu listy i dodawanie go do listy umgekehrt

print(umgekehrt)  
print(liste)  