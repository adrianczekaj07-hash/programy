a = 17
b = 0.3
c = 2
d = 0.65
var1 = 5

print(1 * 1)
print(1 + 1)
print(5 - 1)
print(4 / 2)
print(5 / 2)
print(5 // 2) # wyswietla wynik dzielenia w liczbach calkowitych
print(a % c) # wyswietna reszte z dzielenia a/c (Modulo)
print(a % b)
print(a % d)
print(a ** b) # a do potegi b (Potenz)
print(a ** c)
print("a" + "b")
print(a + 1.9)
print(1 + 3.9)
print(False + True) # False ma wartosc 0 a True 1
print(a + True)

var1 *= 2 # dokonuje operacji var1 * 2 i nadaje wynik jako nowa wartosc var
print(var1)

var1 %= 13 # dokonuje operacji var1 / 13 i nadaje reszte jako nowa wartosc var1
print(var1)

var1 **= 2 # poteguje ver1 do potegi 2 i nadaje wynik jako nowa wartosc ver1
print(var1)


print(8 != 4 + 4) # rozny (wyswietla wynik jako prawda badz falsz)
print(5 < 9) # mniejszy
print(5 >= 10) # wiekszy rowny
print(5 == 5) # rowne
print("5" == 5) # porownoje string do liczby

print((4 + 4 == 8) and (2 + 3 == 5)) # dzialania na wartosciach logicznych
print((4 + 4 == 8) and (1 + 3 == 3))
print((4 + 4 == 8) or (2 + 3 == 5))
print((4 + 4 == 7) or (2 + 3 != 5))
print(not(1 + 4 == 5)) # not jast odwroceniem wartosci (dwuwartosciowa logika)

pattern = "@"  
seq1 = "ralph_steyer@gmx.de"
print(pattern in seq1) # sprawdza czy zmienna (pattern) znajduje sie w stringu (seq1)
print(pattern not in seq1)
seq2 = "ralph_steyer@gmx.de"
print("seq1 is seq2", seq1 is seq2) # porownuje dwa stringi czy sa takie same
print("seq1 == seq2", seq1 == seq2)
z1 = [2, 4, 5]
z2 = [2, 4, 5]
print("z1 is z2", z1 is z2) # sprawdza czy te grupy danych tym samym(rezultat pokazuje, ze sa to dwa rozne obiekty) False
print("z1 == z2", z1 == z2) # sprawdza czy te grupy danych zawieraja te same tylko te same dane) True

'''
Zachodzi rownanie (Modulo X GZD (ganzzahligen Division))dla wszyskich wartosci x, y.
x = 24
y = 7

x == (x // y) * y + (x % y) 
'''





