from hoja import Hoja

class Tunel(Hoja):
    def __init__(self, laberinto):
        super().__init__()
        self.laberinto = None

    def puedeClonarLaberinto(self,alguien):
        self.laberinto = alguien.juego.clonarLaberinto()
        self.laberinto.entrar(self)

    def entrar(self, alguien):
        if self.laberinto is None:
            alguien.clonarLaberinto(self)            
        else:
            self.laberinto.entrar(alguien)
