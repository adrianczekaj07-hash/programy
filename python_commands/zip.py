einige_buchstaben = ["a", "b", "c", "d", "e", "f"]
einige_zahlen = [5, 3, 7, 9, 11,2]

print(type(zip(einige_buchstaben, einige_zahlen)))


for t in zip(einige_buchstaben, einige_zahlen):
    print(t)


buchstaben = "abcdefghijk"
for i, b in zip(range(1, len(buchstaben) + 1), buchstaben):
    print(f"{b:s} ist der {i:1d}. Buchstabe des Alphabetes")       # {b:s} przedstawia buchst jako string (:s)
                                                                   # {i:1d} wyświetl i jako liczbę całkowitą (d = decimal)
                                                                   # 1 oznacza minimalną szerokość pola 1 znak


gerichte = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
laender = ["Italien", "Deutschland", "Spanien", "USA"]

laender_gerichte_liste = list(zip(gerichte, laender))
print(laender_gerichte_liste)


laender_gerichte_dict = dict(zip(gerichte, laender))
print(laender_gerichte_dict)









   





    