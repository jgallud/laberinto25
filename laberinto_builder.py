class LaberintoBuilder:
    """
    Abstract builder for creating labyrinths.
    """

    def __init__(self):
        self._laberinto = None

    def construir_laberinto(self):
        """
        Builds the base labyrinth.
        """
        pass

    def construir_habitacion(self, numero_habitacion):
        """
        Builds a room in the labyrinth.
        """
        pass

    def construir_puerta(self, numero_habitacion1, numero_habitacion2):
        """
        Builds a door between two rooms.
        """
        pass

    def obtener_laberinto(self):
        """
        Returns the constructed labyrinth.
        """
        return self._laberinto
