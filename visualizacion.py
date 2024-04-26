import matplotlib.pyplot as plt
import numpy as np

def frecuenciasObservadas(numeros, intervalos):
    limites = np.linspace(min(numeros), max(numeros), intervalos + 1)  # Genera límites igualmente espaciados para los intervalos

    frecuencias, _ = np.histogram(numeros, bins=limites)  # Genera límites igualmente espaciados para los intervalos

    return frecuencias


def generar_y_visualizar(datos,intervalos):
    plt.hist(datos, bins=intervalos, alpha=0.6, color='g',edgecolor='black', rwidth=0.85) # Genera y visualiza un histograma de los datos
    plt.title('Histograma de la distribución')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.savefig('histograma.png')  # Guarda el histograma como un archivo de imagen
    plt.show()  # Muestra el histograma en pantalla
