import matplotlib.pyplot as plt
import numpy as np

def frecuenciasObservadas(numeros, intervalos):
    limites = np.linspace(min(numeros), max(numeros), intervalos + 1)
     
    frecuencias, _ = np.histogram(numeros, bins=limites)
    
    return frecuencias


def generar_y_visualizar(datos,intervalos):
    plt.hist(datos, bins=intervalos, density=True, alpha=0.6, color='g',edgecolor='black', rwidth=0.85)
    plt.title('Histograma de la distribución')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.savefig('histograma.png')
    plt.show()
