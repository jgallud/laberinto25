from orientacion import Orientacion

class Oeste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, contenedor):
        contenedor.oeste = elemento

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)

    def __str__(self):
        return "Soy la orientacion oeste"
