def funktionFn(a1, b1):              # definiujemy nowa fukcje (funktionFn, ktora za karzdym razem kiedy bedzie wywolana ...
    a1 += 1                         # doda do podanego argumentu a jeden (a1 += 1), ...      
    print(a1 * b1)                   # wyda efekt w postaci wydruku wyniku dzialania (a1 * b1)
 
funktionFn(4, 5)                   # ((a1 + 1) * b1), co daje po podstawieniu ((4 + 1) * 5) = 25

var_1 = 3                       
funktionFn(var_1, 5)               # argumentowi a przypisujemy nasza zmienna (var_1) (obecnie o wartosci 3) 
                                   # zatem: ((3 + 1) * 5) = 20    
print(var_1)                       # funkcja funktionFn() jedynie urzywa zmiennej (var_1) jako zrodla(nie dokonuje zatem zmiany wartosci zmiennej)
                                   # co po wyswietleniu wartosci zmiennej var_1 staje sie oczywiste. tu (var_1 = 3)
def zitat1Fn():                    # zalorzenia takiej bezargumentowej (pustej) funkcji. sa zawsze wypelnione
    print("Jeder nur ein Kreuz")

def zitat2Fn(text):
    print(text)

zitat1Fn()
zitat2Fn("Hallo")


def rechnenFn(a2, b2 = 8):       # opcjonalny parametr (b2), w razie jego braku funkcja (rechnwnFn()) automatycznie przypisze mu wartosc 8
    print(a2 * b2)               # mozemy zatem wywolacfunkcje jedynie z jen´dnym parametrem

def multiplizierenFn(a2, *b2):   # odwolanie (*b2) oznacza, ze przywolujemy tu liste przyporzadkowana do zmiennej (b2)(mozemy wywolac funkcje z dowolna iloscia elementow)
    erg_1 = a2                    # argumentowi (arg_1) przypisujemy wartosc (a2) zadana w funcji na pierwszym miejscu
    for i in b2:                  # dla kazdego elementu zbioru (b2) dokonujemy
        erg_1 *= i                 # mnozymy (a2) czyli  nasz nowy argument (erg_1) razy wartos kolejnych wartosci argumentow listy (b2)
    print(erg_1)

rechnenFn(2)
rechnenFn(3, 4)

multiplizierenFn(3)
multiplizierenFn(3, 5)
multiplizierenFn(3, 5, 7, 11)



