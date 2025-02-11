class ElementoMapa:
    def __init__(self):
        pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

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

# Ejemplo de uso
juego = Juego()
laberinto = juego.laberinto

# Crear habitaciones
habitacion1 = Habitacion(1)
habitacion2 = Habitacion(2)

# Conectar habitaciones
puerta = Puerta(habitacion1, habitacion2)
habitacion1.este = puerta
habitacion2.oeste = puerta

# Agregar habitaciones al laberinto
laberinto.agregar_habitacion(habitacion1)
laberinto.agregar_habitacion(habitacion2)

# Iniciar el juego
juego.iniciar_juego()
