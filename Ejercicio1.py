from fractions import Fraction
N = 10
Potencias = {Fractions(1, 3**k) for k in range (0, N)}
resultado_potencias = sorted(Potencias, reverse= True)