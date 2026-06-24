arg_in = open("aufgaben/aufgabe_12_6(2)/kunst_list.txt").readlines()
arg_out = open("aufgaben/aufgabe_12_6(2)/kunst_list2.txt", "w")


ausgabe = ""
i = 0

for line in arg_in:
    i += 1
    if ausgabe:
        if i % 3 == 0:
            ausgabe += "(" + line.rstrip() + ")\n"
            arg_out.write(ausgabe)
            ausgabe = ""

        else:
            ausgabe += " " + line.rstrip() + "  "        

    else:
        ausgabe = line.rstrip()

arg_out.close()

arg = open("aufgaben/aufgabe_12_6(2)/kunst_list2.txt")

for line in arg:
    print(" " + line.rstrip() + " ")



arg.close()
