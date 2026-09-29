#Ejercicio 2: La biblioteca de Sheldon.
class Biblioteca (object):
    def __init__(self):
        self.libros = []
    def esta_vacia (self):
        return len(self.libros) == 0
    def agregar (self, libro):
        self.libros.append (libro)    
    def remover (self, libro):
        if libro not in self.libros:
            raise ValueError ("Este libro no está en la biblioteca.")
        self.libros.remove (libro)
    def __len__(self):
        return len(self.libros)
        def __str__(self)
        return str(self.libros)

#Ejercicio 3: La organización de la biblioteca.
    def leer_primer_libro(self)
        if self.esta_vacia():
            raise IndexError ("La biblioteca está vacía.")
        return self.libros [0]
    def leer_ultimo_libro(self):
        if self.esta_vacia():
            raise IndexError ("La biblioteca está vacía.")
        return self.libros [-1]
    def insertar_al_principio(self,libro):
        self.libros.insert(0, libro)
    def agregar_al_final(self, libro):
        self.libros.append(libro)

#Ejercicio 4: La representación de la biblioteca.
    def __len__(self):
        return len(self.libros)
    def __str__(self):
        return "Biblioteca: " + str(self.libros)
    def __eq__(self, other):
        if not isinstance (other, Biblioteca):
            return False
        return self.libros == other.libros 
    def __add__(self, other):
        if not isinstance(other, Biblioteca):
            raise TypeError ("Solo se puede sumar una biblioteca con otra biblioteca.")
        nueva = Biblioteca()
        nueva.libros = self.libros + other.libros
        return nueva
        