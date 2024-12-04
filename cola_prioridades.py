class ColaPrioridades:
    def __init__(self):
        # Usamos una lista para almacenar los elementos (tuplas de prioridad y contenido)
        self.cola = []

    def agregar_contenido(self, contenido, prioridad):
        """
        Agrega un contenido a la cola con una prioridad específica.
        """
        # Insertamos el contenido como tupla (prioridad, contenido)
        # El contenido con mayor prioridad tendrá el valor de prioridad más alto
        elemento = (prioridad, contenido)

        # Insertar el elemento de manera ordenada en la lista
        # Insertamos el nuevo elemento en su lugar correspondiente para mantener el orden
        inserted = False
        for i in range(len(self.cola)):
            if self.cola[i][0] < prioridad:
                self.cola.insert(i, elemento)
                inserted = True
                break
        if not inserted:
            self.cola.append(elemento)

        print(f"'{contenido}' fue agregado a la cola con prioridad {prioridad}.")

    def obtener_siguiente(self):
        """
        Obtiene y elimina el contenido con mayor prioridad.
        """
        if self.esta_vacia():
            print("La cola de prioridades está vacía.")
            return None
        # Extraemos y eliminamos el primer elemento (el de mayor prioridad)
        prioridad, contenido = self.cola.pop(0)
        print(f"'{contenido}' con prioridad {prioridad} fue eliminado de la cola.")
        return contenido

    def mostrar_contenido(self):
        """
        Muestra todo el contenido en la cola, sin modificarla.
        """
        if self.esta_vacia():
            print("\nNo hay contenido en la cola de prioridades.")
        else:
            print("\n--- Contenido en la Cola de Prioridades ---")
            for prioridad, contenido in self.cola:
                print(f"- {contenido} (Prioridad: {prioridad})")

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        """
        return len(self.cola) == 0