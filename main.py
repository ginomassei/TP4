import os
import options
import functions as f


def main():
    f.print_blue_text('TP4 Sistema de Gestión de una Competencia Mundial.')
    print('-' * 80)

    countries = []  # Arreglo que va a contener eventualmente los objetos de tipo país.
    fixture = []  # Arreglo que va a contener el fixture del mundial.

    option = -1
    while option != 0:
        f.print_blue_text('Menú de opciones: ')
        print('\n1 - Cargar el archivo.')
        print('2 - Mostrar el listado completo de países.')
        print('3 - Mostrar país con mayor cantidad de campeonatos ganados.')
        print('4 - Mostrar los países que ganaron algún campeonato.')
        print('5 - Generar nuevo vector con paises de alguna confederación en específico.')
        print('6 - Buscar archivo de clasificación de una confederación.')
        print('7 - Generar el fixture del próximo mundial.')
        print('8 - Consultar a qué grupo pertenece un equipo.')

        print('\n0 - Salir.')

        option = int(input('\nIngrese su opción: '))
        print()

        if option == 0:
            options.option0()
            return 0

        if option == 1:
            countries = options.option1()

        elif option == 2:
            options.option2(countries)

        elif option == 3:
            options.option3(countries)

        elif option == 4:
            options.option4(countries)

        elif option == 5:
            options.option5(countries)

        elif option == 6:
            options.option6(countries)

        elif option == 7:
            fixture = options.option7(countries)

        elif option == 8:
            options.option8(fixture, countries)

        else:
            f.print_red_text('Opción no válida')

        print('-' * 80)

        input(f.red_string('Presione la tecla enter para volver al menú de opciones > '))
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia el contenido de la terminal.


if __name__ == "__main__":
    main()
