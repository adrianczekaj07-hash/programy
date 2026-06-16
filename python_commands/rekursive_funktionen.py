def factorial(n):
    print("factorial has been called with n = " + str(n))

    if n == 1:
        print("Fertig!")
        return 1
    
    else:
        res = n * factorial(n - 1)
        print("intermediate result for ", n, " * factorial(", n - 1, "): ", res)
        return res

factorial(10)

'''
    za kazdym razem wylowywana zostaje funkcja factorial() by wyliczyc wartosc 
wczesniejszego argumentu., kolejnie gdy funkcja factorial() zwraca wartosc 1, 
kolejne funkcje zostaja "zamkniete" a w ich miejsce zostaje wstawiona wartosc 
funkcji podrzednej itd. (kaskadowo), 
az do prezentacji wartosci z ostatniej "otwartej" funkcji.

# alternatywnie mozna uzyc petli, jak ponizej:

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
print(factorial(6))

'''