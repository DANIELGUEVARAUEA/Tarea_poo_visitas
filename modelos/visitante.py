# modelos/visitante.py

# Clase modelo.
# Esta clase solo guarda los datos del visitante.
# No contiene lógica del sistema.


class Visitante:
    # Constructor de la clase
    def __init__(self, cedula, nombre_completo, motivo_visita, fecha, hora):
        # Cédula del visitante
        self.cedula = cedula

        # Nombre completo del visitante
        self.nombre_completo = nombre_completo

        # Motivo de la visita
        self.motivo_visita = motivo_visita

        # Fecha del registro
        self.fecha = fecha

        # Hora del registro
        self.hora = hora