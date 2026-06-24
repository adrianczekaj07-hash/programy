roman_number = input("Geben Sie eine römische Zahl ein: ")

decimal = 0

roman_digits = {
    'I': 1, 
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


previus_value = 0
for char in roman_number:        
    if char in roman_digits:     
        if roman_digits[char] > previus_value:            
            decimal -= previus_value
        else:
            decimal += previus_value
    previus_value = roman_digits[char] 
decimal += previus_value

print("Ergebnis:" + str(decimal))
