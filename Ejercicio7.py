from datetime import date


class Comic:
    def __init__(self, titulo: str, id_comic: int, fecha_publicacion: date, precio: float, stock: int):
    
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    def modificar_datos(self, titulo: str = None, precio: float = None, stock: int = None):
    
        if titulo is not None:
            self.titulo = titulo
            print(f"Título actualizado a: '{self.titulo}'")
        
        if precio is not None:
            self.precio = float(precio)
            print(f"Precio actualizado a: ${self.precio:.2f}")
            
        if stock is not None:
            self.stock = int(stock)
            print(f"Stock actualizado a: {self.stock}")

    def calcular_dias_desde_referencia(self, fecha_referencia: date) -> int:
  
        diferencia_dias = (fecha_referencia - self.fecha_publicacion).days

        if diferencia_dias > 0:
            print(f"\n[Aviso] El cómic '{self.titulo}' es más antiguo que la fecha de referencia ({fecha_referencia}).")
            self.stock = 0
            print("El stock ha sido actualizado a 0.")
        
        return diferencia_dias


    def __str__(self) -> str:
 
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, otro_comic) -> bool:
   
        if isinstance(otro_comic, Comic):
            return self.id_comic == otro_comic.id_comic and self.titulo == otro_comic.titulo
        return False


if __name__ == "__main__":
    comic1 = Comic("The Flash #1", 456, date(2020, 1, 15), 5.99, 25)
    comic2 = Comic("The Flash #1", 456, date(2021, 5, 10), 10.00, 50) 
    comic3 = Comic("Batman #1", 789, date(2019, 3, 20), 12.50, 10)

    # 1. Prueba de __str__
    print("--- Prueba de __str__ ---")
    print(comic1)
    print(comic3)

    # 2. Prueba de __eq__
    print("\n--- Prueba de __eq__ ---")
    print(f"¿comic1 es igual a comic2?: {comic1 == comic2}") 
    print(f"¿comic1 es igual a comic3?: {comic1 == comic3}")  
