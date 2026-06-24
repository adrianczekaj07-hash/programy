from tkinter import *
master = Tk()
master.geometry('500x200')
t1="Da ist das Untier"
t2="Wo?"
t3="Na da!"
t4="Wo? Hinter dem Karnickel?"
t5="Es IST das Karnickel!"
Label(master,text=t1, bg="yellow", fg="blue").grid(row=0, column=0)
Label(master,text=t2, bg="green", fg="white").grid(row=1, column=1)
Label(master,text=t3, bg="red", fg="blue").grid(row=2, column=2)
Label(master,text=t4, bg="black", fg="white").grid(row=3, column=3)
Label(master,text=t5, bg="yellow", fg="red").grid(row=4, column=4)
master.mainloop()
