class Ausnahme:
    def rechne(self):
        while True:
            try:
                z1 = float(input("Bitte die erste Zahl eingeben:\n"))
                z2 = float(input("Bitte die zweite Zahl eingeben:\n"))
                erg = z1 / z2
                print(erg)

            except (ValueError, ZeroDivisionError) as e:  # komunikat o bledzie zapisany zostaje w zmiennej "e"
                print(e.args[0], type(e), sep="\t:\t")    # przy powstalym bedzie mozemy wywolac ktory z przewidzianych bledow ma miejsce 

            if (input("Ende mit q - weiter mit jeder anderen Taste: ")=="q"):
                break
        
        print("Ende der Berechnung")