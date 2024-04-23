import generator
from generator import *

# Función Principal - Menú

def principal():
    op = 1

    while op != 6:
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

            if ( a < b and ( 0 < n < 1000000)):
                name = input('Ingrese el Nombre del archivo de la serie:')
                generator.generadorUniforme(a, b, n, name)
            elif a > b:
                print('El LS NO puede ser menor al LI!')
            elif 0 < n > 1000000:
                print('n debe estar entre [1;1000000]!')


        elif op == 2:
            pass;
        elif op == 3:
            pass;
        elif op == 4:
            pass;
        elif op == 5:
            pass;
        elif op == 6:
            pass;
        elif op == 7:
            pass;
        elif op == 8:
            print('\nAdiós!\n')
        else:
            print('\n Valor fuera de rango. \n')


if __name__ == '__main__':
    principal()
