'''

korn = []
n = 0
while n <= 63:
    korn.append(2 ** n)
    n += 1


print("Sissa musste auf das Schachbrett " + str(sum(korn)) + " Körner legen:")

'''

korner = 0
zuwachs = 1

for i in range(64):
    korner += zuwachs
    zuwachs += zuwachs
print("Sissa musste auf das Schachbrett " + str(korner) + " Körner legen:")