import tkinter as tk
from director import Director
from point import Point

class MazeGUI:
    def __init__(self, master, laberinto_file):
        self.master = master
        self.laberinto_file = laberinto_file
        self.juego = None
        self.canvas = None
        self.ancho = 0
        self.alto = 0

        self.load_laberinto()
        self.init_ui()

    def load_laberinto(self):
        director = Director()
        director.procesar(self.laberinto_file)
        self.juego = director.obtenerJuego()
        self.juego.agregar_personaje("Pepe")

    def init_ui(self):
        self.master.title("Maze Game")
        self.canvas = tk.Canvas(self.master, width=1050, height=600, bg="white")
        self.canvas.pack()

        self.calcularLaberinto()
        for habitacion in self.juego.laberinto.hijos:
            print("num-punto",habitacion.num,habitacion.forma.punto.x,habitacion.forma.punto.y)
       #self.draw_maze()
        #self.draw_person()
        #self.draw_bichos()

    def calcularLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularTamContenedor()
        self.asignarPuntosReales()

    def draw_maze(self):
        for habitacion in self.laberinto.hijos:
            x = habitacion.forma.point[0] * 50  # Example: calculate x based on room position
            y = habitacion.forma.point[1] * 50  # Example: calculate y based on room position
            self.canvas.create_rectangle(x, y, x + 40, y + 40, fill="lightgray")

    def draw_person(self):
        # Implementation to draw the person on the canvas
        pass

    def draw_bichos(self):
        # Implementation to draw the bichos on the canvas
        pass

    def calcularPosicion(self):
        habitacion1 = self.juego.obtenerHabitacion(1)
        habitacion1.forma.punto = Point(0, 0)
        for habitacion in self.juego.laberinto.hijos:
            habitacion.calcularPosicion()
    
    def normalizar(self):
        min_x = 0
        min_y = 0

        # Buscar min_x y min_y
        for each in self.juego.laberinto.hijos:
            min_x = min(min_x, each.forma.punto.x)
            min_y = min(min_y, each.forma.punto.y)

        # Ajustar puntos
        for each in self.juego.laberinto.hijos:
            un_punto = each.forma.punto
            nuevo_x = un_punto.x + abs(min_x)
            nuevo_y = un_punto.y + abs(min_y)
            each.forma.punto = Point(nuevo_x, nuevo_y)  
    def calcularTamContenedor(self):
        max_x = 0
        max_y = 0

        for each in self.juego.laberinto.hijos:
            max_x = max(max_x, each.forma.punto.x)
            max_y = max(max_y, each.forma.punto.y)

        max_x += 1
        max_y += 1

        self.ancho = round(1050 / max_x)
        self.alto = round(600 / max_y)

    def asignarPuntosReales(self):
        origen_x, origen_y = 70, 10

        for each in self.juego.laberinto.hijos:
            x = origen_x + (each.forma.punto.x * self.ancho)
            y = origen_y + (each.forma.punto.y * self.alto)
            
            each.forma.punto = Point(x, y)  # Asumo que Punto(x, y) es una clase
            each.forma.extent = (self.ancho, self.alto)

            # Si quisieras incluir la recursión comentada:
            # for hijo in each.hijos:
            #     hijo.asignar_puntos_reales(each)

if __name__ == '__main__':
    root = tk.Tk()
    gui = MazeGUI(root, "./laberintos/lab4HabIzd4Bichos.json")  # Use a default laberinto file
    root.mainloop()
