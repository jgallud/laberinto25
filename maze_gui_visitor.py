from visitor import Visitor

class MazeGUIVisitor(Visitor):
    def __init__(self, canvas):
        self.canvas = canvas

    def visitarLaberinto(self, laberinto):
        pass

    def visitarHabitacion(self, habitacion):
        x = habitacion.forma.point[0] if habitacion.forma.point else 0
        y = habitacion.forma.point[1] if habitacion.forma.point else 0
        self.canvas.create_rectangle(x, y, x + 40, y + 40, fill="lightgray")

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        pass

    def visitarBicho(self, bicho):
        pass

    def visitarOrientacion(self, orientacion):
        pass
