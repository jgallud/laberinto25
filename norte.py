from orientacion import Orientacion

class Norte(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __str__(self):
        return "Soy la orientacion norte"
