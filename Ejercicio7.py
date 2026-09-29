from datetime import date

class Comic:
    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    def modificar_datos(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo

        if precio is not None:
            self.precio = precio

        if stock is not None:
            self.stock = stock

    def calcular_dias(self, fecha_referencia):
        diferencia = (self.fecha_publicacion - fecha_referencia).days

        if diferencia < 0:
            print("El comic es más antiguo que la fecha de referencia.")
            self.stock = 0

        return abs(diferencia)


    def __str__(self):
        return (f"Comic: {self.titulo} | "
                f"ID: {self.id_comic} | "
                f"Precio: ${self.precio} | "
                f"Stock: {self.stock}")

    
    def __eq__(self, otro):
        return (self.id_comic == otro.id_comic and
                self.titulo == otro.titulo)


comic1 = Comic(
    "The Flash #1",
    456,
    date(2023, 5, 20),
    5.99,
    25
)

comic2 = Comic(
    "The Flash #1",
    456,
    date(2024, 1, 1),
    8.50,
    10
)

comic3 = Comic(
    "Batman #10",
    789,
    date(2023, 3, 10),
    7.50,
    15
)


print(comic1)

print(comic1 == comic2)
print(comic1 == comic3)