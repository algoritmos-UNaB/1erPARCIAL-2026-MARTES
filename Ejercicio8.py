class Comic:
    def __init__(self, titulo, idcomic, fechapublicacion, precio, stock):
        self.titulo = titulo
        self.idcomic = idcomic
        self.fechapublicacion = fechapublicacion
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.idcomic} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, otro):
        return (
            isinstance(otro, Comic)
            and self.idcomic == otro.idcomic
            and self.titulo == otro.titulo
        )