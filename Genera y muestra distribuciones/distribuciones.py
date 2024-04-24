import math
import random
import matplotlib.pyplot as plt
import numpy as np


def generarArchivo(nombreArchivo, n):
    archivo = open(nombreArchivo, "w")
    for i in range(int(n)):
        a = random.random()
        linea = str(a) + "\n"
        archivo.write(linea)
    archivo.close()


def uniforme(aleatorios, a, b):
    archivo = open(aleatorios, "r")
    lineas = archivo.readlines()
    archivoExponencial = open("DistUniforme.txt", "w+")
    a = float(a)
    b = float(b)
    for rnd in lineas:
        rnd = float(rnd)
        x = a+rnd*(b-a)
        linea = str(x) + "\n"
        archivoExponencial.write(linea)
    archivoExponencial.close()


def boxMoller(aleatorios, sigma, media):
    archivo = open(aleatorios, "r")
    lineas = archivo.readlines()
    archivoNormal = open("DistNormal.txt", "w+")
    sigma = float(sigma)
    media = float(media)
    for i in range(0, len(lineas)-1, 2):
        rnd1 = float(lineas[i])
        rnd2 = float(lineas[i+1])

        n1 = (math.sqrt(-2*math.log(rnd1)) *
              math.cos(2*math.pi*rnd2))*sigma+media
        n2 = (math.sqrt(-2*math.log(rnd1)) *
              math.sin(2*math.pi*rnd2))*sigma+media

        linea = str(n1) + "\n"
        archivoNormal.write(linea)

        linea = str(n2) + "\n"
        archivoNormal.write(linea)

    archivoNormal.close()


def dist_Exponencial(aleatorios, lambda1):
    archivo = open(aleatorios, "r")
    lineas = archivo.readlines()
    archivoExponencial = open("DistExponencial.txt", "w+")
    lambda1 = float(lambda1)
    for rnd in lineas:
        rnd = float(rnd)
        x = (-1/lambda1)*math.log(1-rnd)
        linea = str(x) + "\n"
        archivoExponencial.write(linea)
    archivoExponencial.close()


def graficar(archivo, cant_intervalos):
    datos = np.loadtxt(archivo)
    print(datos)
    hist, tam_intervalos = np.histogram(datos, int(cant_intervalos))

    plt.figure(archivo)
    plt.hist(datos, tam_intervalos)
    plt.ylabel('frequencia')
    plt.xlabel('valores')
    plt.title('Histograma')
    plt.show()


# """Genera un archivo txt con numeros aleatorios de 0 a 1.
#  Recibe como parametros el nombre del archivo y la cantidad de numero a generar."""
# generarArchivo("aleatorios.txt",100000)

# """Genera un archivo txt con numeros aleatorios con distribucion normal.
#  Recibe como parametros el nombre del archivo, sigma y la media."""
# boxMoller("aleatorios.txt", 10, 50)
# """Genera un archivo txt con numeros aleatorios con distribucion exponencial.
#  Recibe como parametros el nombre del archivo y lambda."""
# dist_Exponencial("aleatorios.txt", 0.02)

# """Grafica el histograma de frecuencia de la distribucion normal.
#  Recibe como parametro el nombre del archivo y la cantidad de intervalos."""
# graficar("DistNormal.txt", 10)
# graficar("DistExponencial.txt", 10)
