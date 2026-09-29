#(1pt.) Ejercicio 1: La Serie de Potencias de Sheldon
#Generar un conjunto por compresión que contenga los números 
#racionales que son potencia de 3, comenzando por el 1 y terminando en 0.

#Ejemplo: { 1, 1/3, 1/9, 1/27, ... }


potencia = {1 / (3 ** i) if i < 10 else 0 for i in range(11)}
