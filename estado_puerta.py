class EstadoPuerta:
    def __init__(self):
        pass

    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        pass

    def entrar(self, puerta, alguien):
        pass


class Abierta(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print("La puerta ya está abierta")

    def cerrar(self, puerta):
        print("Cerrando la puerta")
        puerta.estadoPuerta = Cerrada()

    def entrar(self, puerta, alguien):
        puerta.puedeEntrar(alguien)


class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print("Abriendo la puerta")
        puerta.estadoPuerta = Abierta()

    def cerrar(self, puerta):
        print("La puerta ya está cerrada")

    def entrar(self, puerta, alguien):
        pass
