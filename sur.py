from orientacion import Orientacion

class Sur(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.sur = elemento

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

    def __str__(self):
        return "Soy la orientacion sur"
