from datetime import datetime, timedelta

# Diferencias de zonas horarias respecto a México (en horas)
zonas_horarias = {
    "Dublín": 6,
    "Londres": 7,
    "Tokio": 15,
    "Los Ángeles": -2,
    "Nueva York": 2,
    "Nueva Delhi": 11.3
}

# Solicitar la hora al usuario
hora_mexico = input("Ingresa la hora en formato HH:MM AM/PM: ")

try:
    # Parsear la hora ingresada por el usuario
    hora_formato_12 = datetime.strptime(hora_mexico, "%I:%M %p")

    # Calcular y mostrar la hora en cada ciudad
    print("La hora en las siguientes ciudades sería:")
    for ciudad, diferencia in zonas_horarias.items():
        hora_ciudad = hora_formato_12 + timedelta(hours=diferencia)
        print(f"{ciudad}: {hora_ciudad.strftime('%I:%M %p')}")

except ValueError:
    print("Formato de hora inválido. Asegúrate de usar el formato HH:MM AM/PM.")
