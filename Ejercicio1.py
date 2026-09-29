N = 10
conjunto_potencias = [3**(-n) for n in range(N)]

print("Primeros 10 elementos del conjunto:")
print(conjunto_potencias)

print("\nEn formato de fracción racional:")
from fractions import Fraction
conjunto_fracciones = [Fraction(1, 3**n) for n in range(N)]
for x in conjunto_fracciones:
    print(x, end=", ")
print("...")

def generar_potencias_sheldon(limite_terminos=15):
    n = 0
    while n < limite_terminos:
        valor = 3**(-n)
        yield valor
        n += 1

for n, valor in enumerate(generar_potencias_sheldon(10)):
    print(f"3^(-{n}) = {valor}")
