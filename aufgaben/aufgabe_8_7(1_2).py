class RomanToIntegerConverter:
    def __init__(self):
        # Mapping von römischen Zeichen zu ihren Werten
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Erlaubte Kombinationen für Subtraktionsregeln
        self.subtraction_pairs = {
            'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }
        
    def is_valid_roman(self, roman: str) -> bool:
        """Prüft, ob die Eingabe eine gültige römische Zahl ist."""
        if not roman or not isinstance(roman, str):
            return False
            
        roman_upper = roman.upper()
        
        # 1. Nur erlaubte Zeichen?
        for char in roman_upper:
            if char not in self.roman_values:
                return False
        
        # 2. Maximale Wiederholungen prüfen (III, XXX, CCC, MMM, aber nicht IIII)
        for char in ['I', 'X', 'C', 'M']:
            if char * 4 in roman_upper:
                return False
        
        # 3. V, L, D dürfen nicht wiederholt werden
        for char in ['V', 'L', 'D']:
            if char * 2 in roman_upper:
                return False
        
        # 4. Gültige Subtraktionspaare prüfen
        invalid_patterns = ['IL', 'IC', 'ID', 'IM',
                           'VX', 'VL', 'VC', 'VD', 'VM',
                           'XD', 'XM', 'LC', 'LD', 'LM',
                           'DM']
        
        for pattern in invalid_patterns:
            if pattern in roman_upper:
                return False
        
        # 5. Prüfen, dass keine ungültigen Kombinationen auftreten
        # z.B. IVI, IXI, XLX etc.
        for i in range(len(roman_upper) - 2):
            current = roman_upper[i]
            next_char = roman_upper[i + 1]
            overnext = roman_upper[i + 2]
            
            # Prüfe auf Muster wie IXI (I vor X, dann wieder I)
            if (current in ['I', 'X', 'C'] and 
                self.roman_values[current] < self.roman_values[next_char] and
                self.roman_values[next_char] >= self.roman_values[overnext] * 10):
                return False
        
        return True
    
    def convert(self, roman: str) -> int:
        """
        Wandelt eine römische Zahl in eine natürliche Zahl um.
        Wirft ValueError bei ungültiger Eingabe.
        """
        if not self.is_valid_roman(roman):
            raise ValueError(f"'{roman}' ist keine gültige römische Zahl")
        
        roman_upper = roman.upper()
        result = 0
        i = 0
        
        while i < len(roman_upper):
            # Prüfe auf Zweier-Subtraktionen (IV, IX, XL, XC, CD, CM)
            if i + 1 < len(roman_upper):
                pair = roman_upper[i:i+2]
                if pair in self.subtraction_pairs:
                    result += self.subtraction_pairs[pair]
                    i += 2
                    continue
            
            # Normale Einzelzeichen
            result += self.roman_values[roman_upper[i]]
            i += 1
        
        return result


# Beispielverwendung
def main():
    converter = RomanToIntegerConverter()
    
    test_cases = [
        "III", "IV", "IX", "LVIII", "MCMXCIV", 
        "MMXXIII", "CDXLIV", "MCMXCIX",
        # Ungültige Beispiele
        "IIII", "VV", "IC", "XM", "VX"
    ]
    
    print("=== Test der römischen Zahlenkonvertierung ===\n")
    
    for roman in test_cases:
        try:
            number = converter.convert(roman)
            print(f"✓ {roman:10} -> {number:5} (gültig)")
        except ValueError as e: #
            print(f"✗ {roman:10} -> {e}")
    
    print("\n=== Interaktiver Modus ===")
    while True:
        user_input = input("\nGib eine römische Zahl ein (oder 'exit' zum Beenden): ").strip()
        
        if user_input.lower() == 'exit':
            print("Auf Wiedersehen!")
            break
        
        if not user_input:
            continue
            
        try:
            result = converter.convert(user_input)
            print(f"Ergebnis: {user_input.upper()} = {result}")
        except ValueError as e:
            print(f"Fehler: {e}")


if __name__ == "__main__":
    main()
    