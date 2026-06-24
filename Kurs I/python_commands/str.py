x = "************************************************************************************************************"

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

print(x)

s2 = '''Wrste Zeile
Zweite Zeile
Dritte Zeile \
und ich gehöre auch noch zur 3. Zeile'''
print(s2)

print(x)

s3 = "Eine Zeile\nund noch eine"
print(s3)

print(x)

r1 = "\nEine Zeile\nund noch eine"            
print(r1)

print(x)

r2 = r"\nEine Zeile\nund noch eine"   # literka r(badz R) przed stringiem czyni z niego raw-sring (nie podlegajacemu edycji przez 
print(r2)                             # escape komendy) ==> \nEine Zeile\nund noch eine

print(x)

print(s1.capitalize())                # Komenda .kapitalize() zmienia wszystkie litery stringu na male znaki., 
                                      # za wyjatkiem pierwszego ten zmieniony zostaje na duza liter

print(x)

print(s1.title())                     # Komenda .title() zmiwnia wszystkie poczatkowe znaki slow na durze litery a wszystkie 
                                      # kolejne znaki tego slowa na male litery

print(x)

s4 = "69023 Frankfurt"
print(s4.strip("0123456789 "))        # Komenda .strip(a) usuwa wszystkie znaki a ze stringu.
                                      # wersja tej komendy bez wspolczynnika a czysci wszystkie puste(oraz funkcyjne jak \n czy \t) znaki stringu
                                      # komendy pochodne .rstrip() i .lstrip() czyszcza znaki z lwewj i prawej strony stringu
print(x)

print(s4.center(30))                  # Komenda .center(a) centruje str na przestrzeni a znakow
print(s4.ljust(30))                   # Komenda .ljust(a) justuje str do lewej w przestrzeni a znakow
print(s4.rjust(30))                 
print(s4.zfill(30))                   # komenda .zfill(a) wypelnia zerami z przodu str na przestrzeni edycji a


