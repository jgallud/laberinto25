from juego import Habitacion, Laberinto, Pared, Puerta, ParedBomba, Bomba, Bicho, Agresivo, Perezoso

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

    def crear_bomba(self, em):
        return Bomba(em)

    def crear_bicho(self, vidas, poder, posicion, modo):
        return Bicho(vidas, poder, posicion, modo)

    def crear_modo_agresivo(self):
        return Agresivo()

    def crear_modo_perezoso(self):
        return Perezoso()

class CreatorB(Creator):
    def crear_pared(self):
        return ParedBomba()
