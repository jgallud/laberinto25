from laberinto import Laberinto
from juego import Juego
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste 

class LaberintoBuilder:
    """
    Abstract builder for creating labyrinths.
    """

    def __init__(self):
        self.laberinto = None
        self.juego=None

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def construir_habitacion(self, numero_habitacion):
        """
        Builds a room in the labyrinth.
        """
        pass

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
    def obtener_laberinto(self):
        """
        Returns the constructed labyrinth.
        """
        return self._laberinto
