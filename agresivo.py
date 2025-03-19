import time
from modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Agresivo: Durmiendo un poco...")
        time.sleep(1)

    def caminar(self, bicho):
        print("Agresivo: Caminando con determinación...")

    def atacar(self, bicho):
        print("Agresivo: ¡Atacando con furia!")

    def __str__(self):
        return "-agresivo"
