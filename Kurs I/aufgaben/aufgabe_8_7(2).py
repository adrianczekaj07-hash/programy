spr_liste = []

n = 0
while sum(spr_liste) < 2.5:
    spr_liste.append(1 / 2 ** n)
    print("Die Summe der Sprünge beträgt: " + str(sum(spr_liste)))
    if n > 10000:  
        print("Bei 10.000 Sprüngen gelang es ihm nicht, die Straße zu überqueren.")
        break
    n += 1




    

