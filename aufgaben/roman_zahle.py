eingegebene_zahl_dict = {}

roman_zahl = str(input("Geben Sie eine römische Zahl ein: ")).upper()

roman_zahlen = {
    "I": 1, 
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
def roman_to_arabic(str):
    for i 