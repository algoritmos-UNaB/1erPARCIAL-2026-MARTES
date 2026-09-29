Ejercicio 2: La Biblioteca de Sheldon
Crear una clase Biblioteca. Una biblioteca es una colección homogénea y ordenada de libros (pueden utilizar una lista para representarla). La clase debe contener métodos para facilitar:

- Crear una biblioteca vacía.
- Identificar si una biblioteca está vacía o no.
- Añadir y remover libros de la biblioteca.

Importante: Pueden agregar más atributos y métodos, si lo consideran necesario.

class Biblioteca:

    def __init__(self):
        # Crear una biblioteca vacia
        self.libros = []

    def esta_vacia(self):
        # Devuelve true si no hay libros
        return len(self.libros) == 0


    def agregar_libro(self, libro):
        # Añadir un libro
        self.libros.append(libro)


    def remover_libro(self, libro):
        # Remover un libro
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print("El libro no se encuentra en la biblioteca")


    def mostrar_libros(self):
        # Mostrar los libros
        print(self.libros)


# Crear una biblioteca vacia
biblioteca = Biblioteca()


# Comprobar si esta vacio
print("¿La biblioteca esta vacia?" , biblioteca.esta_vacia())


# Agregar Libros
biblioteca.agregar_libro("Harry Potter")
biblioteca.agregar_libro("El Principito")
biblioteca.agregar_libro("Don Quijote")


# Mostrar Los Libros
biblioteca.mostrar_libros()


# Comprobar nuevamente si esta vacia
print("¿La biblioteca esta vacia?", biblioteca.esta_vacia())


# Remover un Libro
biblioteca.remover_libro("El Principito")


# Mostar los libros despues de remover
biblioteca.mostrar_libros()



Ejercicio 3: La Organización de la Biblioteca
Añadir a la clase Biblioteca los siguientes métodos:

- leer_primer_libro()
- leer_ultimo_libro()
- insertar_al_principio()
- agregar_al_final()

Nota: pensar en los parámetros que necesita cada método para realizar su trabajo y qué operación debe realizar.

class Biblioteca:

    def __init__(self):
        self.libros = []

    # Saber si la biblioteca esta vacia
    def esta_vacia(self):
        return len(self.libros) == 0

    # Añadir un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Remover un libro
    def remover_libro(self, libro):
        self.libros.remove(libro)

    # Leer el primer libro
    def leer_primer_libro(self):
        if self.esta_vacia():
            return "La biblioteca esta vacia"
        return self.libros[0]

    # Leer el ultimo libro
    def leer_ultimo_libro(self):
        if self.esta_vacia():
            return "La biblioteca esta vacia"
        return self.libros[-1]

    # Insertar un libro al principio
    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    # Agregar un libro al final
    def agregar_al_final(self, libro):
        self.libros.append(libro)


# Crear una biblioteca
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro("Harry Potter")
biblioteca.agregar_libro("El Principito")
biblioteca.agregar_libro("1984")

# Leer primer y ultimo libro
print("Primer libro:", biblioteca.leer_primer_libro())
print("Ultimo libro:", biblioteca.leer_ultimo_libro())

# Insertar un libro al principio
biblioteca.insertar_al_principio("Don Quijote")

# Agregar un libro al final
biblioteca.agregar_al_final("Cien años de soledad")

print("Primer libro despues de insertar:", biblioteca.leer_primer_libro())
print("Ultimo libro despues de agregar:", biblioteca.leer_ultimo_libro())

print("Libros de la biblioteca:", biblioteca.libros)

Ejercicio 4: La Representación de la Biblioteca
Sobrescribir los métodos __len__, __str__, __eq__, y __add__ de la clase Biblioteca.

class Biblioteca:

    def __init__(self):
        self.libros = []

    # Saber si la biblioteca esta vacia
    def esta_vacia(self):
        return len(self.libros) == 0

    # Agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Remover un libro
    def remover_libro(self, libro):
        self.libros.remove(libro)

    # Leer el primer libro
    def leer_primer_libro(self):
        if self.esta_vacia():
            return "La biblioteca esta vacia"
        return self.libros[0]

    # Leer el ultimo libro
    def leer_ultimo_libro(self):
        if self.esta_vacia():
            return "La biblioteca esta vacia"
        return self.libros[-1]

    # Insertar un libro al principio
    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    # Agregar un libro al final
    def agregar_al_final(self, libro):
        self.libros.append(libro)

    # Devolver la cantidad de libros
    def __len__(self):
        return len(self.libros)

    # Mostrar la biblioteca
    def __str__(self):
        return str(self.libros)

    # Comparar dos bibliotecas
    def __eq__(self, otra_biblioteca):
        return self.libros == otra_biblioteca.libros

    # Sumar dos bibliotecas
    def __add__(self, otra_biblioteca):
        nueva_biblioteca = Biblioteca()
        nueva_biblioteca.libros = self.libros + otra_biblioteca.libros
        return nueva_biblioteca


# Crear la primera biblioteca
biblioteca1 = Biblioteca()

biblioteca1.agregar_libro("Harry Potter")
biblioteca1.agregar_libro("El Principito")
biblioteca1.agregar_libro("1984")

# Crear la segunda biblioteca
biblioteca2 = Biblioteca()

biblioteca2.agregar_libro("Don Quijote")
biblioteca2.agregar_libro("Cien años de soledad")

# Mostrar las bibliotecas
print("Biblioteca 1:", biblioteca1)
print("Biblioteca 2:", biblioteca2)

# Mostrar cantidad de libros
print("Cantidad de libros de la biblioteca 1:", len(biblioteca1))
print("Cantidad de libros de la biblioteca 2:", len(biblioteca2))

# Comparar las bibliotecas
print("Son iguales:", biblioteca1 == biblioteca2)

# Sumar las dos bibliotecas
biblioteca3 = biblioteca1 + biblioteca2

print("Biblioteca nueva:", biblioteca3)
print("Cantidad de libros de la biblioteca nueva:", len(biblioteca3))