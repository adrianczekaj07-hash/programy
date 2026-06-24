from Konto import *

class Programm:
    def main():
        konto = Konto(1000, "Girokonto")
        print(konto)                      # po zapytaniu o zmienna (konto) otrzymujemy adres klastra pamieci 
                                          # mozemy rownierz stworzyc funkcje klasowa oddajaca jakiekolwiek informacje 
                                          # po wywolaniu zmiennej (tu konto)

    def __init__(self):
        Programm.main()
Programm()