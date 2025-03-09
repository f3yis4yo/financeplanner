import tkinter as tk
from tkinter import simpledialog, messagebox

def add_expense():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    amount = simpledialog.askfloat("Add Expense", "Enter amount:")
    category = simpledialog.askstring("Add Expense", "Enter category:")
    
    if amount and category:
        # Aquí se puede guardar en una base de datos o archivo
        messagebox.showinfo("Success", f"Expense added: {amount} in {category}")
    else:
        messagebox.showwarning("Warning", "Expense not added. Please provide valid inputs.")
    
    root.destroy()