import os.path
import random
import pickle

def generadorUniforme(a, b, n, name):
    mode = 'w'  # Modo de escritura de texto para crear el archivo
    with open(name, mode) as f:
        for _ in range(n):
            random_value = round(random.uniform(a, b), 4)  # Genera un número aleatorio entre a y b
            f.write(str(random_value) + ';')  # Convertir el número en cadena y escribirlo

def generadorExponencial(l, n, name):
    pass;

def generadorNormal(m, d, n, name):
    pass;
