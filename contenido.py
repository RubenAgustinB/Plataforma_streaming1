from arbol_binario import * 
from plataforma import *
from series import *
from temporadas import *
from arbol_general_series import *

class Catalogo:
    """
    Clase que gestiona el catálogo de películas y series de la plataforma.
    """
    def __init__(self):
        self.nombre = None
        
    def mostrar_contenido(self, arbol_peliculas:Arbol_binario, arbol_series:ArbolGeneral):
        """
        Muestra el catálogo completo (películas y series).
        """
        print("\n--- Catálogo de Contenido ---")
        print("\n--- Catálogo de Películas ---")
        arbol_peliculas.mostrar_peliculas() 
        print("\n--- Catálogo de Series ---")
        arbol_series.mostrar_todo()


    # def agregar_pelicula(self, nombre, genero, popularidad, duracion):
    #     """
    #     Agrega una película al árbol de películas.
    #     """
    #     self.peliculas.insertar_pelicula(nombre, genero, popularidad, duracion)
        
    # def agregar_serie(self, nombre, genero, popularidad, episodios):
    #     """
    #     Agrega una serie a la lista de series.
    #     """
    #     self.series.append({"nombre": nombre, "genero": genero, "popularidad": popularidad, "episodios": episodios})
    #     print(f"Serie '{nombre}' agregada con éxito al catálogo.")