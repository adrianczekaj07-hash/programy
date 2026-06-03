en_de = {"eins": "one", "zwei": "two", "drei": "three"}

en_de.setdefault("vier", "four")
print("Updated dictionary:", en_de)

en_de.setdefault("eins", "oneee")
print("After trying to set 'eins' again:", en_de)

en_de.setdefault("fünf")                 # tworzy klucz 'fünf' z wartością None
print("After setting 'fünf':", en_de)

