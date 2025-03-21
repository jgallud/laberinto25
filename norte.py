from orientacion import Orientacion

class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __str__(self):
        return "Soy la orientacion norte"
