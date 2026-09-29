
class Biblioteca:
    def __init__(self):
        self.libros[]
    def biblioteca_vacia(self):
        return len(self.libros) == 0
    def agregar_l(self, libro):
        self.libros.append(libro)
    def quitar_libro(self, libro):
        if libro in self.libros:
            self.libros.romeve(libros)
        else:
            ValueError(f"El libro {libro} no se encuentra en la biblioteca")

    #ejercicio 3
    def leer_primer_libro(self):
        if not self.biblioteca_vacia():
            return self.libros[0]
        else: 
            return "la biblioteca esta vacia"
    def leer_ultimo_libro(self):
        if not self.libreria_vacia():
            return self.libros[-1]
        else: 
            return "la biblioteca esta vacia"
    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)
    def agregar_al_final(sefl, libro):
        self.libros.append(libro)
    
    #ejercicio 4
    def __len__(self):
        return len(self.libros)
    def __str__(self):
        if self.biblioteca_vacia():
            return "La biblioteca esta vacia"
        else: f"la biblioteca tiene {self.libros}"
    def __eq__(self, otra_b):
        if isinstance(otra_b, Biblioteca):
            return self.libros == otra_biblioteca.libros
        else: 
            return False
    def __add__(self, otra_biblioteca):
        nueva_biblioteca= Biblioteca()
        nueva_biblioteca.libros = self.libros + otra_biblioteca.libros
        return nueva_biblioteca



        

        
        
