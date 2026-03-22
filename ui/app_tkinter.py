# ui/app_tkinter.py

# Importamos tkinter
import tkinter as tk

# Importamos ttk para la tabla
# y messagebox para mensajes emergentes
from tkinter import ttk, messagebox


# Clase de interfaz gráfica
# Recibe el servicio como parámetro
# Esto cumple con inyección de dependencias.
class AppTkinter:

    # Constructor
    def __init__(self, root, servicio):
        # Ventana principal
        self.root = root

        # Guardar el servicio recibido
        self.servicio = servicio

        # Configuración de la ventana
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("950x500")
        self.root.resizable(False, False)

        # Color de fondo de la ventana
        self.root.configure(bg="#F3E8FF")

        # Variables enlazadas a los Entry
        self.cedula_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.motivo_var = tk.StringVar()

        # Crear todos los componentes de la interfaz
        self.crear_interfaz()

        # Cargar la tabla al iniciar
        self.cargar_tabla()

    # -------------------------------------------------
    # CREAR INTERFAZ
    # -------------------------------------------------
    def crear_interfaz(self):
        # Frame del formulario
        frame_formulario = tk.LabelFrame(
            self.root,
            text="Datos del visitante",
            bg="#E6CCFF",
            fg="black",
            padx=10,
            pady=10
        )
        frame_formulario.pack(fill="x", padx=10, pady=10)

        # Etiqueta y entrada para cédula
        tk.Label(
            frame_formulario,
            text="Cédula:",
            bg="#E6CCFF",
            fg="black"
        ).grid(row=0, column=0, padx=5, pady=5, sticky="w")

        tk.Entry(
            frame_formulario,
            textvariable=self.cedula_var,
            width=35
        ).grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para nombre
        tk.Label(
            frame_formulario,
            text="Nombre completo:",
            bg="#E6CCFF",
            fg="black"
        ).grid(row=1, column=0, padx=5, pady=5, sticky="w")

        tk.Entry(
            frame_formulario,
            textvariable=self.nombre_var,
            width=35
        ).grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y entrada para motivo
        tk.Label(
            frame_formulario,
            text="Motivo de visita:",
            bg="#E6CCFF",
            fg="black"
        ).grid(row=2, column=0, padx=5, pady=5, sticky="w")

        tk.Entry(
            frame_formulario,
            textvariable=self.motivo_var,
            width=35
        ).grid(row=2, column=1, padx=5, pady=5)

        # Frame para botones
        frame_botones = tk.Frame(self.root, bg="#F3E8FF")
        frame_botones.pack(pady=10)

        # Botón registrar
        tk.Button(
            frame_botones,
            text="Registrar",
            width=15,
            bg="#4CAF50",
            fg="white",
            activebackground="#388E3C",
            activeforeground="white",
            command=self.registrar
        ).grid(row=0, column=0, padx=10)

        # Botón eliminar
        tk.Button(
            frame_botones,
            text="Eliminar",
            width=15,
            bg="#F44336",
            fg="white",
            activebackground="#C62828",
            activeforeground="white",
            command=self.eliminar
        ).grid(row=0, column=1, padx=10)

        # Botón limpiar campos
        tk.Button(
            frame_botones,
            text="Limpiar campos",
            width=15,
            bg="#2196F3",
            fg="white",
            activebackground="#1565C0",
            activeforeground="white",
            command=self.limpiar
        ).grid(row=0, column=2, padx=10)

        # Estilo para la tabla
        estilo = ttk.Style()
        estilo.theme_use("default")

        estilo.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white"
        )

        estilo.configure(
            "Treeview.Heading",
            background="#B57EDC",
            foreground="black"
        )

        # Frame de la tabla
        frame_tabla = tk.LabelFrame(
            self.root,
            text="Lista de visitantes",
            bg="#E6CCFF",
            fg="black",
            padx=10,
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Definir columnas
        columnas = ("cedula", "nombre", "motivo", "fecha", "hora")

        # Crear tabla
        self.tree = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=12
        )

        # Encabezados de la tabla
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre completo")
        self.tree.heading("motivo", text="Motivo de visita")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")

        # Ancho de columnas
        self.tree.column("cedula", width=120)
        self.tree.column("nombre", width=250)
        self.tree.column("motivo", width=220)
        self.tree.column("fecha", width=120)
        self.tree.column("hora", width=120)

        # Mostrar tabla
        self.tree.pack(fill="both", expand=True)

    # -------------------------------------------------
    # REGISTRAR DESDE LA INTERFAZ
    # -------------------------------------------------
    def registrar(self):
        # Leer datos de los campos
        cedula = self.cedula_var.get().strip()
        nombre = self.nombre_var.get().strip()
        motivo = self.motivo_var.get().strip()

        # Validar campos vacíos
        if not cedula or not nombre or not motivo:
            messagebox.showwarning(
                "Campos vacíos",
                "Todos los campos son obligatorios."
            )
            return

        # Llamar al servicio para registrar
        exito, mensaje = self.servicio.registrar_visitante(
            cedula,
            nombre,
            motivo
        )

        # Mostrar mensajes según el resultado
        if exito:
            messagebox.showinfo("Registro exitoso", mensaje)
            self.cargar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", mensaje)

    # -------------------------------------------------
    # ELIMINAR DESDE LA INTERFAZ
    # -------------------------------------------------
    def eliminar(self):
        # Obtener fila seleccionada
        seleccion = self.tree.selection()

        # Validar que se haya seleccionado una fila
        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccione un visitante para eliminar."
            )
            return

        # Obtener información de la fila seleccionada
        item = self.tree.item(seleccion[0])
        valores = item["values"]

        # La cédula está en la primera columna
        cedula = str(valores[0])

        # Llamar al servicio
        exito, mensaje = self.servicio.eliminar_visitante(cedula)

        # Mostrar resultado
        if exito:
            messagebox.showinfo("Eliminado", mensaje)
            self.cargar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", mensaje)

    # -------------------------------------------------
    # CARGAR TABLA
    # -------------------------------------------------
    def cargar_tabla(self):
        # Limpiar tabla antes de volver a cargar datos
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        # Insertar cada visitante en la tabla
        for visitante in self.servicio.obtener_visitantes():
            self.tree.insert(
                "",
                "end",
                values=(
                    visitante.cedula,
                    visitante.nombre_completo,
                    visitante.motivo_visita,
                    visitante.fecha,
                    visitante.hora
                )
            )

    # -------------------------------------------------
    # LIMPIAR CAMPOS
    # -------------------------------------------------
    def limpiar(self):
        # Vaciar los campos del formulario
        self.cedula_var.set("")
        self.nombre_var.set("")
        self.motivo_var.set("")