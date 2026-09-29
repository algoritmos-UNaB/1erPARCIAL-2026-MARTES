Ejercicio 5: El Conteo de Libros de Leonard (Iterativo)
Implementar una función iterativa que calcule la cantidad total de libros en una biblioteca (de la clase Biblioteca definida con anterioridad).

class Biblioteca:

    def __init__(self):
        self.libros = []

    # Saber si la biblioteca esta vacia
    def esta_vacia(self):
        return len(self.libros) == 0

    # Agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Remover un libro
    def remover_libro(self, libro):
        self.libros.remove(libro)

    # Leer el primer libro
    def leer_primer_libro(self):
        if self.esta_vacia():
            return "La biblioteca esta vacia"
        return self.libros[0]

    # Leer el ultimo libro
    def leer_ultimo_libro(self):
        if self.esta_vacia():
            return "La biblioteca esta vacia"
        return self.libros[-1]

    # Insertar un libro al principio
    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    # Agregar un libro al final
    def agregar_al_final(self, libro):
        self.libros.append(libro)

    # Cantidad de libros
    def __len__(self):
        return len(self.libros)

    # Mostrar la biblioteca
    def __str__(self):
        return str(self.libros)

    # Comparar bibliotecas
    def __eq__(self, otra_biblioteca):
        return self.libros == otra_biblioteca.libros

    # Sumar dos bibliotecas
    def __add__(self, otra_biblioteca):
        nueva_biblioteca = Biblioteca()
        nueva_biblioteca.libros = self.libros + otra_biblioteca.libros
        return nueva_biblioteca


# Funcion iterativa para contar los libros
def contar_libros(biblioteca):
    cantidad = 0

    for libro in biblioteca.libros:
        cantidad += 1

    return cantidad


# Crear una biblioteca
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro("Harry Potter")
biblioteca.agregar_libro("El Principito")
biblioteca.agregar_libro("1984")
biblioteca.agregar_libro("Don Quijote")

# Contar los libros
print("Cantidad total de libros:", contar_libros(biblioteca))