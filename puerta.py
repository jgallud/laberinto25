from elemento_mapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self,alguien):
        print("Entrando en una puerta")
        if self.abierta:
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
            else:
                self.lado1.entrar(alguien)
        else:
            print("La puerta está cerrada")

    def abrir(self):
        print("Abriendo puerta")
        self.abierta = True

    def cerrar(self):
        print("Cerrando puerta")
        self.abierta = False

    def esPuerta(self):
        return True

    def __str__(self):
        return "Soy una puerta"
