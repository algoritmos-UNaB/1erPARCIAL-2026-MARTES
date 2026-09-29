#Nombre y apellido: Leandro Leonel Veliz
#Email: leandro.leonel.veliz@gmail.com
#Comisión: 3

import datetime 

class Comic:
    def __init__(self, titulo: str, id_comic: int, fecha_publicacion: datetime.date, precio: float, stock: int):
        # Atributos iniciales definidos en el Ejercicio 7
        self.titulo = titulo                   
        self.id_comic = id_comic               
        self.fecha_publicacion = fecha_publicacion 
        self.precio = precio                   
        self.stock = stock                    

    # EJERCICIO 7: El Inventario de Comics de Stuart
    
    def modificar_datos(self, titulo=None, precio=None, stock=None):
        """Permite cambiar uno o varios datos del cómic (título, precio, stock).""" 
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def calcular_dias_publicacion(self, fecha_referencia: datetime.date):
        """
        Calcula los días transcurridos respecto a una fecha de referencia.
        Si el cómic es más antiguo que dicha fecha, informa al usuario y agota el stock.
        """ 
        diferencia = fecha_referencia - self.fecha_publicacion
        
        # Comprueba si la fecha de publicación es anterior (más antigua) a la fecha de referencia
        if self.fecha_publicacion < fecha_referencia: 
            print(f"Aviso: El cómic '{self.titulo}' es más antiguo que la fecha de referencia.") 
            self.stock = 0 
            
        return abs(diferencia.days)

    # EJERCICIO 8: La Etiqueta de los Comics (Sobrecarga)
    
    def __str__(self):
        """Representa el cómic de forma legible usando el formato solicitado.""" 
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio} | Stock: {self.stock}" 

    def __eq__(self, otro_comic):
        """Compara si dos cómics son iguales basándose estrictamente en su id_comic y titulo.""" 
        if isinstance(otro_comic, Comic):
            return (self.id_comic == otro_comic.id_comic) and (self.titulo == otro_comic.titulo) 
        return False