class Serie:

    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad
        

    def __str__(self):
        return self.nombre
    
    