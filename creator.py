from juego import Habitacion, Laberinto, Pared, Puerta, ParedBomba, Bomba, Bicho, Agresivo, Perezoso
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from orientacion import Orientacion
from cuadrado import Cuadrado
class Creator:
    def crear_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.forma = self.crear_forma()
        pared_norte = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return habitacion

    def crear_forma(self):
        forma=Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    
    def crear_laberinto(self):
        return Laberinto()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def crear_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def crear_bomba(self, em):
        return Bomba(em)

    def crear_bicho(self,vidas,poder,posicion,modo):
        bicho=Bicho();
        bicho.vidas=vidas
        bicho.poder=poder
        bicho.posicion=posicion
        bicho.modo=modo
        return bicho

    def crear_modo_agresivo(self):
        return Agresivo()

    def crear_modo_perezoso(self):
        return Perezoso()

class CreatorB(Creator):
    def crear_pared(self):
        return ParedBomba()
