from Ejercicio7 import Comic
from Ejercicio10 import ListaEnlazada

class TiendaComics:
    def __init__(self):
        self.secciones = {
            "DC Comics": ListaEnlazada(),
            "Marvel": ListaEnlazada(),
            "Independientes": ListaEnlazada()
        }

    def agregar_comic(self, seccion: str, comic: Comic):
        # Agregar comic
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
        else:
            print(f"Error: La seccion {seccion} no existe.")
    
    def remover_comic(self, comic_a_remover: Comic):
        #Remover comic
        localizado = False
        for lista in self.secciones.values():
            if lista.remove(comic_a_remover):
                    localizado = True
                    print(f"Se eliminó el cómic: {comic_a_remover.titulo}")
                    break
            if not localizado:
                print("El cómic no se encuentra en el inventario.")

    def actualizar_stock(self, id_comic: int, nuevo_stock: int):
        # Buscar comic y modificar su stock
        for seccion, comic in self.secciones.items():
            for comic in comics:
                if comic.id_comic == id_comic:
                    comic.stock = nuevo_stock
                    print(f"Stock de {comic.titulo} actualizado a {nuevo_stock}.")
        else:
            print("No se encontro ningun comic con ese ID.")

    def retirar_stock_critico(self):
        # Si el stock calculado es menor o igual a 3, se remueven del inventario
        total_removidos = 0
        
        for lista in self.secciones.values():
            # 1. Identificamos los cómics críticos recorriendo la ListaEnlazada
            criticos = [c for c in lista if c.stock <= 3]
            
            # 2. Los eliminamos de la propia ListaEnlazada
            for comic in criticos:
                lista.remove(comic)
                total_removidos += 1
        
        print(f"Stuart retiro {total_removidos} comic/s por falta de demanda.")
        return total_removidos
    
