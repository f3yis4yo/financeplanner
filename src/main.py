import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from view.dashboard import Dashboard  # Importa la clase desde dashboard.py

def main():
    root = tk.Tk()
    app = Dashboard(root)  # Inicializa la ventana del dashboard
    root.mainloop()  # Mantiene la aplicación en ejecución

if __name__ == "__main__":
    main()
