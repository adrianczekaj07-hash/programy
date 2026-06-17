from Rechne import *
class ProgrammStatisch:
    def main():
        Rechne.multiplizieren(22, 20)
        obj = Rechne()
        print(obj.addiere(33, 30))
        obj.rechne()


    def __init__(self):
        ProgrammStatisch.main()

ProgrammStatisch()

help(Rechne.addiere)  # wyswietla komentarz umieszczony przy funkcji addiere