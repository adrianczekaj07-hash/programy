name = input("Gib dein Nachname ein ")
vorname = "Adrian"
alter = 45
print(name, vorname, alter, sep = "-")      # opcja (sep =) pozwala okreslic dokladnie separatora miedzy stringami
#        name-vorname-alter
for i in range(4):
    print(i, end = " ")                     # opcja (end =) pozwala umieszczac znak (.,-), skok (\n, \t...) czy symbol po karzdym wyswietlanym elemencie
#          0 1 2 3 
''' 

# Zapis komenda print() w pliku tekstowym

fh = open("daten.txt", "w")
print("42 ist die Antwort, aber was ist die Frage?", file = fh)
fh.close()

'''

'''
Zapis bledow kompilatora w kanale bladow czy do pliku:

import sys   # Ausgabe in Standartfehlerkanal

print("Error: 42", file=sys.stderr)

'''