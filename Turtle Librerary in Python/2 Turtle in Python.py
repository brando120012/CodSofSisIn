import turtle


def estrella():

    est = turtle.Turtle()  # Crear un objeto Turtle

    est.right(75)           # Girar a la derecha 75 grados

    est.forward(100)       # Mover hacia adelante 100 unidades


    for i in range(5):     # Dibujar 5 puntas de la estrella

        est.right(144)     # Girar a la derecha 144 grados

        est.forward(100)   # Mover hacia adelante 100 unidades


# Configuración de la ventana

window = turtle.Screen()

window.title("Dibujo de una Estrella")


estrella()  # Llamar a la función para dibujar la estrella


# Finalizar

turtle.done()