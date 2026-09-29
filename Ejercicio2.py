#ejercicio 2 (abajo)
class Biblioteca:
    def __init__(self):
        self.libros = []

    def esta_vacia(self):
        return len(self.libros) == 0

    def agregar(self, libro):
        self.libros.append(libro)

    def remover(self, libro):
        self.libros.remove(libro)
    #ejercicio 3 (abajo)
    def leer_primer_libro(self):
        return self.libros[0]

    def leer_ultimo_libro(self):
        return self.libros[-1]

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)
    #ejercicio 4 (abajo)
    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return str(self.libros)

    def __eq__(self, otra):
        return self.libros == otra.libros

    def __add__(self, otra):
        nueva = Biblioteca()
        nueva.libros = self.libros + otra.libros
        return nueva