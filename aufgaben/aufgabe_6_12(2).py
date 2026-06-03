einkaufs_liste = ["Milch", "Brot", "Eier", "Käse", "Äpfel", "Bananen", "Orangen", "Butter", "Joghurt"]
wagen = []  

arg = str(input("Geben Sie den Namen eines Artikels ein, den Sie kaufen möchten: "))

a = len(einkaufs_liste) - 1
while a > 0:
    if arg in einkaufs_liste:
        wagen.append(arg)
        einkaufs_liste.remove(arg)
        print("Artikel", arg, "wurde zum Wagen hinzugefügt.")
        print("Aktuelle Einkaufsliste:", einkaufs_liste)
        print("Aktueller Wagen:", wagen)
        arg = str(input("Nechsten Artikel eingeben: "))
        a -= 1
    else:
        print("Artikel", arg, "ist nicht in der Einkaufsliste.")
        arg = str(input("Nechsten Artikel eingeben: "))

print("Einkaufsliste ist leer. Alle Artikel wurden gekauft.")




    
    





        
