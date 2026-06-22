fibo_liste = [0, 1]
fibo_zahl = 0

i = 0
while i < 20:
    fibo_zahl = fibo_liste[-1] + fibo_liste[-2]
    fibo_liste.append(fibo_zahl)
    i += 1

print(fibo_liste)