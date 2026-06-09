from math import remainder 


tuple_1 = (3, 99, "Ein Text")                 # definiowanie (Tupel) (nieedytowalnej listy elementow)(immutable)
tuple_2 = (42, 65, 45, 89, 88, 75, 46)
tuple_3 = 12, 35, "können die runden Klammern weggelassen werden"
tuple_4 = ("Mo", "Do", "Mi", "Do", "Fr", "Sa","So")
tuple_5 = ((1, 2), (3, 4))

print(tuple_1)
print(tuple_2)
print(tuple_3)

print(1 in tuple_5)                           # jeedynka nie jest elementem tuple_5 stad (False)., skladnikami tuple_5 sa dwa elementy (1, 2) i (3, 4)
print("o" in tuple_4)                         # "o" jest elementem elementu tuple_4 stad (False)

print(tuple_5[0][1])                          # czytamy od tylu., wywolujemy drugi element poz[1] z pierwszego elementu poz[0] tuple_5
print(tuple_4[1][1])                          # bedzie to druga pozycja, drugiegoelementu zbioru tuple_4(string "Do" da sie podzielic na dwie litery)
print(tuple_1[2][1:5])                        # morzemy wywolac caly zakres., tu (element 2 do 6, bez 6)poz[1] do [5]
print(tuple_2[2:len(tuple_2)])                # wywolujemy elementy tuple_2 od 3-godo ostatniego (funkcja len pozwala nam zbadac ile elementow tuple_2 ma)
print(tuple_2[-2])                            # mozemy rownierz wskazywac elementy "od tylu" tu druga od tylu poz[-2]
print(tuple_2[0:6:2])                         # polecenie tnace od poz[0] do [6](bez [6]), so drugi element[:2]., tu(42, 45, 88)

print("*" * 100)

x, y = 3, 4                                   # rozpakowywanie (unpacking) tu przypisujemy wartosc 3 do x i 4 do y
x, y = y, x                                   # tu przypisujemy wartosc y do x i wartosc x do y, czyli zamieniamy wartosci zmiennych
print(x, y)                                   # wypisujemy nowe wartosci zmiennych

t = ("John", "Smith")                         # tu tworzymy tuple t z dwoma elementami, pierwszy element to "John" a drugi to "Smith"
(anf, end) = t                                # tu rozpakowujemy tuple t, przypisujemy pierwszy element do zmiennej anf a drugi element do 
                                              # zmiennej end
print(anf, end)                               # tu wypisujemy zawartosc zmiennych anf i end, czyli "John" i "Smith"

first, *remainder = (1, 2, 3, 4, 5)           # tu tworzymy tuple z 5 elementami i rozpakowujemy go, przypisujemy pierwszy element do zmiennej 
                                              # first a reszte elementow do zmiennej remainder
print(first)                                  
print(remainder)                              # tu wypisujemy zawartosc zmiennej remainder, czyli [2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)        # tu tworzymy tuple z 5 elementami i rozpakowujemy go, przypisujemy pierwszy element do zmiennej 
                                              # first, srodkowe do zmiennej middle, a ostatni do zmiennej last
print(first)                                  #   1
print(middle)                                 #  [2, 3, 4]
print(last)                                   #   5
print(type(first))                            #   <class 'int'>
print(type(middle))                           #   <class 'list'>, tu middle jest lista, bo przypisujemy do niej kilka elementow
print(type(last))                             #   <class 'int'>, tu last jest intem, bo przypisujemy do niej jeden element

name_1 = "John Paul Smith"
firstname, middlename, lastname = name_1.split() # tu tworzymy string name_1 i rozpakowujemy go, przypisujemy pierwszy element do zmiennej
print(firstname)                                 #   John
print(middlename)                                #   Paul    
print(lastname)                                  #   Smith

name_2 = ([], )                           # tworzymy tuple name_2 z jednym elementem, którym jest pusta lista[]
name_2[0].append("John")                  # dodajemy element "John" do listy, która jest elementem tuple name_2 poz[0]
print(name_2)                             # wypisujemy zawartosc tuple name_2, czyli (['John'],) widzimy, ze tuple name_2 
                                          # zawiera liste z jednym elementem "John"
