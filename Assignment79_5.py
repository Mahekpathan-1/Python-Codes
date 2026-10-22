
import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("350x250")

tk.Label(root, text="Login Form",
         font=("Arial", 16, "bold")).pack(pady=15)

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
