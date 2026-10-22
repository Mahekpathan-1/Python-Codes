
import tkinter as tk
from tkinter import messagebox
import math

def calculate_area():
    try:
        radius = float(entry_radius.get())

        if radius < 0:
            messagebox.showerror("Error", "Radius cannot be negative")
            return

        area = math.pi * radius * radius
        result_label.config(text=f"Area of Circle = {area:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid radius")

root = tk.Tk()
root.title("Area of Circle")
root.geometry("350x220")

tk.Label(root, text="Area of Circle",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Radius").pack()
entry_radius = tk.Entry(root)
entry_radius.pack()

tk.Button(root, text="Calculate Area",
          command=calculate_area).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
