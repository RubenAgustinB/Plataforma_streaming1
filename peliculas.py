class Pelicula:

    def __init__(self, nombre, genero, popularidad, duracion):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.popularidad = popularidad
        
        self.izquierdo = None
        self.derecho = None