from modo import Modo
from agresivo import Agresivo
from ente import Ente

class Bicho(Ente):
    def __init__(self):
        self.modo = None
        self.running = True
        self.poder = None
        self.vidas = None
        self.posicion = None

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return "Soy un bicho"+self.modo.__str__()
