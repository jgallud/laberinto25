from juego import Habitacion, Laberinto, Pared, Puerta, ParedBomba, Bomba, Bicho, Agresivo, Perezoso
from orientacion import Norte, Sur, Este, Oeste

class Creator:
    def crear_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.orientaciones.append(self.crear_norte())
        habitacion.orientaciones.append(self.crear_sur())
        habitacion.orientaciones.append(self.crear_este())
        habitacion.orientaciones.append(self.crear_oeste())
        pared_norte = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return habitacion

    def crear_laberinto(self):
        return Laberinto()

    def crear_norte(self):
        return Norte()

    def crear_sur(self):
        return Sur()

    def crear_este(self):
        return Este()

    def crear_oeste(self):
        return Oeste()

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
