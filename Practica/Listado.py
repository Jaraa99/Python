
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")


tareas_pendientes = []

while True:
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas pendientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ")
        tareas_pendientes.append(nueva_tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        mostrar_tareas(tareas_pendientes)
        if tareas_pendientes:
            num_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
            if 1 <= num_tarea <= len(tareas_pendientes):
                tarea_eliminada = tareas_pendientes.pop(num_tarea - 1)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Número de tarea inválido.")
        else:
            print("No hay tareas pendientes para eliminar.")

    elif opcion == "3":
        mostrar_tareas(tareas_pendientes)

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Inténtelo de nuevo.")
