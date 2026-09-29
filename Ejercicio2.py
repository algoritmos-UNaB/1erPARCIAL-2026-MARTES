class Biblioteca:
    class _Libro():
        #Clase Libro
        def __init__(self, nombre, autor):
            self._nombre = nombre
            self._autor = autor

    def __init__(self):
        self._libros = []
        self._size = 0
    
    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def agregar_libro(self, libro_nom, autor):
        #Agregamos un nuevo libro a la lista
        nuevo_lib = self._Libro(libro_nom, autor)
        self._libros.append(nuevo_lib)
        self._size += 1
    
    def borrar_libro(self, libro_nom, autor):
        #Borramos de la lista un libro deseado y si no existe informamos del error
        for lib in range(self._size):
            lib_candidato = self._libros[lib]
            if lib_candidato._nombre == libro_nom and lib_candidato._autor == autor:
                self._libros.pop(lib)
                self._size -= 1
                return
        print("El libro no existe en la biblioteca")
    
    def leer_primer_libro(self):
        #Si la biblioteca no esta vacia, devolvemos el primer libro
        if self.is_empty():
            print("La biblioteca esta vacia")
        else:
            primer_lib = self._libros[0]
            return primer_lib
    
    def leer_ultimo_libro(self):
        #Si la biblioteca no esta vacia, devolvemos el ultimo libro
        if self.is_empty():
            print("La biblioteca esta vacia")
        else:
            ultimo_lib = self._libros[self._size - 1]
            return ultimo_lib

    def insertar_al_principio(self, lib_nom, autor):
        #Agregamos un libro al inicio de la lista
        if self.is_empty():
            self.agregar_libro(lib_nom, autor)
        else:
            nuevo_lib = self._Libro(lib_nom, autor)
            self._libros.insert(0, nuevo_lib)
            self._size += 1

    def agregar_al_final(self, lib_nom, autor):
        #Agregamos un libro al final de la bibliota, como la funcion agregar_libro() ya hace esto
        #por defecto,simplemente la llamamos
        self.agregar_libro(lib_nom, autor)

    def __len__(self):
        return self._size

    def __str__(self):
        if self.is_empty():
            contenido = "La biblioteca esta vacia"
        else:
            contenido = "Los libros de la biblioteca son: \n"
            for i in range(self._size):
                lib = self._libros[i]
                contenido += f"Libro: {lib._nombre}, Autor: {lib._autor}\n"
        return contenido

    def __eq__(self, seg_biblio):
        #Si tienen distinto tamanio, seran trivialmente distintas
        if self._size != seg_biblio._size:
            return False
        #Comparamos todos los libros de una con todos los libros de otra y si alguno es distinto
        #devolvemos false, consideramos que un orden distinto representa una biblioteca distinta
        else:
            for x in range(self._size):
                lib = self._libros[x]
                seg_lib = self._libros[x]
                if lib._nombre != seg_lib._nombre or lib._autor != seg_lib._autor:
                    return False
            #si ningun libro es diferente son iguales
            return True

    def __add__(self, seg_biblio):
        if seg_biblio.is_empty():
            return self
        else:
            for x in range(seg_biblio._size):
                lib = seg_biblio._libros[x]
                self.agregar_al_final(lib._nombre, lib._autor)
            return self
                     

            
    
    

