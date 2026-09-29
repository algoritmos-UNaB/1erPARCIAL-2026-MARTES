from datetime import date

class Comic():
    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = str(titulo)
        self.id_comic = int(id_comic)
        self.fecha_publicacion = date(fecha_publicacion)
        self.precio = float(precio)
        self.stock = int(stock)

    def modificar_datos(self, titulo=None, precio=None, stock=None):
        # Permite modificar datos
        if titulo is not None:
            self.titulo = str(titulo)
        if precio is not None:
            self.precio = float(precio)
        if stock is not None:
            self.stock = int(stock)

    def dias_publ_comic(self, fecha_referencia: date)
    # Calcula si un comic es mas antiguo o no, a partir de una fecha de referencia
        if self.fecha_publicacion < fecha_referencia:
            self.stock = 0
            print("Aviso: El comic es mas antiguo que la fecha de referencia. Se modifico el stock en 0")
            dias = (fecha_referencia - self.fecha_publicacion).days
            return dias
        else:
            dias = (self.fecha_publicacion - fecha_referencia).days
            return dias
    
    