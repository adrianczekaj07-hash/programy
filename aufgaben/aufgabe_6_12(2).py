

einkaufs_liste = ["Milch", "Brot", "Eier", "Käse", "Äpfel", "Bananen", "Orangen", "Butter", "Joghurt"]
print("Deine Einkaufsliste: ")
a = 0
for x in einkaufs_liste:  
    a += 1      
    print("Produkt Nr:", a, "\t", x)  
  

def produkt_in_liste(c):
    if c in einkaufs_liste:
        print("Produkt", c, "wird in den Einkaufswagen gelegt.")  
        return d = {}
          
    else:
        print(c, "ist nicht auf der Einkaufsliste.")
        return False

produkt = input("Geben Sie ein Produkt ein, das Sie ins Einkaufswagen legen: ")
produkt_in_liste(produkt)