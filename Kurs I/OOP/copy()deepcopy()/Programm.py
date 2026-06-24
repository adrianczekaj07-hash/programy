from Tier import *
from copy import *

class Programm:
    def main():
        t1 = Tier(2)
        print(t1.alter)
        
        t2 = copy(t1)
        t3 = deepcopy(t1)

        t2.alter = 3
        print(t1.alter)

        t3.alter = 4
        print(t1.alter)

    def __init__(self):
        Programm.main()
Programm()
'''
    Dzieki komendzie copy() kopiowane sa elementy ale elementy 
skladowe odnosza sie do kopiowanych elementow skladowych 
(wskazuja te same klastry pamieci) 

komenda deepcopy() tworzy nowy obiekt jak i rownierz nowe elementy 
jego skladu (np. listy i jej elementy)

'''