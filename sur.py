from orientacion import Orientacion

class Sur(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, contenedor):
        contenedor.sur = elemento

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

    def __str__(self):
        return "Soy la orientacion sur"
