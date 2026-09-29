#Nombre y apellido: Leandro Leonel Veliz
#Email: leandro.leonel.veliz@gmail.com
#Comisión: 3

def contar_libros_recursivo(coleccion):
    # Verificamos si recibimos el objeto Biblioteca para extraer su lista interna.
    # En las siguientes llamadas recursivas, recibiremos directamente una lista.
    if type(coleccion) is list:
        lista = coleccion
    else:
        lista = coleccion.libros

    # Caso base: si la lista está vacía, no hay más libros para contar
    if not lista:
        return 0
        
    # Llamada recursiva: sumamos 1 (por el primer libro) y pasamos el resto de la lista
    return 1 + contar_libros_recursivo(lista[1:])