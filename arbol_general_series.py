from series import *

class Nodo:
    def __init__(self, dato):
        self.dato = dato   #serie o temp
        self.siguiente = None #referencia serie o siguiente temp
        self.hijos = None # referencia a primera temp 

class ArbolGeneral: #Series
    def __init__(self, raiz = None):
        self.raiz = raiz  
    
    def arbol_vacio(self):
        if self.raiz is None:
            return True
    
    def agregar_hijo_raiz(self, info):
        if self.arbol_vacio():
            self.raiz = Nodo(info)
            print (f"se agrego {info.nombre} correctamente.")
        else:
            return self.agregar_nodo_serie(self.raiz, info) # raiz y valor que le pasamos.
        return self.raiz
    def agregar_nodo_serie(self, nodo, info):
        if nodo is None:
            return
        if nodo.dato == None:
            return
        nueva_serie = Nodo(info)
        if nodo.siguiente is None:
            nodo.siguiente = nueva_serie
            print ("Se agrego hermana")
            return
        # si el nodo dado tiene hermanos.
        else:
            return self.agregar_nodo_serie(nodo.siguiente, nueva_serie)
        
    def agregar_nodo_temporada(self, serie, info):  # Hermanos temporadas
        nodo_de_serie = self.buscar_serie(serie.nombre)
        temporada = Nodo(info)
        if nodo_de_serie is None:
            print(f"La serie {serie.nombre} no se encuentra en el catalogo..")
            return
        if nodo_de_serie.hijos is None:  # Si no tiene temporadas aún
            nodo_de_serie.hijos = temporada
            print(f"Se agregó la temporada {temporada.dato.nombre} a la serie {nodo_de_serie.dato.nombre}.")
        else:  # Si ya hay temporadas, busca el último nodo
            actual = nodo_de_serie.hijos
            while actual.siguiente is not None:  # Recorrer hasta el final
                actual = actual.siguiente
            actual.siguiente = temporada
            print(f"Se agregó la temporada {temporada.dato.nombre} como hermana en la serie {nodo_de_serie.dato.nombre}.")     
        
    def agregar_hijo_nodo_padre(self, nodo_padre_serie, info):
        if not self.arbol_vacio():
            nodo_padre_serie = self._buscar_nodo(self.raiz, nodo_padre_serie)
            if nodo_padre_serie:
                print ("se agrega temporada")
                self.agregar_nodo(nodo_padre_serie, info)
        else:
            print(f"El árbol está vacío, no se pudo agregar {info} a {nodo_padre_serie}.")
    
    def _buscar_nodo(self, nodo:Serie, serie): # (raiz , nodo padre)
        if nodo is None:
            return None
        if nodo.nombre == serie: # 1er -> compara si la raiz es el padre pasado. 2do compara el dato del nodo hijo pasado
            return nodo
        return self._buscar_nodo(nodo.siguiente_serie, serie)
    

    def buscar_serie(self, nombre_serie):
        nodo = self.raiz # primer serie
        if self.arbol_vacio():
            print("No hay series en el catalogo")
            return None
        elif nodo.dato.nombre == nombre_serie:
               #print(f"Nombre de la serie {nombre_serie}")
                return nodo
        else:
            return self.buscar_serie_recursiva(nodo.siguiente, nombre_serie)  
            
    def buscar_serie_recursiva(self, nodo, nombre_serie):
        if nodo is None:
            print("Serie no encontrada")
            return
        if nodo.dato is None:
            print("Serie no encontrada")
            return None
        if nodo.dato.nombre == nombre_serie:
            print("Serie encontrada")
            return nodo
        else:
            return self.buscar_serie_recursiva(nodo.siguiente, nombre_serie)
        
    def mostrar_temporadas(self, nodo_serie):
        if nodo_serie.hijos is None:
            print("La serie no tiene temporadas")
            return []  # Devolver una lista vacía si no hay temporadas
        temporadas = []
        nodo_temp = nodo_serie.hijos  # Primer hijo (primera temporada)
        while nodo_temp is not None:  # Recorrer todas las temporadas
            temporadas.append({
                "nombre": nodo_temp.dato.nombre,
                "capitulos": nodo_temp.dato.capitulos
            })
            nodo_temp = nodo_temp.siguiente  # Avanzar al siguiente nodo
        return temporadas

    def mostrar_todo(self):
        if self.raiz is None:
            print("No hay series en el catálogo.")
            return
        nodo_serie = self.raiz
        while nodo_serie is not None:  # Recorrer las series
            print(f"- {nodo_serie.dato.nombre} (Género: {nodo_serie.dato.genero}, Popularidad: {nodo_serie.dato.popularidad}.)")
            nodo_temporada = nodo_serie.hijos  # Primera temporada
            while nodo_temporada is not None:  # Recorrer las temporadas
                print(f"  Temporada: {nodo_temporada.dato.nombre}")
                for capitulo in nodo_temporada.dato.capitulos:
                    print(f"    - {capitulo}")
                nodo_temporada = nodo_temporada.siguiente  # Siguiente temporada
            nodo_serie = nodo_serie.siguiente  # Siguiente serie