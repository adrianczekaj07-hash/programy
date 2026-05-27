x = 42
y = x
print(id(x))   # funkcja id(x) pokazuje przypisane id obiektu (tu zmienna x)
print(id(y))   # po przypisaniu zmiennej y wartosci x uzyskuje ona te same 
               # id (odnosza sie do tego samego obiektu

print(id(x) == id(y)) # porownanie id obu obiektow wydaje wynik prawde (True)


print( x is y)  # funkcja is rownierz wskazuje czy obiekt x to obiekt y., tu rownierz (True)

