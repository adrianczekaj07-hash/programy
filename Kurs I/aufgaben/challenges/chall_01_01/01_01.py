import sys
import re 

arg = input("Geben Sie eine einstellige Zahl ein ")

if arg == "":
    sys.exit("Es muss ein Zeichen eingegeben werden. ")

if len(arg) > 1:
    sys.exit("Es darf nur ein Zeichen eingegeben werden. ")

erg = re.search(r"\D", arg)

if erg:
    print("Das ist kein Zahl zwischen 0 und 9. ")

