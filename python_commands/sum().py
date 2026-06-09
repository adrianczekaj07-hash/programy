n = 100
sum_1 = 0    # funkcja sum() liczy sumę elementów w iterowalnym obiekcie, ale tutaj używamy zmiennej sum do przechowywania sumy liczb od 1 do n
i = 1
while i <= n:  
    sum_1 += i
    print("Summe von 1 bis " + str(i) + " ist: " + str(sum_1))
    i += 1

m = 100
sum_2 = sum(range(1, m + 1))  # funkcja sum() zlicza sumę liczb od 1 do m (włącznie) i zwraca wynik
print("Summe von 1 bis " + str(m) + " ist: " + str(sum_2))

s = 100
sum_3 = s * (s + 1) // 2  # wzór na sumę liczb od 1 do s: n(n + 1) / 2, gdzie n to liczba ostatnia
print("Summe von 1 bis " + str(s) + " ist: " + str(sum_3))
