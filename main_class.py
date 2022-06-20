import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Yes/No Dialog')
        self.geometry('300x150')

        # Quit button
        quit_button = ttk.Button(self, text='Quit', command=self.confirm)
        quit_button.pack(expand=True)


        #New button
        new_button = ttk.Button(self, text="Show", command=self.show)
        new_button.pack(expand=True)

    def confirm(self):
        answer = askyesno(title='Confirmation',
                          message='Are you sure that you want to quit?')
        if answer:
            self.destroy()

    def show(self):
        risultato = Text(app, height=10)
        risultato.pack() 
        risultato.insert('1.0', 'messaggio')


if __name__ == "__main__":
    app = App()
    app.mainloop()
