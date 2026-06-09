with open("text_aus_in_datei/Kochanowski.txt") as fobj_in,\
        open("text_aus_in_datei/Kochanowski2.txt", "w") as fobj_out:
        counter = 0
        for line in fobj_in:
            counter += 1
            out = str(counter) + " " + line 
            fobj_out.write(out.rstrip() + "\n")

''' alternatywny zapis

with open("text_aus_in_datei/Kochanowski.txt") as fobj_in:
    with open("text_aus_in_datei/Kochanowski2.txt", "w") as fobj_out:
        counter = 0
        for line in fobj_in:
            counter += 1
            out = str(counter) + " " + line 
            fobj_out.write(out.rstrip() + "\n")
            
'''
