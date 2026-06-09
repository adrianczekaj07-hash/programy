en_de_1 = {"eins": "one", "zwei": "two", "drei": "three"}
en_de_2 = {"eins": "new one", "vier": "four", "fünf": "five", "sechs": "six"}

print("Original dictionary:", en_de_1)
print("Dictionary to update with:", en_de_2)

en_de_1.update(en_de_2)
print("Updated dictionary:", en_de_1)

''' Funkcja update() aktualizuje słownik en_de_1, dodając do niego pary klucz-wartość z en_de_2. 
Jeśli klucz już istnieje w en_de_1, jego wartość zostanie nadpisana wartością z en_de_2. 
W rezultacie otrzymujemy zaktualizowany słownik, który zawiera wszystkie unikalne klucze z obu 
słowników oraz zaktualizowane wartości dla kluczy, które występowały w obu słownikach. '''