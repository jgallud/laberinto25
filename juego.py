from creator import Creator

class ElementoMapa:
    def __init__(self):
        pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = Pared()
        self.sur = Pared()
        self.este = Pared()
        self.oeste = Pared()

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

class Puerta:
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()

    def iniciar_juego(self):
        # Lógica para iniciar el juego
        pass

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)
        habitacion1.sur = puerta
        habitacion2.norte = puerta
        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

#ejemplo de uso
creator = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabFM(creator)
print(juego.laberinto.habitaciones[0].num)
print(juego.laberinto.habitaciones[1].num)
