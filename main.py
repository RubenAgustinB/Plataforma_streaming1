# Archivo que inicia el programa y ejecuta el menu principal.12

from plataforma import Plataforma

def main():
    print("\n>> Bienvenidos a la Plataforma de Streaming <<\n")
    plataforma = Plataforma("Plataforma de Streaming")
    plataforma.inicio_sesion()
    
if __name__ == "__main__":
    main()

    