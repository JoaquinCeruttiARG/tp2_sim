from visualizacion import generar_y_visualizar
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import ventana

def main():
    ventana.ventana_principal()


def guardar_datos(datos, intervalos):
    generar_y_visualizar(datos, intervalos)
    data = {
        'Números Generados': datos,

    }
    df = pd.DataFrame(data)
    df.to_excel('resultados.xlsx', index=False, sheet_name='Resultados')
    wb = load_workbook('resultados.xlsx')
    ws = wb.active
    img = Image('histograma.png')
    ws.add_image(img, 'A1')
    wb.save('resultados_con_histograma.xlsx')
    # realizar_pruebas(datos,intervalos,dist)

if __name__ == "__main__":
    main()
