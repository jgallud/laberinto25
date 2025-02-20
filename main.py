from creator import Creator, CreatorB
from juego import Juego
#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabFM(fm)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
print(hab1.num)
print(hab2.num)

#laberinto con paredes bomba
fmb = CreatorB()
juego.laberinto = juego.crearLaberinto2HabFM(fmb)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)

# Crear laberinto de 4 habitaciones
fm = Creator()
juego.laberinto = juego.crearLaberinto4Hab(fm)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho
        print(f"  Bicho: Vidas={bicho.vidas}, Poder={bicho.poder}, Posicion={bicho.posicion.num}")
