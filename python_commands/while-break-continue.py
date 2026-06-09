i = 0
while (True):
    i += 1
    print("Wert des Schleifenzählers", i)
    if i >= 5:
        break                            # przerwij skadanie ciagu
print("Schleife beendet")
j = 0
while j < 10:
    j += 1
    if ((j % 2) != 0):
        continue                         # jesli powyzszy warunek zostal spelniony ((j % 2) != 0)
    print("Wert des Schleifenzählers", j)# (reszta z dzielenia zmiennej rozna od 0) to pomijamy dalszy czesc petli-
print("Schleife beendet")                #  -tu print("Wert des Schleifenzählers", j)

 
 

