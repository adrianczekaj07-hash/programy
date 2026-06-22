import random as r

r.seed()
# Funktion liefert evtl. mehrfach gleiche Zahlen - Ziehen mit Zurücklegen
def ziehung1():
    i = 0
    zahlen=[]
    while i < 6:
        zahlen.append(round(1 + (r.random()*49)))
        i = i + 1
    return zahlen
# Funktion liefert Zahlen ohne Zurücklegen
def ziehung2():
    r.seed()
    verfuegbareZahlen = list(range(1,49))
    return r.sample(verfuegbareZahlen, 6)
# Funktion liefert Zahlen ohne Zurücklegen
def ziehung3():
    i = 0
    zahlen=[]
    while i < 6:
        temp=round(1 + (r.random()*49))
        if temp in zahlen:
            continue
        zahlen.append(temp)
        i = i + 1
    return zahlen
# Testfunktion
def testrunner(zutesten, anzahl):
   counter=0
   ok = 0
   nichtok = 0
   while counter < anzahl:
       try:
          liste=zutesten()
          liste.sort()
          for i in range(0,len(liste)-1):
             assert liste[i] != liste[i + 1]
          ok+=1
       except:
           nichtok+=1
       counter+=1
   return (ok, nichtok)
print(testrunner(ziehung1,10))
print(testrunner(ziehung2,10))
print(testrunner(ziehung3,100000))
