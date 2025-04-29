import turtle


# Configuración de la ventana

window = turtle.Screen()

window.title("Dibujo de un Cuadrado")


# Crear un objeto turtle

cuadrado = turtle.Turtle()


# Dibujar un cuadrado

for _ in range(4):

    cuadrado.forward(100)  # Mover hacia adelante 100 unidades

    cuadrado.right(90)     # Girar 90 grados a la derecha


# Finalizar

turtle.done()