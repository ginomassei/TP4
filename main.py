import functions as f
import os


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
            f.print_blue_text('Programa finalizado...')
            print('-' * 80)
            return 0

        if option == 1:
            countries = f.load_text_file_on_memory('paises.csv')
            countries = f.get_countries(countries)

            f.print_green_text('Archivo cargado en memoria correctamente.')

        elif option == 2:
            if len(countries) != 0:
                f.print_blue_text('Listado completo de países: \n')
                for country in countries:
                    print(country)
            else:
                f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')

        elif option == 3:
            if len(countries) != 0:
                f.get_wins_per_country(countries)
            else:
                f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')
        
        elif option == 4:
            pass

        elif option == 5:
            confederation_code = f.validate_confederation()
            countries_per_confederation = f.get_countries_per_confederation(confederation_code, countries)
            for country in countries_per_confederation:
                    print(country)


        print('-' * 80)

        input(f.red_string('Presione la tecla enter para volver al menú de opciones > '))
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia el contenido de la terminal.


if __name__ == "__main__":
    main()
