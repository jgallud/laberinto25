class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):        
        self.nombre = nombre
