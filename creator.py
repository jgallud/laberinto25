from juego import Habitacion, Laberinto, Pared, Puerta, ParedBomba

class Creator:
    def crear_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.norte = self.crear_pared()
        habitacion.sur = self.crear_pared()
        habitacion.este = self.crear_pared()
        habitacion.oeste = self.crear_pared()
        return habitacion

    def crear_laberinto(self):
        return Laberinto()

    def crear_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

class CreatorB(Creator):
    def crear_pared(self):
        return ParedBomba()
