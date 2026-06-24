def lsprache(text_input,              
            set_1 = {"a", "e", "i", "o", "u", "ü", "ö", "ä"}, 
            set_2 = {"ei", "au", "ie", "eu"}, 
            fuller = "lew"):
    
    text_input = text_input.lower()
    string_output = ""

    while text_input:
        first_2 = text_input[:2]
        first_1 = text_input[0]

        if first_2 in set_2:
            string_output += first_2 + fuller + first_2
            text_input = text_input[2:]

        elif first_1 in set_1:
            string_output += first_1 + fuller + first_1
            text_input = text_input[1:]

        else:
            string_output += first_1
            text_input = text_input[1:]

    return string_output



if __name__== "__main__":
            words = ["Löffelsprache", "Donauauen", "zweieiig", "Treueeid"]
            for word in words:
                print(lsprache(word))

            print("\n Und nun mit anderer Füllsilabe: ")
            
            for word in words:
                 print(lsprache(word, fuller="lol"))



