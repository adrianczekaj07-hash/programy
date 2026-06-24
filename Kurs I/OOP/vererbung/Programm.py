from Katze import *

class Programm:
    def main():
        katze = Katze(1, "Susi")
        print(katze.alter)

        katze.alter = 2
        print(katze.alter)

        kater = Katze(1, "Strolch")
        print(kater.name)

    def __init__(self):
        Programm.main()

Programm()

