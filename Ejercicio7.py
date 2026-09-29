import datetime as dt
class Comic:
    def __init__(self, titulo: str, id_comic: int, fecha_publicacion: dt.date, precio: float, stock: int):
        self._titulo = titulo
        self._id_comic = int(id_comic)
        self._fecha_publicacion = fecha_publicacion
        self._precio = precio
        self._stock = stock
    
    def modificar_dato(self, nuev_titulo = None, nuev_precio = None, nuev_stock = None):
        #Cambiamos los datos del comci que no esten vacios
        if nuev_titulo is not None:
            self._titulo = titulo
        if nuev_precio is not None:
            self._precio = precio
        if nuev_stock is not None:
            self._stock = stock

    def dias_desde_ref(self, fecha_ref: dt.date):
        #Primero chequeamos si el comic es mas antiguo que la fecha de referencia
        if self._fecha_publicacion < fecha_ref:
            print("El comic es mas antiguo que la fecha de referencia")
            self._stock = 0
        dias_dif = (self._fecha_publicacion - fecha_ref).days
        return dias_dif

    def __str__(self):
        contenido = f"Comic: {self._titulo} | ID: {self._id_comic} | Precio: ${self._precio} | Stock: {self._stock}"
        return contenido
    
    def __eq__(self, seg_com):
        if self._titulo == seg_com._titulo and self._id_comic == seg_com._id_comic:
            return True
        else:
            return False


