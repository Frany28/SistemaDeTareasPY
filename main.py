from SistemaDeTareasPY.gestorTareas import GestorTareas
import os
gestor = GestorTareas()


def menu():
    while True:
  
        print("=== MENÚ DE TAREAS ===")
        print("1. Agregar una tarea")
        print("2. Eliminar una tarea")
        print("3. Ver todas las tareas")
        print("4. Marcar tarea como completada")
        print("5. Ver tareas completadas")
        print("6. Ver tareas pendientes")
        print("7. Modificar una tarea")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            desc = input("Descripcion: ")
            try:
                os.system('cls')
                gestor.agregar_tarea(titulo, desc)
            except ValueError as e:
                print(f" {e}")
        elif opcion == "2":
            gestor.ver_todas()
            i = int(input("Índice de la tarea a eliminar: ")) - 1
            os.system('cls')
            gestor.eliminar_tarea(i)
        elif opcion == "3":
            gestor.ver_todas()
        elif opcion == "4":
            gestor.ver_todas()
            i = int(input("Índice a marcar como completada: ")) - 1
            gestor.marcar_completada(i)
        elif opcion == "5":
            gestor.ver_completadas()
        elif opcion == "6":
            gestor.ver_pendientes()
        elif opcion == "7":
            gestor.ver_todas()
            i = int(input("Índice a modificar: ")) - 1
            nuevo_titulo = input("Nuevo titulo: ")
            nueva_desc = input("Nueva descripción: ")
            gestor.modificar_tarea(i, nuevo_titulo, nueva_desc)
        elif opcion == "8":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("Opción invalida")

        input("\nPresiona Enter para continuar")
