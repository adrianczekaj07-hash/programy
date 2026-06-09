'Dies ist ein String mit eifachen Quotes'                        # morzliwe zapisy stringow w cudzyslowia:
"Mayers' Dackel heißt Waldi"
'''Er sagte "Herrn Mayers' Dackel bellt immer!"'''
s = "Ich  bin über mehrere Zielen \
definiert, genau gesagt \
drei Zeilen"
print(s)

s1 = "Ich  bin über mehrere Zielen \
definiert, \ngenau gesagt \
drei Zeilen"
print(s1)

s2 = '''Wrste Zeile
Zweite Zeile
Dritte Zeile \
und ich gehöre auch noch zur 3. Zeile'''
print(s2)

s3 = "Eine Zeile\nund noch eine"
print(s3)

r1 = "\nEine Zeile\nund noch eine"            
print(r1)

r2 = r"\nEine Zeile\nund noch eine"   # literka r(badz R) przed stringiem czyni z niego raw-sring (nie podlegajacemu edycji przez 
print(r2)                             # escape komendy) ==> \nEine Zeile\nund noch eine

