import generator

# Función Principal - Menú

def principal():
    op = 1

    while op != 9:
        print('\nMenú de opciones')
        print('1 - Generar Serie de Uniforme')
        print('2 - Generar serie Exponencial')
        print('3 - Generar serie Normal')
        print('4 - Visualizar Serie')
        print('5 - Generar Histograma de Frecuencias')
        print('6 - Prueba de Bondad Chi-2')
        print('7 - Prueba de Bondad K-S')
        print('8 - Salir')

        op = int(input('\nPorfavor, ingrese el valor deseado: '))

        if op == 1:
            a = int(input('Ingrese el LI de la serie: '))
            b = int(input('Ingrese el LS de la serie: '))
            n = int(input('Ingrese el tamaño de la serie: '))
            name = input('Ingrese el Nombre del archivo de la serie: ')

            if a < b and 0 < n <= 1000000:
                generator.generadorUniforme(a, b, n, name)
            else:
                print('Valores ingresados incorrectos.')

        elif op == 2:
            l = float(input('Ingrese el valor de lambda (Lambda): '))
            n = int(input('Ingrese el tamaño de la serie: '))
            name = input('Ingrese el Nombre del archivo de la serie: ')

            if l > 0 and 0 < n <= 1000000:
                generator.generadorExponencial(l, n, name)
            else:
                print('Valores ingresados incorrectos.')

        elif op == 3:
            m = float(input('Ingrese el valor de la media: '))
            d = float(input('Ingrese el valor de la desviación estándar: '))
            n = int(input('Ingrese el tamaño de la serie: '))
            name = input('Ingrese el Nombre del archivo de la serie: ')

            if d > 0 and 0 < n <= 1000000:
                generator.generadorNormal(m, d, n, name)
            else:
                print('Valores ingresados incorrectos.')

        elif op == 4:
            name = input('Ingrese el nombre del archivo de la serie: ')
            generator.visualizarSerie(name)

        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            print('\nAdiós!\n')
        else:
            print('\n Valor fuera de rango. \n')


if __name__ == '__main__':
    principal()
