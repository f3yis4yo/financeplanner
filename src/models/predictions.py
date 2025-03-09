import tkinter as tk
from tkinter import messagebox

def predict_expenses():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    
    # Simulación de predicción basada en datos ficticios
    prediction_text = "Predicted Expenses for Next Month:\n- Food: $220\n- Rent: $300\n- Utilities: $100"
    
    messagebox.showinfo("Expense Predictions", prediction_text)
    root.destroy()
