from Kunde import *     
from Konto import *

kunde_1 = Kunde("Hans", "Dampf", 42, "Mann", "Milchstrasse 123, 777 Irgendwodorf", Konto(1000, "Girokonto"))

print(kunde_1.vorname)

print(kunde_1.konto)

print(kunde_1.konto.kontostand)

kunde_1.konto.einzahlen(123)

print(kunde_1.konto.kontostand)
