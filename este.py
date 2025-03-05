from orientacion import Orientacion

class Este(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, contenedor):
        contenedor.este = elemento

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

    def __str__(self):
        return "Soy la orientacion este"
