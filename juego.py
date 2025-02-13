class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self):
        print(f"Entrando en la habitación {self.num}")

class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def entrar(self):
        print("Entrando en el laberinto")

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def obtenerHabitacion(self, num):
        for habitacion in self.habitaciones:
            if habitacion.num == num:
                return habitacion
        return None

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("Entrando en una pared")

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("Entrando en una pared bomba")

class Puerta:
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self):
        print("Entrando en una puerta")

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

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)
