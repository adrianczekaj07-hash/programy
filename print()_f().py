'''
einkäufe = [(7, "Packung Tomaten", 3.76),
            (12, "Nudeln a 500 gr.", 1.45),
            (5, "Bio-Rindfleisch in kg",24.20)]

            
# Umtechnungfaktor Euro nach Schweizer Franken:
kurs_sfr = 1.08

for anzahl, text, preis in einkäufe:
    gesamt = anzahl * preis
    gesamt_in_sfr = gesamt * kurs_sfr
    print(anzahl, text, preis, gesamt, gesamt_in_sfr)


#  Zapis przy pomocy f-string 

name = "Jonas"
alter = 19
name_2 = "Julius"
alter_2 = 21

print(f"{name} ist {abs(alter - alter_2)} Jahre älter als {name_2}!")



print(f"Dies ist ein Python-Dictionary d = {{'a': 3, 'b': 4}}")



def volljährig(age):
    return age > 18

personen = [("Katja", 17), ("Anja", 19), ("Jonas", 19)]

for name, alter in personen:
    print(f"{name} ist {'volljährig' if volljährig(alter) else 'minderjährig'}")

'''
pi = 3.141592653
print(f"Pi hat Wert von {pi:09.3f} auf drei Dezimalstellen gerundet")