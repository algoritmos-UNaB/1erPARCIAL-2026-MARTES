from fractions import Fraction

n = 10  # cantidad de elementos
conjunto = {Fraction(1, 3**k) for k in range(n)}

print(sorted(conjunto, reverse=True))