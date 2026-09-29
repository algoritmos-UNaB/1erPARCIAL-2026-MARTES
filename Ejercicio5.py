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

    def leer_primer_libro(self):
        if not self.esta_vacia():
            return self.libros[0]

    def leer_ultimo_libro(self):
        if not self.esta_vacia():
            return self.libros[-1]

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)

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


def contar_libros(biblioteca):
    contador = 0

    for libro in biblioteca.libros:
        contador += 1

    return contador


b1 = Biblioteca()
b1.agregar_al_final("Don Quijote")
b1.agregar_al_final("1984")
b1.agregar_al_final("El Hobbit")

print("Cantidad total de libros:", contar_libros(b1))