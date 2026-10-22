
import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        result = num1 + num2
        result_label.config(text=f"Addition = {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("350x250")

tk.Label(root, text="Addition of Two Numbers",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add_numbers).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
 
