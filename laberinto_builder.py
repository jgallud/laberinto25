import copy
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste 
from habitacion import Habitacion
from pared import Pared 
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from cuadrado import Cuadrado
from juego import Juego
from tunel import Tunel

class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego=None

    def fabricarJuego(self):
        self.juego=Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = copy.deepcopy(self.juego.prototipo)

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarHabitacion(self, num):
        hab=Habitacion(num)	
        hab.forma=self.fabricarForma()
        hab.forma.num=num
        # hab.agregarOrientacion(self.fabricarNorte())
        # hab.agregarOrientacion(self.fabricarSur())
        # hab.agregarOrientacion(self.fabricarEste())
        # hab.agregarOrientacion(self.fabricarOeste())
        for each in hab.forma.orientaciones:
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
     
    def fabricarForma(self):
        forma=Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma

    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    def fabricarBichoAgresivo(self):
        bicho=Bicho()
        bicho.modo=Agresivo()
        bicho.iniAgresivo()
        return bicho
    def fabricarBichoPerezoso(self):
        bicho=Bicho()
        bicho.modo=Perezoso()
        bicho.iniPerezoso()
        return bicho

    def obtenerJuego(self):
        return self.juego
    
    def fabricarTunelEn(self,unCont):
        tunel=Tunel(None)
        unCont.agregar_hijo(tunel)
    
    def fabricarBicho(self,modo,posicion):
        if modo=='Agresivo':
            bicho=self.fabricarBichoAgresivo()
        if modo=='Perezoso':
            bicho=self.fabricarBichoPerezoso()
        hab=self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(bicho)
        self.juego.agregar_bicho(bicho)
