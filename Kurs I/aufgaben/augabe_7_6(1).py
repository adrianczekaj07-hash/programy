print("Gib Deiner Hund Geburtsdatum ein: ")

from datetime import date

hund_geburts_datum = date(int(input("Jahr: ")), int(input("Monat: ")), int(input("Tag: ")))
heute = date.today()

menschen_monaten = (heute.year * 12 + heute.month) - (hund_geburts_datum.year * 12 + hund_geburts_datum.month)
if menschen_monaten < 0:
    print("Noch kein Hund?...Schade")

elif menschen_monaten <= 12:
    print("Dein Hund is jetzt " + str(int(menschen_monaten * 1.16666667)) + " Jahre alt(in Hund Jahren).")

elif menschen_monaten <= 24:
    print("Dein Hund is jetzt " + str(int(14 + ((menschen_monaten - 12) * 0.6666667))) + " Jahre alt.")

else:
    print("Dein Hund is jetzt " + str(int(22 + ((menschen_monaten - 24) * 0.4166667))) + " Jahre alt.")
