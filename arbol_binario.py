from usuario import Usuario 
from peliculas import Pelicula
#codigo actualizado 20:00 2/12
class Nodo:
      def __init__(self, dato) -> None:
            self.dato = dato
            self.derecho = None
            self.izquierdo = None

class Arbol_binario:
      def __init__(self):
            self.raiz = None
            
      def agregar_nodocontenido(self, elemento):
            if not isinstance(elemento, Usuario) and not isinstance(elemento, Pelicula):
                  print ("error:")
                  return
            
            if self.raiz is None:
                  self.raiz = elemento
                  return
            else:
                  self._agregar_nodo(self.raiz, elemento)

      def _agregar_nodo(self, nodo_actual, nuevo_nodo):

            if nuevo_nodo.nombre < nodo_actual.nombre:
                  if nodo_actual.izquierdo is None:
                        nodo_actual.izquierdo = nuevo_nodo
                        return 
                  else:
                        self._agregar_nodo(nodo_actual.izquierdo, nuevo_nodo)
            else:
                  if nodo_actual.derecho is None:
                        nodo_actual.derecho = nuevo_nodo
                        return 
                  else:
                        self._agregar_nodo(nodo_actual.derecho, nuevo_nodo)
            
      def buscar_usuario(self, nombre, contrasena):
            nodo = self._buscar_recu(self.raiz, nombre)

            if nodo is not None and isinstance(nodo, Usuario) and nodo.contrasena == contrasena:
                  return True
            else:
                  return False
            
      def buscar_pelis(self, nombre):
            nodo = self._buscar_recu(self.raiz, nombre)
            if nodo is not None and isinstance(nodo, Pelicula):
                  return nodo
            else:
                  return False

      def _buscar_recu(self, nodo, nombre):
            if nodo is None:
                  return 
      
            if nodo.nombre == nombre:
                  return nodo

            if nombre < nodo.nombre:
                  print("_buscar_recu izquierdo")
                  return self._buscar_recu(nodo.izquierdo, nombre)
            elif nombre > nodo.nombre:
                  print("_buscar_recu derecho")
                  return self._buscar_recu(nodo.derecho, nombre)
            else:
                  return None
                        
      
      def peliculas_mas_populares(self, umbral_popularidad=250):
            peliculas_populares = []
            self._peliculas_mas_populares_recur(self.raiz, peliculas_populares, umbral_popularidad)
            print(peliculas_populares)

      def _peliculas_mas_populares_recur(self, nodo, peliculas_populares, umbral_popularidad):
            if nodo:
                  self._peliculas_mas_populares_recur(nodo.izquierdo, peliculas_populares, umbral_popularidad)
            if isinstance(nodo, Pelicula) and nodo.popularidad > umbral_popularidad:
                  peliculas_populares.append(nodo.nombre)  
            self._peliculas_mas_populares_recur(nodo.derecho, peliculas_populares, umbral_popularidad)

      def mostrar_peliculas(self):
            def _inorden(nodo):
                  if nodo is not None:
                        _inorden(nodo.izquierdo)
                        print(f"- {nodo.nombre} (Género: {nodo.genero}, "
                              f"Popularidad: {nodo.popularidad}, "
                              f"Duración: {nodo.duracion} minutos)")
                        _inorden(nodo.derecho)

            if self.raiz is None:
                  print("No hay películas en el catálogo.")
            else:
                  
                  _inorden(self.raiz)