import pandas as pd
import os

def generar_excel(lista_numeros, nombre_archivo, media, n, maximo, minimo, rango, intervalos, amplitud, fe, fo, li, ls,
                  pm, lista_chi2, chi, poac, peac, maxdiff, po, pe, listadiffs, des):

    # Crear un DataFrame con los números en una columna
    df_numeros = pd.DataFrame({"Números": lista_numeros})

    # Crear un DataFrame con los valores adicionales
    df_valores = pd.DataFrame({
        "Descripción": ["Media", "N (Tamaño)", "Máximo", "Mínimo", "Rango", "Intervalos", "Amplitud", "Desviacion"],
        "Valores": [media, n, maximo, minimo, rango, intervalos, amplitud, des]
    })

    # Añadir una columna en blanco en la columna C
    df_valores.insert(0, " ", "")

    # Concatenar los dos DataFrames
    df = pd.concat([df_numeros, df_valores], ignore_index=True, axis=1)

    # Generar intervalos automáticamente
    intervalos_auto = list(range(1, intervalos + 1))

    # Guardar el DataFrame en un archivo de Excel
    with pd.ExcelWriter(nombre_archivo, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Datos")

        # Escribir la tabla adicional en el mismo archivo Excel
        df_tabla = pd.DataFrame({
            "Intervalos": intervalos_auto + ["-"],
            "Li": li + ["-"],
            "Ls": ls + ["-"],
            "Pm": pm + ["-"],
            "Fe": fe + [sum(fe)],
            "Fo": fo + [sum(fo)],
            "Chi2": lista_chi2 + [chi]  # Agregamos el valor de chi a la lista_chi2
        })

        # Calcular la posición donde se debe escribir la tabla adicional
        pos_inicio_tabla = 0  # Iniciamos en la primera fila
        pos_fin_tabla = pos_inicio_tabla + len(df_tabla) + 1

        # Insertar la tabla adicional en la posición calculada
        df_tabla.to_excel(writer, startrow=pos_inicio_tabla, startcol=10, index=False, sheet_name="Datos",
                          header=["Intervalos", "Li", "Ls", "Pm", "Fe", "Fo", "Chi2"])

        # Agregar la segunda tabla adicional
        df_segunda_tabla = pd.DataFrame({
            "Intervalos": intervalos_auto + ["-"],  # Utilizamos los mismos intervalos
            "Li": li + ["-"],  # Utilizamos los mismos límites inferiores
            "Ls": ls + ["-"],  # Utilizamos los mismos límites superiores
            "Fe": fe + [sum(fe)],
            "Fo": fo + [sum(fo)],
            "Pobs": po + [sum(po)],  # Lista de pobs
            "Pesp": pe + [sum(pe)],  # Lista de pesp
            "Poac": poac + ["-"],  # Lista de poac
            "Peac": peac + ["KS: "],  # Lista de peac
            "Diff": listadiffs + [maxdiff]  # Lista de diffs
        })

        # Insertar la segunda tabla adicional después de la primera
        df_segunda_tabla.to_excel(writer, startrow=pos_fin_tabla, startcol=10, index=False, sheet_name="Datos",
                                  header=["Intervalos", "Li", "Ls", "Fe", "Fo", "Pobs", "Pesp", "Poac", "Peac", "Diff"])

    # Abrir el archivo de Excel
    os.system("start EXCEL.EXE {}".format(nombre_archivo))






