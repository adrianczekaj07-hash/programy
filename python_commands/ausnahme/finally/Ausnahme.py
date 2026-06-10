class Ausnahme:
    def rechne(self):
        while True:
            try:     
                print("Eingabe Zahl 1")              
                zl_1 = int(input())
                print("Eingabe Zahl 2")
                zl_2 = int(input())
                arg = zl_1 / zl_2
                print(arg)
            
            except ValueError:              
                print("Bitte nur Zahl eingeben")
                            
            except ZeroDivisionError:
                print("Die zweite Zahl darf nicht Null sein")

            if (input("Ende mit q - weiter mit jeder anderen Taste: ") == "q"):
                break

            
        print("Ende der Berechnungen")        
                                        