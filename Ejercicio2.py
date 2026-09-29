class Biblioteca:
    def __init__(self):
        self.libros = [] 

    def esta_vacia(self):
        """Identifica si la biblioteca está vacía o no."""
        return len(self.libros) == 0

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

# Metodos adiccionales para la clase Biblioteca

    def mostrar_libros(self):
        if self.esta_vacia():
            print("La biblioteca está vacía.")
        else:
            print("--- Inventario de la Biblioteca ---")
            for indice, libro in enumerate(self.libros, start=1):
                print(f"{indice}. {libro}")
            
    def cantidad_libros(self):
        return len(self.libros)
    
    def ordenar_alfabeticamente(self):
        if not self.esta_vacia():
            self.libros.sort()
            print("La biblioteca ha sido ordenada alfabéticamente.")
        else:
            print("No hay libros para ordenar.")

# Ejercicio 3

    def leer_primer_libro(self):
        # Corrección: Validación de biblioteca vacía para evitar IndexError
        if not self.esta_vacia():
            primer_libro = self.libros[0]
            return primer_libro
        return None

    def leer_ultimo_libro(self):
        # Corrección: Validación de biblioteca vacía para evitar IndexError
        if not self.esta_vacia():
            ultimo_libro = self.libros[-1]
            return ultimo_libro
        return None

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)

# Ejercicio 4

# Sobrecarga de la función len()
    def __len__(self):
        # Corrección: Atributo correcto es self.libros, no self._libros
        return len(self.libros)

# Sobrecarga de la función print() y str()
    def __str__(self):
        if len(self) == 0:
            return "Biblioteca vacía."
        return f"Biblioteca ({len(self)} libros): {self.libros}"

# Sobrecarga del operador de igualdad (==)
    def __eq__(self, otro):
        if type(otro) != type(self):
            raise NotImplementedError('No se puede comparar una Biblioteca con un ' + str(type(otro)))
    
        return self.libros == otro.libros

# Sobrecarga del operador de suma (+)
    def __add__(self, otro):
        if type(otro) != type(self):
            raise TypeError("Solo se pueden sumar dos objetos de tipo Biblioteca.")
        
        nueva_biblioteca = Biblioteca()
        
        nueva_biblioteca.libros = self.libros + otro.libros
        
        return nueva_biblioteca