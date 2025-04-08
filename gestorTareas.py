from SistemaDeTareasPY.tarea import Tarea
import os

class GestorTareas:
    def __init__(self, archivo="tareas.txt"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r", encoding="utf-8") as f:
            return [Tarea.from_linea(linea) for linea in f if linea.strip()]

    def guardar_tareas(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for tarea in self.tareas:
                f.write(tarea.to_linea() + "\n")

    def agregar_tarea(self, titulo, descripcion):
        nueva = Tarea(titulo, descripcion)
        self.tareas.append(nueva)
        self.guardar_tareas()
        print("Tarea agregada correctamente")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
            self.guardar_tareas()
            print("Tarea eliminada")
        else:
            print("indice invalido")

    def ver_todas(self):
        for i, tarea in enumerate(self.tareas):
            print(f"{i + 1}. {tarea}")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            self.guardar_tareas()
            print(" Tarea marcada como completada")
        else:
            print(" indice invalido")

    def ver_completadas(self):
        for tarea in self.tareas:
            if tarea.completada:
                print(tarea)

    def ver_pendientes(self):
        for tarea in self.tareas:
            if not tarea.completada:
                print(tarea)

    def modificar_tarea(self, indice, nuevo_titulo, nueva_descripcion):
        if 0 <= indice < len(self.tareas):
            if not Tarea.validar_texto(nuevo_titulo) or not Tarea.validar_texto(nueva_descripcion):
                print(" Texto con caracteres inválidos.")
                return
            self.tareas[indice].titulo = nuevo_titulo
            self.tareas[indice].descripcion = nueva_descripcion
            self.guardar_tareas()
            print(" Tarea modificada correctamente")
        else:
            print(" indice invalido")
