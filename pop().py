en_de = {"eins": "one", "zwei": "two", "drei": "three"}

x = en_de.pop("zwei")
print("Popped value:", x)
print("Updated dictionary:", en_de)

y = en_de.pop("vier", "my default value")
print("Popped value for 'vier':", y)    
print("Final dictionary:", en_de)

