import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Login")

#fungsi
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password =="admin":
        tk.Label(root, text="Login Berhasil", fg="green", bg="white").place(x=15, y=130)
    else:
        tk.Label(root, text="Login Gagal", fg="red", bg="white").place(x=15, y=130)


# FORM
tk.Label(root, text="Login", fg="blue", bg="white").place(x=15, y=10)

tk.Label(root, text="Username", fg="blue", bg="white").place(x=15, y=40)
entry_username = tk.Entry(root)
entry_username.place(x=100,y=40)

tk.Label(root, text="Password", fg="blue", bg="white").place(x=15, y=70)
entry_password = tk.Entry(root, show="*")
entry_password.place(x=100,y=70)

tk.Button(root,text="Login", fg="blue", bg="white", command=login).place(x=15,y=100)

root.bind('<Return>', lambda event: login())

root.mainloop()