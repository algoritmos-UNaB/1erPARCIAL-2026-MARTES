 Ejercicio 9: La Gestión de la Tienda de Comics
Crear una clase TiendaComics, la cual estará representada mediante varias listas de objetos del tipo Comic. Cada lista corresponde a una sección de la tienda (ej: "DC Comics", "Marvel", "Independientes").

La clase debe contener métodos para facilitar:

Controlar el stock de cómics (añadir un nuevo cómic a una sección, remover un cómic del inventario, actualizar stock).
Calcular cuántos cómics tienen stock crítico (menor o igual a 3) y removerlos del inventario (simulando que Stuart los retira por falta de demanda).

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

    # Mostrar el comic
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


class TiendaComics:

    def __init__(self):
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    # Agregar un comic a una seccion
    def agregar_comic(self, comic, seccion):
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
        else:
            print("La seccion no existe.")

    # Remover un comic del inventario
    def remover_comic(self, comic, seccion):
        if seccion in self.secciones:
            if comic in self.secciones[seccion]:
                self.secciones[seccion].remove(comic)
            else:
                print("El comic no se encuentra en la seccion.")
        else:
            print("La seccion no existe.")

    # Actualizar el stock de un comic
    def actualizar_stock(self, comic, seccion, nuevo_stock):
        if seccion in self.secciones:
            for c in self.secciones[seccion]:
                if c == comic:
                    c.cambiar_stock(nuevo_stock)
                    return

            print("El comic no se encuentra en la seccion.")
        else:
            print("La seccion no existe.")

    # Contar y remover comics con stock critico
    def retirar_stock_critico(self):
        cantidad = 0

        for seccion in self.secciones:
            comics_a_remover = []

            for comic in self.secciones[seccion]:
                if comic.stock <= 3:
                    comics_a_remover.append(comic)
                    cantidad += 1

            for comic in comics_a_remover:
                self.secciones[seccion].remove(comic)

        return cantidad

    # Mostrar todos los comics
    def mostrar_inventario(self):
        for seccion in self.secciones:
            print("\n" + seccion + ":")

            for comic in self.secciones[seccion]:
                print(comic)


# Crear comics
comic1 = Comic(
    "The Flash",
    456,
    date(2026, 9, 20),
    5.99,
    25
)

comic2 = Comic(
    "Batman",
    789,
    date(2026, 9, 15),
    7.50,
    3
)

comic3 = Comic(
    "Spider-Man",
    123,
    date(2026, 9, 10),
    6.50,
    2
)

comic4 = Comic(
    "Comic Independiente",
    555,
    date(2026, 9, 5),
    4.99,
    10
)


# Crear la tienda
tienda = TiendaComics()

# Agregar comics a las secciones
tienda.agregar_comic(comic1, "DC Comics")
tienda.agregar_comic(comic2, "DC Comics")
tienda.agregar_comic(comic3, "Marvel")
tienda.agregar_comic(comic4, "Independientes")

# Mostrar inventario
print("INVENTARIO INICIAL")
tienda.mostrar_inventario()

# Actualizar stock
tienda.actualizar_stock(comic1, "DC Comics", 20)

print("\nDESPUES DE ACTUALIZAR EL STOCK")
tienda.mostrar_inventario()

# Retirar comics con stock critico
cantidad = tienda.retirar_stock_critico()

print("\nCantidad de comics retirados:", cantidad)

# Mostrar inventario final
print("\nINVENTARIO FINAL")
tienda.mostrar_inventario()