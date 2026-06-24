fh = open("OOP/string_split()/addresses.txt")

for address in fh:
    address = address.strip()
    (lastname, firstname, city, phone) = address.split(";")
    print(firstname + " " + lastname + ", " + phone)

s = "red, green, blue, yellow, pink, brown, black, white"

for i in range(1, 8):
    x = s.split(",", i)
    print(len(x), x)

