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
        return (f"Comic: {self.titulo}, "
                f"ID: {self.id_comic}, "
                f"Precio: ${self.precio}, "
                f"Stock: {self.stock}")
                
comic1 = Comic(
    "Spider-Man",
    101,
    date(2020, 5, 15),
    1500.50,
    10
)

print(comic1)

comic1.modificar_datos(precio=1800.75, stock=5)

print(comic1)

fecha_ref = date(2022, 1, 1)

dias = comic1.calcular_dias(fecha_ref)

print("Días de diferencia:", dias)
print("Stock actual:", comic1.stock)