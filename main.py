from tkinter import ttk
import tkinter as tk
from tkinter import *



root = tk.Tk() 

root.title("titolo della finestra")
root.geometry("300x300")
root.resizable(False, False)

def command1():
    pass

def callback():
    print("ciao")

##riga testo
label = Label(root, text="Inserisci città", font=("Helvetica", 14))
label.pack(ipadx=10, ipady=10)

#inserisco immagine
# photo = tk.PhotoImage(file='./logo5.jpg')
# image_label = Label(
#     root,
#     image=photo,
#     padding=5
# )
# image_label.pack() 

button_ok = Button(
    root,
    text="Clicca",
    command=callback
)

button_ok.pack(
    ipdax=15,
    ipady=15,
    expand=True
)



root.mainloop() 