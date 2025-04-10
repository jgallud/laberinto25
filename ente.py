from estado_ente import Vivo, Muerto

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()

    def clonarLaberinto(self,tunel):
        pass

    def esAtacadoPor(self, atacante):
        print(f"Ataque: {self}  es atacado")
        self.vidas -= atacante.poder
        print(f"Vidas restantes: {self.vidas}")
        if self.vidas <= 0:
            print(f"El ente ha muerto")
            self.estadoEnte.morir(self)

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas
        self.juego = juego

    def clonarLaberinto(self,tunel):
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()

    def __str__(self):
        return self.nombre