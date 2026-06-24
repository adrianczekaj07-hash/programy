from tkinter import *

class Application(Frame):                # tworzymy klase i wskazujemy jej super() klase, po ktorej bedzie dziedziczyc wszystkie wlasnosci(tu Frame)
    def __init__(self, master=None):
        Frame.__init__(self, master)

root = Tk()
app = Application(master=root)
app.mainloop()
