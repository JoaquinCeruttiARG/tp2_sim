from generadores import generar_uniforme, generar_exponencial, generar_normal
from visualizacion import generar_y_visualizar
from pruebas import realizar_pruebas
import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image


def solicitar_parametros():
    print("Seleccione la distribución:")
    print("1. Uniforme")
    print("2. Exponencial")
    print("3. Normal")
    opcion = int(input("Ingrese el número de la distribución: "))
    
    N = int(input("Ingrese el tamaño de la muestra (hasta 1.000.000): "))
    
    if opcion == 1:

        a = int(input('Ingrese el valor del limite inferior: '))
        b = int(input('Ingrese el valor del limite superior: '))
        if a > b:
            print('Error en los limites seleccionados!')
            return

        return "uniforme", a, b, N
    elif opcion == 2:
        lambda_ = float(input("Ingrese el valor de lambda: "))
        return "exponencial", lambda_, N
    elif opcion == 3:
        media = float(input("Ingrese la media: "))
        desviacion = float(input("Ingrese la desviación: "))
        return "normal", media, desviacion, N
    else:
        print("Opción no válida. Intente de nuevo.")
        return solicitar_parametros()
    pass

def main():
    distribucion, *args, N = solicitar_parametros()
    if distribucion == "uniforme":
        a, b = args
        datos = generar_uniforme(a, b, N)
        dist= "uniforme"
    elif distribucion == "exponencial":
        lambda_ = args[0]
        datos = generar_exponencial(lambda_, N)
        dist= "exponencial"
    elif distribucion == "normal":
        media, desviacion = args
        datos = generar_normal(media, desviacion, N)
        dist= "normal"
    

    print("Seleccione la cantidad de intervalos de frecuencias:")
    print("1. 10")
    print("2. 12")
    print("3. 16")
    print("4. 23")
    opcion_intervalos = int(input("Ingrese el número de la opción: "))
    if opcion_intervalos == 1:
        intervalos = 10
    elif opcion_intervalos == 2:
        intervalos = 12
    elif opcion_intervalos == 3:
        intervalos = 16
    elif opcion_intervalos == 4:
        intervalos = 23
    else:
        print("Opción no válida. Intente de nuevo.")
        return
    
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
    #realizar_pruebas(datos,intervalos,dist)


if __name__ == "__main__":
    main()
