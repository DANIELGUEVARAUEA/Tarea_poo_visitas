# servicios/visita_servicio.py

# Importamos la clase modelo
from modelos.visitante import Visitante

# Librería estándar para manejo de archivos
import os

# Librería estándar para fecha y hora
from datetime import datetime


# Clase de servicio.
# Aquí se maneja la lógica del programa:
# registrar, listar, eliminar, guardar en txt y cargar desde txt.
class VisitaServicio:

    # Constructor
    def __init__(self):
        # Lista privada donde se guardan los visitantes en memoria
        self._visitantes = []

        # Nombre del archivo txt
        self.archivo = "visitantes.txt"

        # Al iniciar, cargar datos del archivo si existe
        self.cargar_desde_txt()

    # -------------------------------------------------
    # GUARDAR EN TXT
    # -------------------------------------------------
    def guardar_en_txt(self):
        # Abrir el archivo en modo escritura
        # Se reescribe todo el contenido actualizado
        with open(self.archivo, "w", encoding="utf-8") as archivo:

            # Recorrer todos los visitantes guardados en la lista
            for visitante in self._visitantes:
                # Crear una línea de texto con los datos separados por comas
                linea = (
                    f"{visitante.cedula},"
                    f"{visitante.nombre_completo},"
                    f"{visitante.motivo_visita},"
                    f"{visitante.fecha},"
                    f"{visitante.hora}\n"
                )

                # Escribir la línea en el archivo
                archivo.write(linea)

    # -------------------------------------------------
    # CARGAR DATOS DESDE TXT
    # -------------------------------------------------
    def cargar_desde_txt(self):
        # Verificar si el archivo existe
        if not os.path.exists(self.archivo):
            return

        # Abrir el archivo en modo lectura
        with open(self.archivo, "r", encoding="utf-8") as archivo:

            # Leer línea por línea
            for linea in archivo:
                # Quitar salto de línea y dividir por comas
                datos = linea.strip().split(",")

                # Validar que tenga 5 datos
                if len(datos) == 5:
                    cedula, nombre, motivo, fecha, hora = datos

                    # Crear objeto Visitante con los datos leídos
                    visitante = Visitante(
                        cedula,
                        nombre,
                        motivo,
                        fecha,
                        hora
                    )

                    # Agregar el visitante a la lista
                    self._visitantes.append(visitante)

    # -------------------------------------------------
    # REGISTRAR VISITANTE
    # -------------------------------------------------
    def registrar_visitante(self, cedula, nombre, motivo):
        # Verificar que la cédula no esté repetida
        for visitante in self._visitantes:
            if str(visitante.cedula) == str(cedula):
                return False, "Ya existe un visitante con esa cédula."

        # Obtener fecha y hora actual
        ahora = datetime.now()

        # Formato de fecha
        fecha = ahora.strftime("%d/%m/%Y")

        # Formato de hora
        hora = ahora.strftime("%H:%M:%S")

        # Crear el nuevo objeto visitante
        nuevo_visitante = Visitante(
            cedula,
            nombre,
            motivo,
            fecha,
            hora
        )

        # Agregar el visitante a la lista
        self._visitantes.append(nuevo_visitante)

        # Guardar los cambios en el txt
        self.guardar_en_txt()

        return True, "Visitante registrado correctamente."

    # -------------------------------------------------
    # OBTENER LISTA DE VISITANTES
    # -------------------------------------------------
    def obtener_visitantes(self):
        # Retorna la lista actual de visitantes
        return self._visitantes

    # -------------------------------------------------
    # ELIMINAR VISITANTE
    # -------------------------------------------------
    def eliminar_visitante(self, cedula):
        # Buscar el visitante por cédula
        for visitante in self._visitantes:
            if str(visitante.cedula) == str(cedula):
                # Eliminar el visitante encontrado
                self._visitantes.remove(visitante)

                # Actualizar el txt
                self.guardar_en_txt()

                return True, "Visitante eliminado correctamente."

        # Si no se encontró la cédula
        return False, "No se encontró el visitante."