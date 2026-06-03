print("Geben Sie ein Jahr, dass Sie überprüfen möchten ob es ein Schaltjahr ist:")
untersuchte_jahr = int(input())

if (untersuchte_jahr % 4 != 0):
    print("Das Jahr", untersuchte_jahr, "ist kein Schaltjahr.")

elif (untersuchte_jahr % 100 == 0):
    if (untersuchte_jahr % 400 == 0):
        print("Das Jahr", untersuchte_jahr, "ist ein Schaltjahr.")  
    else:
        print("Das Jahr", untersuchte_jahr, "ist kein Schaltjahr.")
else:
    print("Das Jahr", untersuchte_jahr, "ist ein Schaltjahr.")