import random as r
r.seed()
# Funktion liefert evtl. mehrfach gleiche Zahlen - Ziehen mit Zurücklegen
def ziehung():
    i = 0
    zahlen=[]
    while i < 6:
        zahlen.append(round(1 + (r.random()*49)))
        i = i + 1
    return zahlen
counter=0
ok = 0
nichtok = 0
while counter < 10:
    try:
        liste = ziehung()
        # Testausgabe Liste mit Lottozahlen
        #print(liste)
        liste.sort()
        for i in range(0,len(liste)-1):
            assert liste[i] != liste[i + 1]
        print(liste)
        ok+=1
    except:
        nichtok+=1
        # Testausgabe Liste mit Lottozahlen
        print(liste, "Zahlen mehrfach")
    counter+=1
print("Anzahl Tests: ", counter, ", davon OK:", ok, ", davon Fehler: ", nichtok)
