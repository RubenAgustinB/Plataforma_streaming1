class Usuario:
    
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena
        self.edad = None
        self.historial_visualizacion = []
        self.preferencias = []
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        return self.nombre