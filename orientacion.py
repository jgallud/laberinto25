class Orientacion:
    def __init__(self):
        pass

    def poner(self, contenedor, elemento):
        pass

class Norte(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, contenedor, elemento):
        contenedor.norte = elemento

class Sur(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, contenedor, elemento):
        contenedor.sur = elemento

class Este(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, contenedor, elemento):
        contenedor.este = elemento

class Oeste(Orientacion):
    def __init__(self):
        super().__init__()

    def poner(self, contenedor, elemento):
        contenedor.oeste = elemento
