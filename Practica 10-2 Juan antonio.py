import math

# Ejemplo 1: Calcular el factorial
num = int(input("Número para factorial: "))
print("Factorial:", math.factorial(num))

# Ejemplo 2: Suma de los dígitos
num = input("Número para suma de dígitos: ")
print("Suma de dígitos:", sum(map(int, num)))

# Ejemplo 3: Formato creciente y decreciente
m = int(input("Número para el patrón: "))
for i in range(1, m + 1):
    print(''.join(str(j) for j in range(1, i + 1)))
for i in range(m, 0, -1):
    print('*' * i)

# Ejemplo 4: Promedio de 10 números
numeros = list(map(int, input("10 números separados por comas: ").split(',')))
print("Promedio:", sum(numeros) / len(numeros))

# Ejemplo 5: Números primos entre dos valores
a, b = map(int, input("Dos números separados por espacio: ").split())
print("Números primos entre", a, "y", b, ":")
for num in range(a, b + 1):
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num)
