from datetime import date

class Comic:
    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    # ejercicio 7
    def modificar(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_desde_referencia(self, fecha_referencia):
        dias = (self.fecha_publicacion - fecha_referencia).days
        if dias < 0:
            print(self.titulo, "es más antiguo que la fecha de referencia")
            self.stock = 0
            return None
        return dias

    # ejercicio 8
    def __str__(self):
        return ("Comic: " + self.titulo + " | ID: " + str(self.id_comic) +
                " | Precio: $" + str(self.precio) + " | Stock: " + str(self.stock))

    def __eq__(self, otro):
        return self.id_comic == otro.id_comic and self.titulo == otro.titulo

if __name__ == "__main__":
    c1 = Comic("The Flash #1", 456, date(2024, 5, 10), 5.99, 25)
    c2 = Comic("The Flash #1", 456, date(2023, 1, 1), 9.99, 3)
    print(c1)
    print(c1 == c2)  # True
    print(c1.dias_desde_referencia(date(2024, 1, 1)))  # 130
    c1.dias_desde_referencia(date(2025, 1, 1))  # avisa y stock = 0
    print(c1.stock)  # 0