class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def esta_vacia(self):
        return len(self.libros) == 0
    
    def agregar_libros(self, libro):
        self.libros.append(libro)

    def remove_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

b = Biblioteca()

print(b.esta_vacia())

b.agregar_libro("El selor de los Anillos")
b.agregar_libro("1984")

print(b.esta_vacia())
b.remover_libro("984")
print(b.libros)