import funciones

while True:
    print("\n===================================")
    print("        TECHCARE SYSTEM")
    print("===================================")
    print("1. Registrar usuario")
    print("2. Ver historial")
    print("3. Buscar usuario")
    print("4. Ver estadísticas")
    print("5. Recomendaciones")
    print("6. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        funciones.registrar_usuario()
    elif opcion == "2":
        funciones.ver_historial()
    elif opcion == "3":
        funciones.buscar_usuario()
    elif opcion == "4":
        funciones.estadisticas()
    elif opcion == "5":
        funciones.recomendaciones()
    elif opcion == "6":
        print("\nGracias por utilizar TechCare System.")
        break
    else:
        print("\nOpción inválida.")