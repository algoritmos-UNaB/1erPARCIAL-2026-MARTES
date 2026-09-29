#secuencia de potencia de 3
n = 10  # número de términos a generar
conjunto_potencias = {3**(-k) for k in range(n)}

# Imprimir los valores numéricos float:
print(conjunto_potencias)

#como fracciones (1/3, 1/9, etc.):
from fractions import Fraction

conjunto_fracciones = {Fraction(1, 3**k) for k in range(n)}
print(conjunto_fracciones)