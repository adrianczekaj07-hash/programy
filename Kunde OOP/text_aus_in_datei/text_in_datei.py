fobj_in = open("text_aus_in_datei/Kochanowski.txt")
fobj_out = open("text_aus_in_datei/Kochanowski2.txt", "w")

counter = 0
for line in fobj_in:
    counter += 1
    ausgabezeile = str(counter) + " " + line.rstrip() + "\n"
    fobj_out.write(ausgabezeile)

fobj_in.close()
fobj_out.close()
