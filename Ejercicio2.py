class Biblioteca:
    def __init__(self):
        self.libros = []

    def esta_vacia(self):
        return len(self.libros) == 0

    def agregar_libro (self, libro):
        self.libros.append(libro)

    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print(f"El libro '{libro}' no se encuentra en la biblioteca")
#ejercicio 3

    def leer_primer_libro(self):
        if self.esta_vacia():
            return None
        return self.libros[0]

    def leer_ultimo_libro(self):
        if self.esta_vacia():
            return None
        return self.libros[-1]

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)

#ejercicio 4

    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return f"Biblioteca con {len(self.libros)} libros: {self.libros}"
    
    def __eq__(self, otra_biblioteca):
        if isinstance(otra_biblioteca, Biblioteca):
            return self.libros == otra_biblioteca.libros
        return False

    def __add__(self, otra_biblioteca):
        nueva_biblioteca = Biblioteca()
        if isinstance(otra_biblioteca, Biblioteca):
            nueva_biblioteca.libros = self.libros + otra_biblioteca.libros
        return nueva_biblioteca