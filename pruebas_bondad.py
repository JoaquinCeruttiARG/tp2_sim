import math
from scipy.stats import ksone, chi2
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

    chi2_critico = chi2.ppf(1 - 0.1, gl)

    return chi2_critico


def chi_cuadrado(Esperadas, Observadas):
    lista_chi2 = [0] * len(Observadas)
    for i, (obs, esp) in enumerate(zip(Observadas, Esperadas)):
        lista_chi2[i] = ((obs - esp) ** 2) / esp

    chi_cuadrado = sum(lista_chi2)

    return chi_cuadrado, lista_chi2


def ks_tabla(lista):
    tamano = len(lista)

    if tamano > 35:
        ks_tabla = 1.22 / math.sqrt(tamano)
    else:
        # Calcula la tabla de valores críticos utilizando ksone
        ks_tabla = ksone.ppf(1 - 0.1 / 2, tamano)  # 0.1 para un nivel de significancia de 0.1
    return ks_tabla


def c_fe_uniforme(intervalos, tamano):
    f_esperada = [0] * intervalos
    fe = tamano / intervalos
    for f in range(intervalos):
        f_esperada[f] = fe
    return f_esperada


# Calcula las frecuencias esperadas de una distribución normal
def c_fe_normal(lista_valores, intervalos, media, desviacion, li, ls, pm):
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
    return f_esperada


# Calcula las frecuencias esperadas de una distribución exponencial
def c_fe_exponencial(lam, intervalos, li, ls, tamano):

    f_esperada = [0] * intervalos

    for i in range(len(li)):
        f_esperada[i] = (1 - math.exp(-lam * ls[i])) - (1 - math.exp(-lam * li[i]))

        # Multiplica por el tamaño total de la muestra
        f_esperada[i] *= tamano
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
    return LI, LS, puntos_Medio


def c_valores(lista, intervalos):
    maximo = max(lista)
    minimo = min(lista)
    tamano = len(lista)
    rango = maximo - minimo
    amplitud = rango / intervalos
    media = np.mean(lista)
    desviacion = np.std(lista)

    return maximo, minimo, tamano, amplitud, rango, media, desviacion


def c_frec_observadas(lista, intervalos, li, ls):

    frecuencias_observadas = [0] * intervalos

    for n in lista:
        for i in range(intervalos):
            if li[i] <= n <= ls[i]:
                frecuencias_observadas[i] += 1

    return frecuencias_observadas


# Calcula chi2, KS y compara con las tablas, devuelve analisis de las pruebas
def prueba(lista, intervalo_seleccionado, distribucion_seleccionada, lam):
    # Realizar la prueba de chi-cuadrado
    global expected_freq

    # Generamos los respectivos valores
    li, ls, pm = c_limites(lista, intervalo_seleccionado)
    maximo, minimo, tamano, amplitud, rango, media, desviacion = c_valores(lista, intervalo_seleccionado)

    observed_freq = c_frec_observadas(lista, intervalo_seleccionado, li, ls)

    observed_freq2, intervalos2 = np.histogram(lista, bins=intervalo_seleccionado)
    print("Frecuencias observadas por libreria: ", observed_freq2)
    print("INTERVALOS DE LIBRERIA: ", intervalos2)
    print("TAMANO INTLIB: ", len(intervalos2))
    print("FOBS POR MI: ", observed_freq)

    if distribucion_seleccionada == "uniforme":
        expected_freq = c_fe_uniforme(intervalo_seleccionado, tamano)
    elif distribucion_seleccionada == "normal":
        expected_freq = c_fe_normal(lista, intervalo_seleccionado, media, desviacion, li, ls, pm)
    elif distribucion_seleccionada == "exponencial":
        expected_freq = c_fe_exponencial(lam, intervalo_seleccionado, li, ls, tamano)

    chi_calculado, lista_chi2 = chi_cuadrado(expected_freq, observed_freq)
    chi_tabla = chi2_tabla(intervalo_seleccionado, distribucion_seleccionada)


    # Prueba
    chi_calculado2, p_val, fe, tc = chi2_contingency([observed_freq, expected_freq])
    print("Chi2 calculado por libreria: ", chi_calculado2)
    print("Por mi: ", chi_calculado)

    ks_calculado, p = stats.ks_2samp(observed_freq, expected_freq)

    ks_tab = ks_tabla(lista)

    generador_excel.generar_excel(lista, "DistribucionAleatoria.xlsx", media, tamano, maximo, minimo, rango, intervalo_seleccionado, amplitud, expected_freq, observed_freq, li, ls, pm, lista_chi2, chi_calculado)

    print("Distribucion: ", distribucion_seleccionada)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)
    print("Tamaño:", tamano)
    print("Amplitud:", amplitud)
    print("Rango:", rango)
    print("Media:", media)
    print("Desviación Estándar:", desviacion)
    print("Límite Inferior:", li)
    print("Límite Superior:", ls)
    print("Punto Medio:", pm)
    print("FESP: ", expected_freq)
    print("FOBS: ", observed_freq)

    return chi_calculado, chi_tabla, ks_calculado, ks_tab




