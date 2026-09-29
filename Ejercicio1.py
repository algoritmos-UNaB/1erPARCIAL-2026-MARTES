Ejercicio 1: La Serie de Potencias de Sheldon
Generar un conjunto por compresión que contenga los números racionales que son potencia de 3, comenzando por el 1 y terminando en 0.

Ejemplo: { 1, 1/3, 1/9, 1/27, ... }

# Ejercicio 1: La Serie de Potencias de Sheldon

N = 10

serie = {1 / (3 ** i) for i in range(N)}

for numero in serie:
    print(numero)