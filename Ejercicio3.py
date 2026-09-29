class Biblioteca:
    def __init__(self):
        self.libros = []

    def leerprimerlibro(self):
        return self.libros[0] if self.libros else None

    def leerultimolibro(self):
        return self.libros[-1] if self.libros else None

    def insertaralprincipio(self, libro):
        self.libros.insert(0, libro)

    def agregaralfinal(self, libro):
        self.libros.append(libro)