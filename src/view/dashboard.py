import tkinter as tk
from tkinter import messagebox
from models import expenses
from models import summary
from models import predictions

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.root.geometry("400x300")
        
        self.label = tk.Label(root, text="Finance Tracker", font=("Arial", 16))
        self.label.pack(pady=10)
        
        self.btn_add_expense = tk.Button(root, text="Add Expense", command=expenses.add_expense)
        self.btn_add_expense.pack(pady=5)
        
        self.btn_view_summary = tk.Button(root, text="View Summary", command=summary.view_summary)
        self.btn_view_summary.pack(pady=5)
        
        self.btn_predict_expenses = tk.Button(root, text="Predict Expenses", command=predictions.predict_expenses)
        self.btn_predict_expenses.pack(pady=5)
        
        self.btn_exit = tk.Button(root, text="Exit", command=root.quit)
        self.btn_exit.pack(pady=5)

    def show(self):
        print("Displaying dashboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()