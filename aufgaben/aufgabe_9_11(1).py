de_liste = ["Datei", "Neu", "Öffnen", "Speichern", "Speichern unter", "Druckansicht", "Drucken", "Schliesen", "Verlassen"]
en_liste = ["File", "New", "Open", "Save", "Save As","Print Preview", "Print", "Close", "Exit"]
fr_liste = ["Fichier", "Nouveau", "Ouvrir", "Enregistrer", "Enregistrer sous","Aperçu avant impression", "Imprimer", "Fermer", "Quitter"]
it_liste = ["File", "Nuovo", "Apri", "Salva", "Salva con nome","Anteprima di stampa", "Stampa", "Chiudi", "Esci"]


lex_01 = {en: {"de": de, "fr": fr, "it": it} for en, de, fr, it in zip(en_liste, de_liste, fr_liste, it_liste)}


befehl = input("Geben Sie einen Befehl ein:\nen:\t English\nde:\t German\nfr:\t French\nit:\t Italian\n")

match befehl:
    case "en":
        print("English Menu\n")
        for item in lex_01:
            print(f"{item:16} : {item}")

    case "de":
        print("Deutsches Menü\n")
        for item in lex_01:
            print(f"{item:16} : {lex_01[item]["de"]}")

    case "fr":
        print("Menu Français\n")
        for item in lex_01:
            print(f"{item:16} : {lex_01[item]["fr"]}")

    case "it":
        print("Menu Italiano\n")
        for item in lex_01:
            print(f"{item:16} : {lex_01[item]["it"]}")

    case _:                                                     
        print("Falscher Befehl")








    


