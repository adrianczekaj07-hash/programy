#import math                       # uruchamia modul matematychny(bez niego python nie ma dostepu do funkcji matematycznych)
#print(dir(math))

from gettext import install
import time

import pip                        # uruchamia modul czasu, ktory pozwala nam mierzyc czas wykonywania programu        
n = 10000

start_time = time.time()           # mierzymy czas wykonywania programu, ktory jest roznica czasu po wykonaniu programu i czasu przed jego wykonaniem (start_time)
l = []                             # definiujemy pusta liste, do ktorej bedziemy dodawac elementy w petli for
for i in range(n):                 # petla for, ktora wykonuje sie n razy (od 0 do n-1), w kazdej iteracji dodajemy do listy l element i*2 (czyli podwojona wartosc i)
    # l += [i * 2]                 # dodajemy do listy l element i*2 za pomoca operatora (+), ktory tworzy nowa liste z elementami l i [i*2] i przypisuje ja do l (jest to mniej efektywne niz metoda append, poniewaz tworzy nowa liste za kazda iteracja, zamiast dodawac element do istniejącej listy)
    l.append(i * 2)                # dodajemy do listy l element i*2 za pomoca metody append, ktora dodaje element do istniejącej listy (jest to bardziej efektywne niz operator +, poniewaz nie tworzy nowej listy za kazda iteracja)
print(time.time() - start_time)    # mierzymy czas wykonywania programu, ktory jest roznica czasu po wykonaniu programu i czasu przed jego wykonaniem (start_time) i wyswietlamy go na ekranie

'''
time.sleep(1)                      # wstrzymuje wykonywanie programu na okreslony czas (w tym przypadku 1 sekunda), po czym program kontynuuje swoje dzialanie
'''
import random                      # uruchamia modul losowy, ktory pozwala nam generowac losowe liczby
m = 20 
print(random.randint(1, m))        # generuje losowa liczbe calkowita z przeym 1 i 20) i wyswietla ja na ekranie


pip install roman                  # instaluje modul roman, ktory pozwala nam konwertowac liczby rzymskie na arabskie i odwrotnie (nalezy uruchomic to polecenie w terminalu, a nie w kodzie Pythona)
import roman                       # uruchamia modul roman, ktory pozwala nam konwertowac liczby rzymskie na arabskie i odwrotnie
