from datetime import date

from Ejercicio7 import Comic


class TiendaComics:
    def __init__(self, nombre="La Tienda de Stuart"):
      
        self.nombre = nombre
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }


    def agregar_comic(self, seccion: str, comic: Comic):
  
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
            print(f"Cómic '{comic.titulo}' agregado a la sección '{seccion}'.")
        else:
            print(f"Error: La sección '{seccion}' no existe en la tienda.")

    def remover_comic(self, seccion: str, id_comic: int) -> bool:
       
        if seccion in self.secciones:
            lista_seccion = self.secciones[seccion]
            for comic in lista_seccion:
                if comic.id_comic == id_comic:
                    lista_seccion.remove(comic)
                    print(f"Cómic '{comic.titulo}' (ID: {id_comic}) removido de la sección '{seccion}'.")
                    return True
            print(f"No se encontró ningún cómic con ID {id_comic} en la sección '{seccion}'.")
        else:
            print(f"Error: La sección '{seccion}' no existe.")
        return False

    def actualizar_stock(self, seccion: str, id_comic: int, nuevo_stock: int) -> bool:
      
        if seccion in self.secciones:
            for comic in self.secciones[seccion]:
                if comic.id_comic == id_comic:
                    comic.modificar_datos(stock=nuevo_stock)
                    print(f"Stock actualizado a {nuevo_stock} para '{comic.titulo}'.")
                    return True
            print(f"No se encontró el cómic con ID {id_comic} en '{seccion}'.")
        else:
            print(f"Error: La sección '{seccion}' no existe.")
        return False


    def depurar_stock_critico(self, limite_critico: int = 3) -> int:
        
        total_removidos = 0
        print(f"\n--- Depurando cómics con stock crítico (<= {limite_critico}) ---")

        for seccion, lista_comics in self.secciones.items():
            comics_mantenidos = []
            for comic in lista_comics:
                if comic.stock <= limite_critico:
                    print(f"Retirando '{comic.titulo}' (ID: {comic.id_comic}) de '{seccion}' - Stock: {comic.stock}")
                    total_removidos += 1
                else:
                    comics_mantenidos.append(comic)
            
            self.secciones[seccion] = comics_mantenidos

        print(f"Total de cómics retirados por stock crítico: {total_removidos}")
        return total_removidos

    def mostrar_inventario(self):
        
        print(f"\n==========================================")
        print(f"      INVENTARIO: {self.nombre}")
        print(f"==========================================")
        for seccion, lista_comics in self.secciones.items():
            print(f"\n--- Sección: {seccion} ({len(lista_comics)} títulos) ---")
            if not lista_comics:
                print("  (Sección vacía)")
            else:
                for comic in lista_comics:
                    print(f"  • {comic}")



if __name__ == "__main__":
    tienda = TiendaComics()

    c1 = Comic("The Flash #1", 101, date(2020, 1, 15), 5.99, 25)
    c2 = Comic("Batman: Year One", 102, date(1987, 2, 1), 12.50, 2)
    c3 = Comic("Spider-Man #300", 201, date(1988, 5, 1), 15.00, 10)
    c4 = Comic("X-Men #1", 202, date(1991, 10, 1), 8.00, 1)
    c5 = Comic("Saga Vol. 1", 301, date(2012, 10, 10), 14.99, 0)

    tienda.agregar_comic("DC Comics", c1)
    tienda.agregar_comic("DC Comics", c2)
    tienda.agregar_comic("Marvel", c3)
    tienda.agregar_comic("Marvel", c4)
    tienda.agregar_comic("Independientes", c5)

    tienda.mostrar_inventario()

    print("\n--- Actualizando Stock ---")
    tienda.actualizar_stock("DC Comics", 101, 20)

    tienda.depurar_stock_critico(limite_critico=3)

    tienda.mostrar_inventario()
