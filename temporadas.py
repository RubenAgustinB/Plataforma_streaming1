class Temporada:
    def __init__(self,nombre):
        self.nombre = nombre
        self.capitulos = []

    def cargar_capitulos(self, dato):
        self.capitulos.append(dato)
        
    def __str__(self):
        return self.nombre
    
    def lista_cap(self):
        return self.lista_cap

        