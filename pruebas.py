from scipy.stats import chi2_contingency, ks_2samp
from scipy.stats import chisquare
import numpy as np


def realizar_prueba_chi_cuadrado(datos):
    muestra_teorica = datos
    chi2, p_valor_chi2, dof, expected = chi2_contingency([datos, muestra_teorica])
    print(f"Prueba de Chi cuadrado: Chi2 = {chi2}, p-valor = {p_valor_chi2}, grados de libertad = {dof}")


def calculate_observed_frequencies(data, num_intervals):
    # Sort the data
    sorted_data = sorted(data)
    
    # Calculate bin edges
    bin_edges = np.linspace(min(sorted_data), max(sorted_data), num_intervals + 1)
    
    # Initialize a list to store the observed frequencies for each bin
    observed_frequencies = [0] * num_intervals
    
    # Iterate through each data point
    for data_point in sorted_data:
        # Find the bin that the data point falls into
        for i, (lower, upper) in enumerate(zip(bin_edges[:-1], bin_edges[1:])):
            if lower <= data_point < upper:
                # Increment the count for this bin
                observed_frequencies[i] += 1
                break # Exit the loop once the bin is found
    
    return observed_frequencies


def prueba_chi_cuadrado(datos,intervalos, distribucion):
    if distribucion == 'uniforme':
       observed_frequencies=calculate_observed_frequencies(datos,intervalos)
       total_observations = sum(observed_frequencies)
    
       # Calculate the expected frequency for each category
       expected_frequency = total_observations / len(observed_frequencies)
       expected_frequencies = [expected_frequency] * len(observed_frequencies)
    
       # Perform the chi-square test
       chi_square_stat, p_value = chisquare(observed_frequencies, expected_frequencies)
    
       # Determine if the distribution is uniform
       # If p_value > 0.05, we do not reject the null hypothesis (i.e., the distribution is uniform)
       if p_value>0.05:
            print("Se acepta la hipotesis")
       else:
            print("Se rechaza la hipotesis")
       

    elif distribucion == 'exponencial':
        # Calcular el parámetro lambda
        lambda_param = 1 / np.mean(datos)
        # Calcular las frecuencias esperadas
        frecuencias_esperadas = lambda_param * np.exp(-lambda_param * datos)
        chi2, p_value = chisquare(datos, f_exp=lambda x: frecuencias_esperadas)
    elif distribucion == 'normal':
        # Calcular la media y la desviación estándar
        media = np.mean(datos)
        desviacion = np.std(datos)
        # Calcular las frecuencias esperadas
        frecuencias_esperadas = (1 / (np.sqrt(2 * np.pi * desviacion**2))) * np.exp(-(datos - media)**2 / (2 * desviacion**2))
        chi2, p_value = chisquare(datos, f_exp=lambda x: frecuencias_esperadas)
    else:
        raise ValueError("Distribución no soportada")
    
    return p_value


def realizar_prueba_ks(datos):
    muestra_teorica = np.random.normal(size=len(datos))
    D, p_valor_ks = ks_2samp(datos, muestra_teorica)
    print(f"Prueba de Kolmogorov-Smirnov: D = {D}, p-valor = {p_valor_ks}")


def realizar_pruebas(datos, intervalos, distribucion):
    realizar_prueba_chi_cuadrado(datos)
    prueba_chi_cuadrado(datos,intervalos, distribucion)
    realizar_prueba_ks(datos)
