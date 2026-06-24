arg_in = open("aufgaben/aufgabe_12_6(1)/Namen.txt") 
arg_out = open("aufgaben/aufgabe_12_6(1)/Namen2.txt", "w") 

ausgabe = ""
for line in arg_in:
    if ausgabe:
        ausgabe += " " + line.rstrip() + "\n"
        arg_out.write(ausgabe)
        ausgabe = ""
    else:
        ausgabe = line.rstrip()

arg_in.close()
arg_out.close()       

