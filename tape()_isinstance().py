var1 = 7
print(type(var1))      # wyswietla typ zmiennej var1
var2 = "3"
print(var1 + int(var2)) # dokonuje zmiany zmiennej var2 z stringu(text) na zmienna liczbowa
print(str(var1) + var2) # dokonuje zmiany zmiennej ver1 na tekst i sklada ze zmienna var2
print(type(float(var1)))# dokonuje zmiany zmiennej na float(ulamek dziesietny) i wyswietla nowy typ

s = "Ich bin String"
print(isinstance(s, str)) # wyswietla logiczny wniosek z pytania "Czy obiekt s jest stringiem", tu (True)

x = 4
print(isinstance(x, int) or isinstance(x, float)) 

y = (89, 123, 898)

print(isinstance(y, (list, tuple)))
      


