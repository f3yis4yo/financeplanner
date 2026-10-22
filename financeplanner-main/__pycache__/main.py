import sys
import os
import tkinter as tk
from view import Dashboard  # Importa la clase desde dashboard.py

# Obtener la ruta del directorio raíz del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)  # Agregarlo a sys.path

def main():
    root = tk.Tk()
    app = Dashboard(root)  # Inicializa la ventana del dashboard
    root.mainloop()  # Mantiene la aplicación en ejecución

if __name__ == "__main__":
    main()
