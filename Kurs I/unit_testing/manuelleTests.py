import random as r

def zutesten():
   r.seed()
   return r.random()
i = 0
fehler = 0
while i < 10:
   if zutesten() > 0.9:
      fehler += 1
   i += 1

print(fehler)
