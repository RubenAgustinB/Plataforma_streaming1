from arbol_binario import Arbol_binario
from contenido import Catalogo
from usuario import *
from peliculas import *
from series import *
from temporadas import *
from arbol_general_series import *
from cola_prioridades import ColaPrioridades

#----------------------------------------------#
class Plataforma:
    def __init__(self, nombre):
        self.nombre = nombre
        self.arbol_usuarios = Arbol_binario()
        self.arbol_peliculas = Arbol_binario()
        self.arbol_series = ArbolGeneral()
        self.catalogo = Catalogo()        
        self.watchlist = ColaPrioridades()
        
    def inicio_sesion(self):
        while True:
            print("\n1.Iniciar Sesión \n2.Crear Usuario \n3.Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                usuario = input("Usuario: ")
                contrasena = input("Contraseña: ")
                if self.arbol_usuarios.buscar_usuario(usuario, contrasena):
                    self.menu_principal()
                else:
                    print("Usuario o contraseña incorrectos.")
            
            elif opcion == "2":
                self.crear_usuario()

            elif opcion == "3":
                print("¡Gracias por usar la plataforma!")
                break
           
            else:
                print("Opción no válida.")
    
    def crear_usuario(self):
        nombre = input("Nombre: ")
        contrasena = input("Contraseña: ")
        # Se crea una instancia de la clase Usuario con los datos ingresados. 

        usuario = Usuario(nombre, contrasena)
        self.arbol_usuarios.agregar_nodocontenido(usuario)
        print(f"Usuario {nombre} creado con éxito.")

    def agregar_pelicula(self):
        print("\n--- Agregar Película ---")
        nombre = input("Nombre de la película: ").strip()
        genero = input("Género: ").strip()
        popularidad = int(input("Popularidad (número de visualizaciones): ").strip())
        duracion = int(input("Duración (en minutos): ").strip())
        print("Por favor, ingrese valores numéricos para popularidad y duración.")
        pelicula = Pelicula(nombre, genero, popularidad, duracion)
        self.arbol_peliculas.agregar_nodocontenido(pelicula)    
        return
    
    def buscar_pelicula(self):
        print("\n--- Buscar Película ---")
        nombre = input("\nNombre de la película: ").strip()
        pelicula = self.arbol_peliculas.buscar_pelis(nombre)  
        if pelicula:
            print(f"Pelicula encontrada: {pelicula.nombre}, Género: {pelicula.genero},
                  Popularidad: {pelicula.popularidad}, Duración: {pelicula.duracion} minutos.")
        else:
            print(f"\nNo se encontró la película.")
    
    def agregar_serie(self):

        print("\n--- Agregar Serie ---")
        nombre = input("Nombre de la serie: ")
        genero = input("Genero de la serie: ")
        popularidad = input("Popularidad de la serie: ")
        
        serie = Serie(nombre, genero, popularidad)

        self.arbol_series.agregar_hijo_raiz(serie)

        self.carga_temps(serie)
    
    def carga_temps(self, serie):
        print("\n--- Agregar Temporadas ---")

        while True:
            nombre_temporada = input("Nombre de la Temporada ('x' para terminar): ")
            if nombre_temporada.lower() == "x":
                break

            temporada = Temporada(nombre_temporada)

            while True:
                nombre_capitulo = input("Ingrese nombre del capítulo ('x' para terminar): ")
                if nombre_capitulo.lower() == "x":
                    break
                temporada.cargar_capitulos(nombre_capitulo)

            # Agregar la temporada al árbol
            self.arbol_series.agregar_nodo_temporada(serie, temporada)

        print("\n--- Carga terminada ---") 
    
    def buscar_serie(self):
        print("\n--- Buscar Serie ---")
        nombre = input("Nombre de la Serie: ")
        serie = self.arbol_series.buscar_serie(nombre)
        if serie == None:
            
            return
        else:
            print(f"Serie encontrada: {serie.dato.nombre}")
            temps = self.arbol_series.mostrar_temporadas(serie)
            if not temps:
                print("No hay temporadas disponibles.")
            else:
                for temp in temps:
                    print(f"Temporada: {temp['nombre']}")
                    print("Capítulos:")
                    for capitulo in temp['capitulos']:
                        print(f"  - {capitulo}")
        return (serie.dato.nombre)          

    def menu_admin(self):
        while True:
            print("\n--- Menú Admin ---")
            print("1. Ver contenido")
            print("2. Agregar película") 
            print("3. Buscar Pelicula")
            print("4. Agregar Serie")
            print("5. Buscar Serie")
            print("6. Mas populares")
            print("7. Mostrar peliculas")
            print("8. Salir a Menu Usuario")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.catalogo.mostrar_contenido(self.arbol_peliculas, self.arbol_series)
            elif opcion == "2":  
                self.agregar_pelicula()
            elif opcion == "3":
                self.buscar_pelicula()
            elif opcion == "4":  
                self.agregar_serie()
            elif opcion == "5": 
                self.buscar_serie()
            
            elif opcion == "6":
                pass

            elif opcion == "7":

                self.arbol_peliculas.mostrar_peliculas()
            elif opcion == "8":
                break
            else:
                print("Opción no válida.")
    
    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Ver contenido")
            print("2. Buscar Pelicula")
            print("3. Buscar Serie")
            print("4. Mas populares")
            print("5. Mostrar peliculas")
            print("6. Agregar a Watchlist")
            print("7. Mostrar Watchlist")
            print("8. Salir")
            print("*. TOKEN Admin")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.catalogo.mostrar_contenido(self.arbol_peliculas, self.arbol_series)
            elif opcion == "2":
                self.buscar_pelicula()
            elif opcion == "3": 
                nombre_serie = self.buscar_serie()
                if nombre_serie is not None:
                    self.arbol_series.buscar_serie(nombre_serie) 
            elif opcion == "4":
                self.peliculas.mas_popular()
            elif opcion == "5":
                self.arbol_peliculas.mostrar_peliculas()            
            elif opcion == "6":
                self.agregar_a_watchlist()
            elif opcion == "7":
                self.mostrar_watchlist()
            elif opcion == "999":
                self.menu_admin()
            elif opcion == "8":
                break
            else:
                print("Opción no válida.")
    
    
    
    
    # def agregar_a_watchlist(self):
        
    #     #Permite al usuario agregar contenido a la watchlist.
        
    #     print("\n--- Agregar a Watchlist ---")
    #     nombre = input("Nombre del contenido: ").strip()
    #     try:
    #         prioridad = int(input("Prioridad (mayor número, mayor prioridad): ").strip())
    #     except ValueError:
    #         print("Por favor, ingrese un número válido para la prioridad.")
    #         return

    #     if self.arbol_peliculas.buscar_pelis(nombre):
    #         self.watchlist.agregar_contenido(nombre, prioridad)
    #         print(f"'{nombre}' fue agregado a la watchlist con prioridad {prioridad}.")
    #     else:
    #         print(f"El contenido '{nombre}' no está disponible en el catálogo.")
    # def mostrar_watchlist(self):
        
        #Muestra los contenidos en la watchlist.
        
        print("\n--- Watchlist ---")
        self.watchlist.mostrar_contenido()






