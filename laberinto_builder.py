from laberinto import Laberinto
from juego import Juego
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste 
from habitacion import Habitacion
from pared import Pared 

class LaberintoBuilder:
    """
    Abstract builder for creating labyrinths.
    """

    def __init__(self):
        self.laberinto = None
        self.juego=None

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarHabitacion(self, num):
        hab=Habitacion(num)	
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        for each in hab.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(),each)
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1,o1,lado2,o2):
        hab1=self.laberinto.obtenerHabitacion(lado1)
        hab2=self.laberinto.obtenerHabitacion(lado2)
        puerta=Puerta(hab1,hab2)
        objOr1=self.obtenerObjeto(o1)
        objOr2=self.obtenerObjeto(o2)
        hab1.ponerElementoEnOrientacion(puerta,objOr1)
        hab2.ponerElementoEnOrientacion(puerta,objOr2)
    
    def obtenerObjeto(self,cadena):
        obj=None
        match cadena:
            case 'Norte':
                obj=self.fabricarNorte()
            case 'Sur':
                obj=self.fabricarSur()
            case 'Este':
                obj=self.fabricarEste()
            case 'Oeste':
                obj=self.fabricarOeste()
        return obj
     
    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    def obtenerJuego(self):
        juego=Juego()
        juego.laberinto=self.laberinto
        return self.juego
