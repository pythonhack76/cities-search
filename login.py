import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo

# root window
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()
address = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    msg = f'You entered email: {email.get()} and password: {password.get()}'
    showinfo(
        title='Information',
        message=msg
    )

def close_login():    
    msg = f'sto chiudendo la finestra...'
    showinfo(
        title='Info',
        message=msg
    )
    root.destroy()

def conferma():
    risposta = askyesno(title='conferma',
                        message='Sei sicuro di chiudere la finestra?')
    if risposta:
        root.destroy()




# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

# close button
close_button = ttk.Button(signin, text="Close", command=conferma)
close_button.pack(fill='x', expand=True, padx=10, pady=10)


root.mainloop()