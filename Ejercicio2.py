class Biblioteca:
    def __init__(self):
        self.libros = []

    def esta_vacia(self):
        return len(self.libros) == 0

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)