import functions as f
import os
from options import *


def main():
    f.print_blue_text('TP4 Sistema de Gestión de una Competencia Mundial.')
    print('-' * 80)

    countries = []  # Arreglo que va a contener eventualmente los objetos de tipo país.

    option = -1
    while option != 0:
        f.print_blue_text('Menú de opciones: ')
        print('\n1 - Cargar el archivo.')
        print('2 - Mostrar el listado completo de países.')
        print('3 - Mostrár país con mayor cantidad de campeonatos ganados.')
        print('4 - Mostrar los países que ganaron algún campeonato.')
        print('5 - Generar nuevo vector con paises de alguna confederación en específico.')

        print('\n0 - Salir.')

        option = int(input('\nIngrese su opción: '))
        print()

        if option == 0:
            option0()
            return 0

        if option == 1:
            option1(countries)

        elif option == 2:
            option2(countries)

        elif option == 3:
            option3(countries)

        elif option == 4:
            option4()

        elif option == 5:
            option5(countries)

        print('-' * 80)

        input(f.red_string('Presione la tecla enter para volver al menú de opciones > '))
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia el contenido de la terminal.


if __name__ == "__main__":
    main()
