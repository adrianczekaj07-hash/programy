zeichen = {}

with open("aufgaben\challenges\chall_01_02\Tekst.txt", "r", encoding="utf-8") as datei:
    text = datei.read()

for buchstabe in text:
    if buchstabe in zeichen:
        zeichen[buchstabe] += 1
    else:
        zeichen[buchstabe] = 1

sortiert = sorted(zeichen.items(), key=lambda x: x[1])

for buchstabe, anzahl in sortiert:
    print(f"'{buchstabe}' : {anzahl}")

