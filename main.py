from creator import Creator
from juego import Juego
#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabFM(fm)
print(juego.laberinto.habitaciones[0].num)
print(juego.laberinto.habitaciones[1].num)
