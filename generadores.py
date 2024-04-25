import numpy as np
import random
import math

def generar_uniforme(a, b, N):
    uniformes = np.random.uniform(a, b, N)
    return np.round(uniformes,4)

def generar_exponencial(lambda_, N):
    numeros_generados = [round(-np.log(1 - random.random()) / lambda_, 4) for _ in range(N)]
    return numeros_generados

def generar_normal(media, desviacion, N):
    numeros_generados = []
    for _ in range(N):
        u1, u2 = random.random(), random.random()
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        numeros_generados.append(round(media + desviacion * z0, 4))
    return numeros_generados


