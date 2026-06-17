x = ("mp3", "Hallo", "hello", "343", "767.43")

for word in x:
    print("%6s : %s" % (word, word.isalnum()))           # komenda .isalnm() zwraca True kiedy wszystkie znaki stringu literami badz cyframi sa.

print("*", 0, 50)

for word in x:
    print("%6s : %s" % (word, word.isalpha()))
