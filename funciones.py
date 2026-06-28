import os

CARPETA = os.path.dirname(__file__)
ARCHIVO = os.path.join(CARPETA, "datos.txt")


def registrar_usuario():
    nombre = input("Nombre del usuario: ").title()
    horas = float(input("Horas de uso al día: "))

    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(nombre + "," + str(horas) + "\n")
    archivo.close()

    print("\nUsuario registrado correctamente.")
    input("Presione Enter para continuar...")


def ver_historial():
    print("\n===== HISTORIAL =====")

    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        if len(lineas) == 0:
            print("No existen registros.")
        else:
            for linea in lineas:
                datos = linea.strip().split(",")
                print("Usuario:", datos[0], "| Horas:", datos[1])

    except FileNotFoundError:
        print("No existe el archivo datos.txt.")

    input("\nPresione Enter para continuar...")


def buscar_usuario():
    buscar = input("Ingrese el nombre del usuario: ").title()
    encontrado = False

    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            datos = linea.strip().split(",")

            if datos[0] == buscar:
                print("\nUsuario encontrado")
                print("Horas de uso:", datos[1])
                encontrado = True

        if encontrado == False:
            print("\nUsuario no encontrado.")

    except FileNotFoundError:
        print("No existen registros.")

    input("\nPresione Enter para continuar...")


def estadisticas():
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        if len(lineas) == 0:
            print("\nNo hay datos.")
            input("Presione Enter para continuar...")
            return

        total = 0
        mayor = 0
        usuario_mayor = ""

        for linea in lineas:
            datos = linea.strip().split(",")
            horas = float(datos[1])
            total = total + horas

            if horas > mayor:
                mayor = horas
                usuario_mayor = datos[0]

        promedio = total / len(lineas)

        print("\n===== ESTADÍSTICAS =====")
        print("Usuarios registrados:", len(lineas))
        print("Promedio de horas:", round(promedio, 2))
        print("Mayor tiempo de uso:", usuario_mayor, "-", mayor, "horas")

    except FileNotFoundError:
        print("No existen registros.")

    input("\nPresione Enter para continuar...")


def recomendaciones():
    buscar = input("Ingrese el nombre del usuario: ").title()
    encontrado = False

    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            datos = linea.strip().split(",")

            if datos[0] == buscar:
                horas = float(datos[1])
                encontrado = True

                print("\n===== RECOMENDACIÓN =====")

                if horas <= 3:
                    print("Uso BAJO")
                    print("Excelente equilibrio digital.")
                elif horas <= 6:
                    print("Uso MODERADO")
                    print("Recuerda descansar cada cierto tiempo.")
                else:
                    print("Uso EXCESIVO")
                    print("Se recomienda reducir el tiempo frente a pantallas.")

        if encontrado == False:
            print("\nUsuario no encontrado.")

    except FileNotFoundError:
        print("No existen registros.")

    input("\nPresione Enter para continuar...")