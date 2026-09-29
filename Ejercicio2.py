# Biblioteca y metodos
class Biblioteca:
    def __init__(self):
        #la biblioteca vacia 
        self.libros = []
        #implemento los metodos
    def esta_vacia(self):
        len(self.libros) == 0
      return true 

    def anadir_libro(self, libro = None):   #anadir libros
        if libro is None:
            libro = input("¿Qué libro queres agregar?")
        self.libros.append(libro)

    def remover_libro(self, libro):
        if libro is None:
            libro = input("¿Qué libro queres remover?")
        if libros in self.libros:
            self.libros.remove(libro)

    #----Ejercicio 3----
    def leer_primer_libro(self):
        if not self.esta_vacia():
            return self.libros[0]
        return None

    def leer_Ultimo_libro(self):
        if not self.esta_vacia():
            return self:libros[-1]
        return None

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    #----Ejercicio 4---- le agrego los otros metodos
    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return f"Biblioteca con (len(self.libros)) libros: (self.libros)"
    
    def __eq__(self, otra_biblioteca):
        if isinstance(otra_biblioteca, Biblioteca):
            return self.libros == otra_biblioteca.libros
        return False

    def __add__(self, otra_biblioteca):
        # Combina los libros de dos bibliotecas en una nueva
        nueva_biblioteca = Biblioteca()
        if isinstance(otra_biblioteca, Biblioteca):
            nueva_biblioteca.libros = self.libros + otra_biblioteca.libros
        return nueva_biblioteca
        