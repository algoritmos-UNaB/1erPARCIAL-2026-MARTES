#(3pt.) Ejercicio 2: La Biblioteca de Sheldon

#Crear una clase Biblioteca. Una biblioteca es una colección homogénea y ordenada de libros 
#(pueden utilizar una lista para representarla). La clase debe contener métodos para facilitar:

#- Crear una biblioteca vacía. -
# libros lista

#- Identificar si una biblioteca está vacía o no.
# Metodos = vacia

#- Añadir y remover libros de la biblioteca.
# meotodos: agregar_libro, remover_libro

#Importante: Pueden agregar más atributos y métodos, si lo consideran necesario.
# listar_libros
###############################################################################
#Añadir a la clase Biblioteca los siguientes métodos:

#- leer_primer_libro()
#- leer_ultimo_libro()
#- insertar_al_principio()
#- agregar_al_final()

#Nota: pensar en los parámetros que necesita cada método para realizar su trabajo y 
#qué operación debe realizar.

###############################################################################
#Sobrescribir los métodos: __len__, __str__, __eq__, y __add__ de la clase Biblioteca.

class biblioteca:
    def __init__(self):
        self.libros = []
    
    def vacia(self):
        return len(self.libros) == 0

    def agregar_libro(self, libro):
        if libro in self.libros:
            self.libros.append(libro)
    
    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
    
    def listar_libros(self):
        return self.libros

    def leer_primer_libro(self):
        if not self.vacia():
            return self.libro[0]

    def leer_ultimo_libro(self):
        if not self.vacia():
            return self.libro[-1]

    def insertar_al_principio(self, libro):
        self.libros.insert(0,libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)

    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return str(self.libros)
    
    def __eq__(self, alter_biblioteca):
        return self.libros == alter_biblioteca.libros

    def __add__(self, alter_biblioteca):
        biblioteca_nueva = biblioteca()
        biblioteca_nueva.libros = self.libros + alter_biblioteca.libros
        return biblioteca_nueva