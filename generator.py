import os.path
import random
import pickle
import turtle

def generadorUniforme(a, b, n, name):
    mode = 'w'  # Modo de escritura de texto para crear el archivo
    with open(name, mode) as f:
        for _ in range(n):
            random_value = round(random.uniform(a, b), 4)  # Genera un número aleatorio entre a y b
            f.write(str(random_value) + ';')  # Convertir el número en cadena y escribirlo

def generadorExponencial(l, n, name):
    mode = 'w'
    with open(name, mode) as f:
        for _ in range(n):
            random_value = round(random.expovariate(1/l), 4)  # Genera un número aleatorio exponencial
            f.write(str(random_value) + ';')

def generadorNormal(m, d, n, name):
    mode = 'w'
    with open(name, mode) as f:
        for _ in range(n):
            random_value = round(random.normalvariate(m, d), 4)  # Genera un número aleatorio normal
            f.write(str(random_value) + ';')


def visualizarSerie(name):
    if os.path.exists(name):
        with open(name, 'r') as f:
            serie = f.readline().strip().split(';')[:-1]
            serie = [float(x) for x in serie]

            turtle.speed('fastest')  # Establecer la velocidad del dibujo al máximo

            # Ajustar el tamaño de la ventana de la tortuga
            turtle.setup(width=800, height=600)

            # Dibujar el eje x
            turtle.penup()
            turtle.goto(-350, 0)
            turtle.pendown()
            turtle.forward(700)

            # Dibujar el eje y
            turtle.penup()
            turtle.goto(0, -250)
            turtle.left(90)
            turtle.pendown()
            turtle.forward(500)

            # Etiquetas de los ejes
            turtle.penup()
            turtle.goto(-370, -10)
            turtle.pendown()
            turtle.write('Índice', align='left')

            turtle.penup()
            turtle.goto(-20, -270)
            turtle.pendown()
            turtle.write('Valor', align='left')

            # Dibujar la serie como una línea
            max_value = max(serie)
            min_value = min(serie)
            range_value = max_value - min_value
            num_points = len(serie)

            turtle.penup()
            turtle.goto(-350, -250)
            turtle.pendown()

            for i in range(num_points):
                x = -350 + (i / (num_points - 1)) * 700
                y = -250 + ((serie[i] - min_value) / range_value) * 500
                turtle.goto(x, y)

            turtle.hideturtle()
            turtle.done()

    else:
        print("El archivo no existe.")
