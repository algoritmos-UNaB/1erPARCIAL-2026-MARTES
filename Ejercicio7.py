Ejercicio 7: El Inventario de Comics de Stuart
Definir una clase Comic que represente un cómic en venta en la tienda de Stuart. Contiene los datos:

titulo: 'string'
id_comic: 'integer'
fecha_publicacion: date (importar datetime)
precio: 'float'
stock: 'integer'
La clase debe contener métodos para facilitar:

Cambiar uno o varios datos del cómic (título, precio, stock).
Calcular en cuántos días se publicó un cómic desde una fecha de referencia. Si el método detecta que el cómic es más antiguo que la fecha de referencia, deberá informar al usuario y marcar el stock como 0.

from datetime import date


class Comic:

    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    # Cambiar el titulo
    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    # Cambiar el precio
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Cambiar el stock
    def cambiar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    # Calcular los dias desde la fecha de referencia
    def dias_desde_fecha(self, fecha_referencia):

        if self.fecha_publicacion < fecha_referencia:
            print("El comic es mas antiguo que la fecha de referencia.")
            self.stock = 0
            return 0

        diferencia = self.fecha_publicacion - fecha_referencia
        return diferencia.days

    # Mostrar los datos del comic
    def __str__(self):
        return (
            "Titulo: " + self.titulo +
            "\nID: " + str(self.id_comic) +
            "\nFecha de publicacion: " + str(self.fecha_publicacion) +
            "\nPrecio: $" + str(self.precio) +
            "\nStock: " + str(self.stock)
        )


# Crear un comic
comic1 = Comic(
    "Spider-Man",
    101,
    date(2026, 9, 20),
    5000.50,
    10
)

# Mostrar los datos
print(comic1)

# Cambiar datos
comic1.cambiar_titulo("Spider-Man: Nuevo comienzo")
comic1.cambiar_precio(5500.00)
comic1.cambiar_stock(15)

print("\nDespues de modificar:")
print(comic1)

# Fecha de referencia
fecha_referencia = date(2026, 9, 25)

# Calcular dias
dias = comic1.dias_desde_fecha(fecha_referencia)

print("\nDias desde la fecha de referencia:", dias)
print("Stock actual:", comic1.stock)


Ejercicio 8: La Etiqueta de los Comics (Sobrecarga de Métodos)
Sobrecargar los siguientes métodos en la clase Comic:

__str__: Para representar el cómic de forma legible (ej: "Comic: The Flash #1 | ID: 456 | Precio: $5.99 | Stock: 25").
__eq__: Para comparar si dos cómics son iguales basándose en su id_comic y titulo.

from datetime import date


class Comic:

    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    # Cambiar el titulo
    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    # Cambiar el precio
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Cambiar el stock
    def cambiar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    # Calcular los dias desde una fecha de referencia
    def dias_desde_fecha(self, fecha_referencia):

        if self.fecha_publicacion < fecha_referencia:
            print("El comic es mas antiguo que la fecha de referencia.")
            self.stock = 0
            return 0

        diferencia = self.fecha_publicacion - fecha_referencia
        return diferencia.days

    # Representar el comic de forma legible
    def __str__(self):
        return (
            "Comic: " + self.titulo +
            " | ID: " + str(self.id_comic) +
            " | Precio: $" + str(self.precio) +
            " | Stock: " + str(self.stock)
        )

    # Comparar dos comics
    def __eq__(self, otro_comic):
        return (
            self.id_comic == otro_comic.id_comic
            and self.titulo == otro_comic.titulo
        )


# Crear dos comics
comic1 = Comic(
    "The Flash",
    456,
    date(2026, 9, 20),
    5.99,
    25
)

comic2 = Comic(
    "The Flash",
    456,
    date(2026, 9, 20),
    5.99,
    10
)

# Mostrar los comics
print(comic1)
print(comic2)

# Comparar los comics
print("Los comics son iguales:", comic1 == comic2)