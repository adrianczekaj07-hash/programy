befehl = input("Geben Sie einen Befehl ein:\nx:\t Ende\ns:\t Speichen\nd:\t Drucken\n ")
match befehl:
    case "x":                            
        print("Program verlassen.")
    case "s":
        print("Daten speichern.")
    case "d":
        print("Drucken.")
    case other:
        print("Keine Treffer.")
        
              
