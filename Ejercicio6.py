class Biblioteca:
    
    def __init__(self):                 # Crea una biblioteca vacía.
        self.libros = []

    def esta_vacia(self):               # Devuelve True si está vacía.
        return len(self._libros) == 0

    def agregar_al_final(self, libro):  # Agrega un libro al final de la biblioteca.
        self._libros.append(libro)

    def insertar_al_principio(self, libro):     # Agrega un libro al principio de la biblioteca.
        self._libros.insert(0, libro)

    def leer_primer_libro(self):        # Devuelve el primer libro.
        if self.esta_vacia():
            return None
        return self._libros[0]

    def leer_ultimo_libro(self):        # Devuelve el último libro.
        if self.esta_vacia():
            return None
        return self._libros[-1]

    def remover_libro(self, libro):     # Saca un libro. Si no está, da un aviso.
        if libro in self._libros:
            self._libros.remove(libro)
        else:
            print(f'"{libro}" no está en la biblioteca.' )

    def cantidad_libros(self):          # Cuantos libros hay.
        return len(self._libros)
    
    def __len__(self):                  # Permite usar len(biblioteca) en vez de biblioteca.cantidad_libros().
        return len(self.libros)

    def __str__(self):                  # Muestra el estado de la biblioteca.
        if self.esta_vacia():
            return "Biblioteca vacia."
        return "Biblioteca: " + ", ".join(self._libros)

    def __eq__(self, otra):             # Permite comparar dos bibliotecas.         
        if not isinstance(otra, Biblioteca):
            return False
        return self.libros == otra._libros

    def __add__(self, otra):            # Permite sumar dos bibliotecas.
        nueva = Biblioteca()
        nueva._libros = self._libros + otra._libros
        return nueva

def contar_libros_recursivo(Biblioteca): # Ejercicio 6: cuenta la cantidad total de libros en una biblioteca, usando recursión.
    return _contar_recursivo(biblioteca._libros)             

def _contar_recursivo(lista):
    if not lista:
        return 0
    return 1 + _contar_recursivo(lista[1:])