import re

class Tarea:
    def __init__(self, titulo, descripcion, completada=False):
        # Validamos tItulo y descripción con regex para evitar caracteres no permitidos
        if not self.validar_texto(titulo) or not self.validar_texto(descripcion):
            raise ValueError("El tItulo o la descripción contiene caracteres no permitidos.")
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.titulo} | {self.descripcion} | {estado}"

    def to_linea(self):
        return f"{self.titulo}|{self.descripcion}|{int(self.completada)}"

    @staticmethod
    def from_linea(linea):
        partes = linea.strip().split("|")
        return Tarea(partes[0], partes[1], bool(int(partes[2])))

    @staticmethod
    def validar_texto(texto):
        return re.fullmatch(r"[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ.,:;¡!¿?\s]+", texto)
