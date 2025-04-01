# alumnos.py

CONSTANTE_ARCHIVO = "alumnos.txt"


def guardar_alumno():
    """Solicita información de un alumno y la almacena en un archivo."""
    
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")

    with open(CONSTANTE_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"Nombre: {nombre}, Edad: {edad}, Fecha de Nacimiento: {fecha_nacimiento}\n")

    print("Información guardada correctamente.")


def mostrar_alumnos():
    """Lee y muestra la información almacenada en el archivo de alumnos."""
    
    try:
        with open(CONSTANTE_ARCHIVO, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                print("\nInformación de los alumnos:")
                print(contenido)
            else:
                print("El archivo está vacío, guarda información primero.")
    except FileNotFoundError:
        print(f"El archivo '{CONSTANTE_ARCHIVO}' no existe aún. Por favor guarda información primero.")


def mostrar_menu():
    """Muestra el menú principal y gestiona la interacción con el usuario."""

    while True:
        print("\nMenú:")
        print("1. Guardar información de un alumno")
        print("2. Mostrar información guardada")
        print("3. Salir")

        opcion = input("Selecciona una opción (1, 2, 3): ")

        if opcion == "1":
            guardar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor intenta nuevamente.")


if __name__ == "__main__":
    mostrar_menu()
