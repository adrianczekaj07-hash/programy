food = ("pizza", "burger", "pasta")

dict_1 = dict.fromkeys(food) # tworzy słownik z kluczami z krotki, a wartościami None
print(dict_1)

dict_2 = dict.fromkeys(food, 0) # tworzy słownik z kluczami z krotki, a wartościami 0
print(dict_2)

dict_3 = dict.fromkeys(food, "delicious") # tworzy słownik z kluczami z krotki, a wartościami "delicious"
print(dict_3)

