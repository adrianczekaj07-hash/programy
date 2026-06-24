arg = "Wir verwenden Cookies und andere Technologien, die für die Bereitstellung unserer Services und Funktionen auf der Website erforderlich sind. Weitere Informationen hierzu finden Sie in unserer"

x = arg.find("tion", 35, 100)       # komenda find(a, b, c) a jest stringiem ktorego obecnosc w pierwotnym stringu(tu arg)
print(x)                            # b startowa pozycja przeszukiwania., c koncowa pozycja (koniec przeszukiwania)
y = arg.find("Olaf")                # funkcja wraca pozycje pierwszego pojawienia sie wycinka a, 
print(y)                            # badz (-1) w razie niewystepowania wycinka a w stringu pierwotnym
                                    # analogicznie funkcja rfind() przeszukuje ona string od konca.
                                    
                                    # funkcja index() dziala tak samo jak find() (lub rindex()) zwraca ona natomiast, 
                                    # w razie niewystapienia blad(ValueError)

z = arg.count("ion", 0, 150)        # liczy ile razy wystepuje substring w zadanym przedzisle
print(z)
