f_obj = open("text_aus_in_datei/Kochanowski.txt", "r")

for line in f_obj:
    print(line.rstrip())

f_obj.close()

