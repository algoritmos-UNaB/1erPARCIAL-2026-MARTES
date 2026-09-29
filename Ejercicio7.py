#(2pt.) Ejercicio 7: El Inventario de Comics de Stuart
#Definir una clase Comic que represente un cómic en venta en la tienda de Stuart.Contiene los datos:

#titulo: 'string'
#id_comic: 'integer'
#fecha_publicacion: date (importar datetime)
#precio: 'float'
#stock: 'integer'
#La clase debe contener métodos para facilitar:

#Cambiar uno o varios datos del cómic (título, precio, stock).
# def modificar_datos

#Calcular en cuántos días se publicó un cómic desde una fecha de referencia.
# def dias_publicacion  resta de fechas

#Si el método detecta que el cómic es más antiguo que la fecha de referencia, 
#deberá informar al usuario y marcar el stock como 0.
# condicion error, dentro de la funcion dias_publicacion


from datetime import date

class Comic:
    def __init__(self,titulo, id_comic,fecha_publicacion,precio,stock):
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
        if self.stock is not None:
            self.stock = stock

    def dias_publicacion(self, fecha_referencia):
        diferencia = fecha_referencia - self.fecha_publicacion

        if self.fecha_publicacion < fecha_referencia:
            print("el cómic es más antiguo que la fecha de referencia")
            self.stock = 0
        
        return diferencia.days