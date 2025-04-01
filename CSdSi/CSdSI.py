def guardar_alumno():
    # Solicitar información del alumno
    
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
    # Abrir archivo en modo 'append' para agregar información nueva
    with open("alumnos.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}, Edad: {edad}, Fecha de Nacimiento: {fecha_nacimiento}\n")
    print("Información guardada correctamente.")

def mostrar_alumnos():
    try:
        # Leer y mostrar el contenido del archivo
        with open("alumnos.txt", "r") as archivo:
            print("\nInformación de los alumnos:")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo 'alumnos.txt' no existe aún. Por favor guarda información primero.")

# Menú principal
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
