import tkinter as tk
import os
from models import expenses
from models import summary
from models import predictions
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Imports Image and ImageTk from Pillow

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        self.root.geometry("400x500")
        self.root.configure(bg="#FFF44F")  # Lemon color
        
        # Frame for the top part (to organize the title and right button)
        frame_top = tk.Frame(root, bg="#FFF44F")
        frame_top.pack(fill=tk.X, padx=10, pady=20)

        # Title label
        self.label = tk.Label(frame_top, text="Hi, Ivan", font=("Arial", 16, "bold"), bg="#FFF44F", fg="black")
        self.label.pack(side=tk.LEFT)

        # Button in the upper right corner
       
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the script directory
        image_path = os.path.join(script_dir, "..", "..", "static", "image", "power.png") # Builds the relative path
        print(image_path)
        power_icon = None  # Initializes power_icon with None
        if not os.path.exists(image_path):
            print(f"Image file not found at {image_path}")
        else:
            original_image = Image.open(image_path)
            resized_image = original_image.resize((60, 60), Image.LANCZOS) # Scales the image to 60x60
            power_icon = ImageTk.PhotoImage(resized_image)

        script_dir = os.path.dirname(os.path.abspath(__file__))  # Gets the script directory
        image_path = os.path.join(script_dir, "..", "..", "static", "image", "settings.png") # Builds the relative path
        settings_icon = None  # Initializes settings_icon with None
        if not os.path.exists(image_path):
            print(f"Image file not found at {image_path}")
        else:
            original_image = Image.open(image_path)
            resized_image = original_image.resize((20, 20), Image.LANCZOS) # Scales the image to 20x20
            settings_icon = ImageTk.PhotoImage(resized_image)

        if power_icon:  # Checks if power_icon has an assigned value
            self.btn_exit = tk.Button(frame_top, image=power_icon, command=root.quit, borderwidth=0)
            self.btn_exit.image = power_icon
            self.btn_exit.pack(side=tk.RIGHT, anchor="ne", padx=5)
        else:
            self.btn_exit = tk.Button(frame_top, text="Exit", command=root.quit, borderwidth=0)
            self.btn_exit.pack(side=tk.RIGHT, anchor="ne", padx=5)

        if settings_icon: # Checks if settings_icon has an assigned value
            self.btn_settings = tk.Button(frame_top, image=settings_icon, command=self.open_settings, borderwidth=0)
            self.btn_settings.image = settings_icon
            self.btn_settings.pack(side=tk.RIGHT, anchor="ne", padx=5)
        else:
            self.btn_settings = tk.Button(frame_top, text="Settings", command=self.open_settings, borderwidth=0)
            self.btn_settings.pack(side=tk.RIGHT, anchor="ne", padx=5)

        # Frame for the buttons at the bottom
        frame_buttons = tk.Frame(root, bg="#FFF44F")
        frame_buttons.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

        # Buttons organized at the bottom
        self.btn_add_expense = tk.Button(frame_buttons, text="Budget", command=expenses.add_expense)
        self.btn_add_expense.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.btn_view_summary = tk.Button(frame_buttons, text="Expenses", command=summary.view_summary)
        self.btn_view_summary.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.btn_predict_expenses = tk.Button(frame_buttons, text="Financial Summary", command=predictions.predict_expenses)
        self.btn_predict_expenses.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

    def open_settings(self):
        print("Open settings")

    def show(self):
        print("Displaying dashboard")

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()