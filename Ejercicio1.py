from fraction import Fraction

N = 10 # Terminos que se van a generar.

conjunto = {Fraction(1/3) ** n for n in range(N)}
