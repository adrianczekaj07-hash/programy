class Ausnahme:
    def rechne(self):
        
        try:     
            print("Eingabe Zahl 1")              
            zl_1 = int(input())
            print("Eingabe Zahl 2")
            zl_2 = int(input())
            arg = zl_1 * zl_2
            print(arg)
        except ValueError:              # musimy przewidziec rodzaj powstalego bledu
            print("Falsche Eingabe")
            return
        
        finally:                         # komend "finally:" zostaje wykonana niezaleznie czy pojawil sie blad czy nie
            print("Die finally-Aweisungen")

        print("Das kommt immer")        # ta czesc programu bedzie wykonana
                                        # niezaleznie od wczesniej powstalego bledu
'''
     Opcja try ... except wymaga od programujacego wiedzy jakiego rodzaju 
bledy moga sie pojawic przy okreslaniu zmiennej (tu zamiast liczby mozna 
wprowadzic litery(str)) i mozna je "wylaczyc"., tworzac klase sprawdzajaca 
zmienna (tu Ausnahme) zanim zostanie ona zaimplemantowana w glownym programie

'''

