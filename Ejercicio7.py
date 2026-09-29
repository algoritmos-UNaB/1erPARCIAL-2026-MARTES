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

###########################################################################
#(2pt.) Ejercicio 8: La Etiqueta de los Comics (Sobrecarga de Métodos)
#Sobrecargar los siguientes métodos en la clase Comic:

#__str__: Para representar el cómic de forma legible (ej: "Comic: The Flash #1 | ID: 456 
# | Precio: $5.99 | Stock: 25").
#  es una cadena tipo registro
#__eq__: Para comparar si dos cómics son iguales basándose en su id_comic y titulo.


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

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | precio ${self.precio} | stock: {self.stock}"
    
    def __eq__(self, alt_comic):
        return self.id_comic == alt_comic.id_comic and self.titulo == alt_comic.titulo