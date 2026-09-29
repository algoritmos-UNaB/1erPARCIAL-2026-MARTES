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


# Ejemplo de uso
b = Biblioteca()

b.insertar_al_principio("Don Quijote")
b.agregar_al_final("El Señor de los Anillos")
b.agregar_al_final("1984")

print(b.leer_primer_libro())  # Don Quijote
print(b.leer_ultimo_libro())  # 1984
print(b.libros)
