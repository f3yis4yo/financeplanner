import tkinter as tk
from tkinter import messagebox

def view_summary():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    # Aquí se puede calcular un resumen real a partir de los datos almacenados
    summary_text = "Total Expenses: $500\nCategories:\n- Food: $200\n- Rent: $300"
    
    messagebox.showinfo("Financial Summary", summary_text)
    root.destroy()
