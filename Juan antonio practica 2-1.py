# Tasas de conversión de divisas
yuan = 2.81  # China
yen = 0.14  # Japón
dolar = 20.49  # Estados Unidos
euro = 21.28  # Unión Europea
libra = 25.5  # Reino Unido

# Solicitar al usuario la cantidad de pesos
pesos = float(input("Ingresa la cantidad de pesos a convertir: "))

# Calcular equivalencias
equivalente_yuan = pesos / yuan
equivalente_yen = pesos / yen
equivalente_dolar = pesos / dolar
equivalente_euro = pesos / euro
equivalente_libra = pesos / libra

# Imprimir resultados
print("Los pesos equivalen a:")
print(f"{equivalente_yuan:.2f} Yuanes")
print(f"{equivalente_yen:.2f} Yenes")
print(f"{equivalente_dolar:.2f} Dólares")
print(f"{equivalente_euro:.2f} Euros")
print(f"{equivalente_libra:.2f} Libras")