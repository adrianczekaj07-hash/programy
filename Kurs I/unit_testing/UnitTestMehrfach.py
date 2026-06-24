import random as r
counter=0
ok = 0
nichtok = 0
while counter < 10:
    try:
        assert sum([1, 1, round(1 + (r.random()*2))]) == 4
        ok+=1
    except:
        nichtok+=1
    counter+=1
print("Anzahl Tests: ", counter, ", davon OK:", ok, ", davon Fehler: ", nichtok)
