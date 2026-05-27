a_1 = 42              # definiujemy nowa globalna zmienna ktora nie podlega zmianie wewnatrz funkcji (ausgabeFn)
def ausgabeFn():      # globalnosc zmiennej a_1 daje  mozliwosc "czerpania" jej wartosci, ale nie jej zmiane
    global a_1        # w sytuacji koniecznosci zmiennej glodalnej, mozemy ja wywolac wewnatrz funkcji komenda global., tu (global a_1) 
    a_1 += 1
    print(a_1)

ausgabeFn()
print(a_1)


ausgabeFn()           # przy karzdorazoej inicjacji funkcji (ausgabeFN()), przy urzyciu komend global, dokonuje sie zmiana wartosci zmiennej (a_1)
ausgabeFn()
print(a_1)


def rechnenFn(a_2):
    pot_1 = 3                                  # wprowadzamy lokalna zmienna (pot_1) 
    def innenFn():                             # definiowanie jednej funkcji(innenFn) wewnatrz innej funkcji(rechnenFn) nazywamy Closures (zawieranie)
        text_1 = "Das Ergebnis ist"
        print(text_1, a_2 ** pot_1 )
    innenFn()
rechnenFn(4)
rechnenFn(5)
rechnenFn(7)