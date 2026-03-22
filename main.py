# main.py

# Importar tkinter
import tkinter as tk

# Importar la clase del servicio
from servicios.visita_servicio import VisitaServicio

# Importar la clase de la interfaz
from ui.app_tkinter import AppTkinter


# Función principal
def main():
    # Crear ventana principal
    root = tk.Tk()

    # Crear el servicio
    servicio = VisitaServicio()

    # Crear la app pasando el servicio a la interfaz
    app = AppTkinter(root, servicio)

    # Mantener la ventana abierta
    root.mainloop()


# Ejecutar solo si este archivo es el principal
if __name__ == "__main__":
    main()