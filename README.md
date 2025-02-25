# Laberinto25
Proyecto de la asignatura Diseño de Software del curso 24-25
El proyecto consiste en diseñar e implementar la lógica de un juego basado en un laberinto
La idea del proyecto está tomada de los ejemplos que aparecen en el libro "Design Patterns: Elements of Reusable Object-Oriented Programming", utilizados para ilustrar los patrones de creación.

Este curso 24-25 utilizaremos los asistentes de AI disponibles. Cada alumno podrá usar el que desee.
En este proyecto se utiliza Cline en VSCode con Geimini

## Factory Method
El primer patrón implementado es el Factory Method. A continuación, se muestra el diagrama de clases.

![laberinto-fm](https://github.com/user-attachments/assets/76cfb4d0-9eb1-4b9e-a36e-1a8ff2089e9a)

## Decorator
Con este patrón podemos agregar responsabilidades nuevas (Bomba) a otros objetos (Pared, Puerta...).
![decorator](https://github.com/user-attachments/assets/5f8839ea-10f1-484e-ae90-15cc09f186e6)

## Strategy
El Strategy encapsula familias de algoritmos como objetos. En nuestra solución lo aplicamos para encapsular el modo (Agresivo, Perezoso) de los bichos.
![strategy](https://github.com/user-attachments/assets/8357957d-3dc6-462b-b8d7-56b5069c74bc)

## Composite
Este patrón se utiliza para representar estructuras recursivas todo-parte. Simplifica a los clientes porque pueden tratar de manera uniforme a compuestos y hojas.
![composite](https://github.com/user-attachments/assets/c901618f-64bc-410c-ba11-2d336447ea92)
