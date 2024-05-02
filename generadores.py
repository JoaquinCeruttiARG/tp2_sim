import numpy as np
import random
import math

def generar_uniforme(a, b, N):
    """
    Genera una serie de números aleatorios uniformemente distribuidos en el intervalo [a, b].

    Args:
    - a (float): Extremo inferior del intervalo.
    - b (float): Extremo superior del intervalo.
    - N (int): Número de números aleatorios a generar.

    Returns:
    - numpy.ndarray: Array de números aleatorios uniformemente distribuidos.
    """
    uniformes = np.random.uniform(a, b, N)
    return np.round(uniformes, 4)

def generar_exponencial(lambda_, N):
    """
    Genera una serie de números aleatorios con distribución exponencial.

    Args:
    - lambda_ (float): Parámetro lambda de la distribución exponencial.
    - N (int): Número de números aleatorios a generar.

    Returns:
    - list: Lista de números aleatorios con distribución exponencial.
    """
    numeros_generados = [round(-np.log(1 - random.random()) / lambda_, 4) for _ in range(N)]
    return numeros_generados

def generar_normal(media, desviacion, N):
    """
    Genera una serie de números aleatorios con distribución normal.

    Args:
    - media (float): Media de la distribución normal.
    - desviacion (float): Desviación estándar de la distribución normal.
    - N (int): Número de números aleatorios a generar.

    Returns:
    - list: Lista de números aleatorios con distribución normal.
    """
    numeros_generados = []
    for _ in range(N):
        u1, u2 = random.random(), random.random()
        z0 = math.sqrt(-2.0 * math.log(1-u1)) * math.cos(2.0 * math.pi * u2)
        numeros_generados.append(round(media + desviacion * z0, 4))
    return numeros_generados
