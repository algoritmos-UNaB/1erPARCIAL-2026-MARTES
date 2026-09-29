class Biblioteca():
    def __init__(self):
        # Crea una biblioteca vacia
        self._libros = []

    # Identifica si la biblioteca se encuentra vacia
    def esta_vacia(self):
        return len(self._libros) == 0

    def agregar_libro(self, libro):
        # Anade libro a la coleccion
        self._libros.append(libro)
        self._libros.sort() # Ordena libros

    def remover_libro(self, libro):
        # Remover un libro de la biblioteca
        if libro in self._libros:
            self._libros.remove(libro)
        else:
            raise ValueError(f"El libro {libro} no se encuentra en la biblioteca.")
  
    def leer_primer_libro(self):
        # Retorna el primer libro de la lista
        if self.esta_vacia():
            raise IndexError(f"La biblioteca esta vacia")
        else:
            return self._libros[0]
    
    def leer_ultimo_libro(self):
    # Retorna el ultimo libro de la lista
        if self.esta_vacia():
            raise IndexError(f"La biblioteca esta vacia")
        else:
            return self._libros[-1]
    
    def insertar_al_principio(self, libro):
    # Agrega un libro al principio de la biblioteca
        self._libros.insert(0, libro)

    def agregar_al_final(self, libro):
    # Agrega un libro al final de la biblioteca
        self._libros.append(libro)

    def __len__(self):

        return len(self._libros)

    def __eq__(self, otra):
    # 2 bibliotecas son iguales si contienen los mismos libros
        if isinstance(otra, Biblioteca):
            return set(self._libros) == set(otra._libros)
        return False

    def __add__(self, otra: "Biblioteca"):
    # Crear una nueva biblioteca fusionando otras 2
        libros_nuevos = self._libros + otra._libros
        return Biblioteca(libros_nuevos)
      
    def __str__(self):
    # Visualizar elementos de la biblioteca
        return f"Biblioteca: {self._libros}"
    