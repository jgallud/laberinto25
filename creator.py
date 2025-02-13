from juego import Habitacion, Laberinto, Pared, Puerta

class Creator:
    def crear_habitacion(self, num):
        hab=Habitacion(num)
        hab.norte = Pared()
        hab.sur = Pared()
        hab.este = Pared()
        hab.oeste = Pared()
        return hab

    def crear_laberinto(self):
        return Laberinto()

    def crear_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)


