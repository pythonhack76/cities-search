import tkinter as tk
from tkinter import ttk
from tkinter import *

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')

def command1():
    pass

def callback():
    print("ciao")

##riga testo
label = Label(root, text="Inserisci città", font=("Helvetica", 14))
label.pack(ipadx=10, ipady=10)

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()