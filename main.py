from visualizacion import generar_y_visualizar
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import ventana

def main():
    ventana.ventana_principal() #Se invoca la pantalla principal


def guardar_datos(datos, intervalos):
    generar_y_visualizar(datos, intervalos) # Genera y visualiza el histograma de los datos
    data = {
        'Números Generados': datos,

    }
    df = pd.DataFrame(data)
    df.to_excel('resultados.xlsx', index=False, sheet_name='Resultados') # Guarda el DataFrame como un archivo Excel sin índice en la hoja 'Resultados'
    wb = load_workbook('resultados.xlsx') # Carga el archivo Excel y añade el histograma como imagen en la hoja activa
    ws = wb.active
    img = Image('histograma.png')
    ws.add_image(img, 'A1')
    wb.save('resultados_con_histograma.xlsx')  # Guarda el archivo Excel con el histograma añadido
    # realizar_pruebas(datos,intervalos,dist)

if __name__ == "__main__":
    main()
