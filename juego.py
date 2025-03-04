class ElementoMapa:
    def __init__(self):
        self.padre = None
    
    def recorrer(self, func):
        func(self)

    def entrar(self):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        self.hijos.remove(hijo)

class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em

class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.activa = False

    def esBomba(self):
        return True

class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.modo = modo

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.poder = 1
        self.vidas = 5

class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self):
        print(f"Entrando en la habitación {self.num}")

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()        

    def entrar(self):
        print("Entrando en el laberinto")

    def agregar_habitacion(self, habitacion):
        self.hijos.append(habitacion)

    def obtenerHabitacion(self, num):
        for habitacion in self.hijos:
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

class Puerta(ElementoMapa):
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

class Orientacion:
    def __init__(self):
        pass

class Norte(Orientacion):
    def __init__(self):
        super().__init__()

class Sur(Orientacion):
    def __init__(self):
        super().__init__()

class Este(Orientacion):
    def __init__(self):
        super().__init__()

class Oeste(Orientacion):
    def __init__(self):
        super().__init__()

class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

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
    
    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.crear_laberinto()
        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        puerta = creator.crear_puerta(habitacion1, habitacion2)

        habitacion1.sur = puerta
        habitacion2.norte = puerta

        pared1 = creator.crear_pared()
        bomba1 = creator.crear_bomba(pared1)
        habitacion1.este = bomba1

        pared2 = creator.crear_pared()
        bomba2 = creator.crear_bomba(pared2)
        habitacion2.oeste = bomba2

        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        return laberinto

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)

    def crearLaberinto4Hab(self, creator):
        laberinto = creator.crear_laberinto()

        habitacion1 = creator.crear_habitacion(1)
        habitacion2 = creator.crear_habitacion(2)
        habitacion3 = creator.crear_habitacion(3)
        habitacion4 = creator.crear_habitacion(4)

        puerta12 = creator.crear_puerta(habitacion1, habitacion2)
        puerta13 = creator.crear_puerta(habitacion1, habitacion3)
        puerta24 = creator.crear_puerta(habitacion2, habitacion4)
        puerta34 = creator.crear_puerta(habitacion3, habitacion4)

        habitacion1.sur = puerta12
        habitacion1.este = puerta13
        habitacion3.oeste = puerta13
        habitacion3.sur = puerta34
        habitacion2.norte = puerta12
        habitacion2.este = puerta24
        habitacion4.norte = puerta34
        habitacion4.oeste = puerta24

        bicho1 = creator.crear_bicho(5, 10, habitacion1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, habitacion3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, habitacion2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, habitacion4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        habitacion1.bicho = bicho1
        habitacion2.bicho = bicho2
        habitacion3.bicho = bicho3
        habitacion4.bicho = bicho4

        laberinto.agregar_habitacion(habitacion1)
        laberinto.agregar_habitacion(habitacion2)
        laberinto.agregar_habitacion(habitacion3)
        laberinto.agregar_habitacion(habitacion4)

        return laberinto
