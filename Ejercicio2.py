class Biblioteca:
    def __init__(self):
        self.libros = []

    def esta_vacia(self):
        return len(self.libros) == 0

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def remover_libro(self, libro):
        self.libros.remove(libro)

    def leer_primer_libro(self):
        return self.libros[0]

    def leer_ultimo_libro(self):
        return self.libros[-1]

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)
            def __len__(self):
        return len(self.libros)

    def __str__(self):
        return str(self.libros)

    def __eq__(self, otra_biblioteca):
        return self.libros == otra_biblioteca.libros

    def __add__(self, otra_biblioteca):
        nueva_biblioteca = Biblioteca()
        nueva_biblioteca.libros = self.libros + otra_biblioteca.libros
        return nueva_biblioteca