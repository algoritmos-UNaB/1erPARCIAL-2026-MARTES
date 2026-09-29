class Biblioteca:
    def __init__(self):
        self.libros = []

    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return str(self.libros)

    def __eq__(self, otra):
        return isinstance(otra, Biblioteca) and self.libros == otra.libros

    def __add__(self, otra):
        nueva = Biblioteca()
        nueva.libros = self.libros + otra.libros
        return nueva