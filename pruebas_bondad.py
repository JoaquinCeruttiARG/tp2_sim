import math
from scipy.stats import ksone
import numpy as np
from scipy.stats import chi2_contingency, stats
import generador_excel


def chi2_tabla(intervalos, dist):
    gl = 0

    if dist == "uniforme":
        gl = intervalos - 1
    elif dist == "normal":
        gl = intervalos - 3
    elif dist == "exponencial":
        gl = intervalos - 2

    alpha_09 = [0.016, 0.211, 0.352, 0.711, 1.61, 2.204, 2.833, 3.49, 4.168,
                4.865, 5.578, 6.304, 7.041, 7.79, 8.547, 9.312, 10.085, 10.865, 11.651,
                12.443, 13.24, 14.041, 14.848, 15.659, 16.473, 17.292, 18.114, 18.939,
                19.768, 20.599, 24.797, 29.051, 33.35, 37.689, 42.06, 46.459, 50.883,
                55.329, 59.795, 64.278, 68.777, 73.291, 77.818, 82.358]

    return alpha_09[gl-1]


def ks_tabla(lista):
    tamano = len(lista)

    if tamano > 35:
        ks_tabla = 1.22 / math.sqrt(tamano)
    else:
        # Calcula la tabla de valores críticos utilizando ksone
        ks_tabla = ksone.ppf(1 - 0.1 / 2, tamano)  # 0.1 para un nivel de significancia de 0.1
    return ks_tabla


def c_fe_uniforme(lista_valores, intervalos):
    f_esperada = [0] * intervalos
    total = len(lista_valores)
    fe = total / intervalos
    for f in range(intervalos):
        f_esperada[f] = fe
    print("fe esperada uniforme: ", f_esperada)
    return f_esperada


# Calcula las frecuencias esperadas de una distribución normal
def c_fe_normal(lista_valores, intervalos):
    media = np.mean(lista_valores)
    print("Media de np: ", media)
    desviacion = np.std(lista_valores)
    print("Desviacion de np: ", desviacion)

    li, ls, pm = c_limites(lista_valores, intervalos)

    f_esperada = []
    for i in range(intervalos):
        limite_inferior = li[i]
        limite_superior = ls[i]
        punto_medio = pm[i]

        exponente = -0.5 * (((punto_medio - media) / desviacion) ** 2)
        parte1 = math.exp(exponente) / (desviacion * math.sqrt(math.pi * 2))
        resultado = parte1 * (limite_superior - limite_inferior)

        fe = resultado * len(lista_valores)
        f_esperada.append(fe)
    print("fe esperada normal: ", sum(f_esperada))
    return f_esperada


# Calcula las frecuencias esperadas de una distribución exponencial
def c_fe_exponencial(lista_valores, lam, intervalos):
    li, ls, pm = c_limites(lista_valores, intervalos)
    tamano = len(lista_valores)

    f_esperada = [0] * intervalos

    for i in range(len(li)):
        f_esperada[i] = (1 - math.exp(-lam * ls[i])) - (1 - math.exp(-lam * li[i]))

        # Multiplica por el tamaño total de la muestra
        f_esperada[i] *= tamano

    print("fe esperada exponencial: ", sum(f_esperada))
    return f_esperada


# Calcula los limites inferiores y superior, junto con el respectivo punto medio
def c_limites(lista_valores, intervalos):
    minimo = min(lista_valores)
    maximo = max(lista_valores)
    rango = maximo - minimo
    amplitud = rango / intervalos

    LI = [0] * intervalos
    LS = [0] * intervalos
    puntos_Medio = [0] * intervalos

    LI[0] = minimo
    LS[0] = LI[0] + amplitud

    for i in range(1, intervalos):  # Comenzamos desde 1 para evitar repeticiones
        LI[i] = LS[i - 1]  # El límite inferior del intervalo actual es el límite superior del intervalo anterior
        LS[i] = LI[i] + amplitud

    for i in range(intervalos):
        puntos_Medio[i] = (LS[i] + LI[i]) / 2  # Calculamos el punto medio de cada intervalo

    print("LI:", LI)
    print("LD: ", LS)
    print("PUNTO MEDIO: ", puntos_Medio)
    return LI, LS, puntos_Medio


# Calcula chi2 y compara con la tabla, devuelve analisis de las pruebas
def prueba(lista, intervalo_seleccionado, distribucion_seleccionada, lam):
    # Realizar la prueba de chi-cuadrado
    global expected_freq

    observed_freq, intervalos = np.histogram(lista, bins=intervalo_seleccionado)
    print(intervalos)

    if distribucion_seleccionada == "uniforme":
        expected_freq = c_fe_uniforme(lista, intervalo_seleccionado)
    elif distribucion_seleccionada == "normal":
        expected_freq = c_fe_normal(lista, intervalo_seleccionado)
    elif distribucion_seleccionada == "exponencial":
        expected_freq = c_fe_exponencial(lista, lam, intervalo_seleccionado)

    chi_calculado, p_val, fe, tc = chi2_contingency([observed_freq, expected_freq])
    chi_tabla = chi2_tabla(intervalo_seleccionado, distribucion_seleccionada)

    ks_calculado, p = stats.ks_2samp(observed_freq, expected_freq)
    ks_tab = ks_tabla(lista)

    print("frecuencia observada: ", observed_freq)
    print("frecuencia esperada: ", expected_freq)

    media = np.mean(lista)
    print("Media de np: ", media)
    desviacion = np.std(lista)
    print("Desviacion de np: ", desviacion)
    maximo = max(lista)
    minimo = min(lista)
    rango = maximo - minimo
    amplitud = rango / intervalos

    #li, ls, pm = c_limites(lista, intervalos)

    generador_excel.generar_excel(lista, "DistribucionAleatoria.xlsx", media, len(lista), maximo, minimo, rango, len(intervalos), amplitud )

    return chi_calculado, chi_tabla, ks_calculado, ks_tab


    #generar_excel(numeros, "datos.xlsx", media, n, maximo, minimo, rango, intervalos, amplitud)

