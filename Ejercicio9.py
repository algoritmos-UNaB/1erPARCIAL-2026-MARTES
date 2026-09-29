class TiendaComics:
    def __init__(self):
        self._secciones: dict[str, [Comic]] = {}

    def agregar_seccion(self, nombre_sec: str):
        if nombre_sec in self._secciones:
            print(f" La sección "{nombre_sec}" ya existe.")
            return
        self._secciones[nombre_sec] = []
        print(f" Sección "{nombre_sec}" creada.")
    
    def agregar_comic(self, nombre_sec, comic: Comic):
        for com in self._secciones[nombre_sec]:
            if com._id_comic == comic._id_comic:
                print("El comic ya esta registrado")
                return
        self._secciones[nombre_sec].append(comic)
    
    def remover_comic(self, id_co):
        #Borra un comic buscandolo por su id
        for sec, lista_c in self._secciones.items():
            for com in lista_c:
                if com._id_comic == id_co:
                    self._secciones[sec].remove(com)
                    break
        print(f"El comic no existe en la tienda")
    
    def actualizar_stock(self, seccion, id_co, n_stock):
        #Actualizar un comic dando su seccion e id
        if seccion not in self._secciones:
            print(f"La seccion {seccion} no existe.")
            
        for com in self._secciones[seccion]:
             if com._id_comic == id_co:
                com._stock = n_stock
                return
        print("El comic no se encuentra en la seccion indicada")

    def stock_critico(self):
        removidos = 0
        for sec, lista_c in self._secciones.items():
            list_cop = lista_c
            for com in list_cop:
                if com._stock <= 3:
                    self._secciones[sec].remove(com)
                    removidos += 1
        return removidos
