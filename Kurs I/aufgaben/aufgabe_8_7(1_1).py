roman_digits = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def validate_roman(roman):

    if not roman:
        return False

    # Ungültige Zeichen
    for char in roman:
        if char not in roman_digits:
            return False

    # VV, LL, DD verboten
    for forbidden in ["VV", "LL", "DD"]:
        if forbidden in roman:
            return False

    # Maximal 3 Wiederholungen
    for forbidden in ["IIII", "XXXX", "CCCC", "MMMM"]:
        if forbidden in roman:
            return False

    # Erlaubte Subtraktionen
    allowed = {"IV", "IX", "XL", "XC", "CD", "CM"}

    for i in range(len(roman) - 1):

        current = roman_digits[roman[i]]
        next_value = roman_digits[roman[i + 1]]

        if current < next_value:
            pair = roman[i] + roman[i + 1]

            if pair not in allowed:
                return False

    return True


def roman_to_decimal(roman):

    decimal = 0
    previous_value = 0

    for char in reversed(roman):  # von rechts nach links

        value = roman_digits[char]

        if value < previous_value:
            decimal -= value
        else:
            decimal += value

        previous_value = value

    return decimal


roman_number = input("Geben Sie eine römische Zahl ein: ").upper()

if validate_roman(roman_number):

    decimal = roman_to_decimal(roman_number)

    if 1 <= decimal <= 3999:
        print("Dezimalzahl:", decimal)
    else:
        print("Fehler: Wert außerhalb des Bereichs 1 bis 3999")

else:
    print("Fehler: Ungültige römische Zahl")