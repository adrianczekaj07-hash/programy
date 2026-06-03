liste = eval(input("Liste mit positiven Zahlen eingeben: "))
n = len(liste)
i = 0
previous = None
erg = []
while i < n:
    current = liste[i]
    i += 1
    if current == previous: # sprawdza, czy aktualna liczba jest taka sama jak poprzednia
        continue            # pomija duplikaty i przechodzi do następnej iteracji
    if current <= 0:
        print("Abbruch: Nicht-positive Zahl gefunden!") 
        break               # przerywa pętlę, jeśli znajdzie liczbę niepozytywną
    erg.append(current)
    previous = current
print("Ergebnis:", erg)
