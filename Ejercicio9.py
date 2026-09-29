#Nombre y apellido: Leandro Leonel Veliz
#Email: leandro.leonel.veliz@gmail.com
#Comisión: 3

class TiendaComics:
    def __init__(self):
        # La tienda está representada mediante varias listas de objetos del tipo Comic
        # Se agrupan en un diccionario para facilitar el acceso por nombre de sección
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    def agregar_comic(self, comic, seccion):
        # Añade un nuevo cómic a una sección específica
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
        else:
            # Si la sección no existe en el diccionario, la crea
            self.secciones[seccion] = [comic]

    def remover_comic(self, comic):
        # Remueve un cómic del inventario buscando en todas las secciones
        for nombre_seccion, lista_comics in self.secciones.items():
            if comic in lista_comics:
                lista_comics.remove(comic)
                return True # Retorna True si lo encontró y lo borró
        return False

    def actualizar_stock(self, comic, nuevo_stock):
        # Actualiza el stock utilizando el método de la clase Comic (Ejercicio 7)
        comic.modificar_datos(stock=nuevo_stock)
        
        # Alternativamente, si se accediera directo al atributo:
        # comic.stock = nuevo_stock

    def limpiar_stock_critico(self):
        # Calcula y remueve los cómics con stock crítico (menor o igual a 3)
        cantidad_removidos = 0
        
        for nombre_seccion, lista_comics in self.secciones.items():
            # Iteramos sobre una copia de la lista (lista_comics[:]) 
            # para evitar errores al eliminar elementos durante la iteración
            for comic in lista_comics[:]:
                if comic.stock <= 3:
                    lista_comics.remove(comic)
                    cantidad_removidos += 1
                    
        return cantidad_removidos