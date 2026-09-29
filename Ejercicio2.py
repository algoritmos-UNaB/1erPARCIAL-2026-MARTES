class Biblioteca:
    def __init__(self):
        self.libros = []

    def vacia(self):
        return len(self.libros) == 0

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    def listar_libros(self):
        return list(self.libros)

    def leer_primer_libro(self):
        if not self.vacia():
            return self.libros[0]
        return None  

    def leer_ultimo_libro(self):
        if not self.vacia():
            return self.libros[-1]
        return None  

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)

    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return f"Biblioteca: {self.libros}"

    def __eq__(self, segunda_biblioteca):
        if isinstance(segunda_biblioteca, Biblioteca):
            return self.libros == segunda_biblioteca.libros
        return False

    def __add__(self, segunda_biblioteca):
        nueva = Biblioteca()
        nueva.libros = self.libros + segunda_biblioteca.libros
        return nueva

