class Biblioteca:
    
    def __init__(self):     # Crea una biblioteca vacía.
        self.libros = []

    def esta_vacia(self):               # Devuelve True si está vacía.
        return len(self._libros) == 0

    def agregar_libro(self, libro):     # Agrega un libro.
        self._libros.append(libro)

    def remover_libro(self, libro):     # Saca un libro. Si no está, da un aviso.
        if libro in self._libros:
            self._libros.remove(libro)
        else:
            print(f'"{libro}" no está en la biblioteca.' )

    def cantidad_libros(self):          # Cuantos libros hay.
        return len(self._libros)
    
    def __str__(self):                  # Muestra el estado de la biblioteca.
        if self.esta_vacia():
            return "Biblioteca vacia."
        return "Biblioteca: " + ", ".join(self._libros)
