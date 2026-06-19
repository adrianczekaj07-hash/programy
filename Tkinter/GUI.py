import tkinter as tk

# Funkcja wywoływana po kliknięciu przycisku
def pokaz_tekst():
    etykieta.config(text="Hallo")

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("GUI test")
okno.geometry("300x200")

# Przycisk
przycisk = tk.Button(okno, text="push", command=pokaz_tekst)
przycisk.pack(pady=20)

# Etykieta
etykieta = tk.Label(okno, text="")
etykieta.pack()

# Uruchomienie pętli programu
okno.mainloop()