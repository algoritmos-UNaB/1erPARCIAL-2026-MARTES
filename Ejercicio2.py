class Biblioteca:
    def __init__(self, nombre="Biblioteca General"):
        self.nombre = nombre
        self.libros = []

    def esta_vacia(self) -> bool:
        return len(self.libros) == 0

    def agregar_libro(self, libro: str):
        self.agregar_al_final(libro)

    def remover_libro(self, libro: str) -> bool:
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"Libro '{libro}' removido con éxito.")
            return True
        else:
            print(f"El libro '{libro}' no se encuentra en la biblioteca.")
            return False

    def leer_primer_libro(self) -> str:
        if self.esta_vacia():
            print("La biblioteca está vacía.")
            return None
        return self.libros[0]

    def leer_ultimo_libro(self) -> str:
        if self.esta_vacia():
            print("La biblioteca está vacía.")
            return None
        return self.libros[-1]

    def insertar_al_principio(self, libro: str):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro: str):
        self.libros.append(libro)

    
    def __len__(self) -> int:
        return len(self.libros)

    def __str__(self) -> str:
        if self.esta_vacia():
            return f"Biblioteca '{self.nombre}' (Vacía)"
        
        lista_formateada = "\n  - ".join(self.libros)
        return f"Biblioteca '{self.nombre}' ({len(self)} libros):\n  - {lista_formateada}"

    def __eq__(self, otra_biblioteca) -> bool:
        if isinstance(otra_biblioteca, Biblioteca):
            return self.libros == otra_biblioteca.libros
        return False

    def __add__(self, otra_biblioteca):
        if isinstance(otra_biblioteca, Biblioteca):
            nuevo_nombre = f"Unión de {self.nombre} y {otra_biblioteca.nombre}"
            nueva_biblio = Biblioteca(nuevo_nombre)
            nueva_biblio.libros = self.libros + otra_biblioteca.libros
            return nueva_biblio
        else:
            raise TypeError("Solo se pueden sumar objetos de la clase Biblioteca")

if __name__ == "__main__":
    b1 = Biblioteca("Sede Central")
    b1.agregar_al_final("Cien años de soledad")
    b1.agregar_al_final("El Aleph")

    b2 = Biblioteca("Sede Anexa")
    b2.agregar_al_final("Estructuras de Datos")

    print(f"Cantidad de libros en b1: {len(b1)}")

    print("\n--- Representación en texto (__str__) ---")
    print(b1)

    b3 = Biblioteca("Sede Copia")
    b3.agregar_al_final("Cien años de soledad")
    b3.agregar_al_final("El Aleph")

    print("\n--- Comparación (__eq__) ---")
    print(f"¿b1 es igual a b2?: {b1 == b2}")
    print(f"¿b1 es igual a b3?: {b1 == b3}")

    print("\n--- Suma de Bibliotecas (__add__) ---")
    b_combinada = b1 + b2
    print(b_combinada)
