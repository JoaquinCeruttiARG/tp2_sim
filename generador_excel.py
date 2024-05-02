import pandas as pd

def generar_excel(lista_numeros, nombre_archivo, media, n, maximo, minimo, rango, intervalos, amplitud):
    # Crear un DataFrame con los números en una columna
    df_numeros = pd.DataFrame({"Números": lista_numeros})

    # Crear un DataFrame con los valores adicionales
    df_valores = pd.DataFrame({
        "Descripción": ["Media", "N (Tamaño)", "Máximo", "Mínimo", "Rango", "Intervalos", "Amplitud"],
        "Valores": [media, n, maximo, minimo, rango, intervalos, amplitud]
    })

    # Añadir una columna en blanco en la columna C
    df_valores.insert(0, " ", "")

    # Concatenar los dos DataFrames
    df = pd.concat([df_numeros, df_valores], ignore_index=True, axis=1)

    # Guardar el DataFrame en un archivo de Excel
    with pd.ExcelWriter(nombre_archivo, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Datos")

    # Abrir el archivo de Excel
    import os
    os.system("start EXCEL.EXE {}".format(nombre_archivo))






