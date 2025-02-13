from juego import Habitacion, Laberinto, Pared, Puerta

class Creator:
    def crear_habitacion(self, num):
        return Habitacion(num)

    def crear_laberinto(self):
        return Laberinto()

    def crear_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)


