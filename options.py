import functions as f
import os.path


def option0():
    f.print_blue_text('Programa finalizado...')
    print('-' * 80)


def option1():
    countries = f.load_text_file_on_memory('paises.csv')
    countries = f.get_countries(countries)

    f.print_green_text('Archivo cargado en memoria correctamente.')

    return countries


def option2(countries):
    if len(countries) != 0:
        f.print_blue_text('Listado completo de países: \n')
        for country in countries:
            print(country)

    else:
        f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')


def option3(countries):
    if len(countries) != 0:
        most_winning_country = f.get_most_winning_country(countries)

        f.print_green_text('País encontrado!')
        print(f'\nEl país con mayor cantidad de campeonatos ganados es: ')
        print(most_winning_country)

    else:
        f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')


def option4(countries):

    if len(countries) != 0:

        wcpc = f.get_winning_countries_per_confederation(countries)

        f.print_green_text(f'Países de la UEFA que han ganado algún campeonato: {wcpc[0]}')
        f.print_green_text(f'Países de la CONMEBOL que han ganado algún campeonato: {wcpc[1]}')
        f.print_green_text(f'Países de la CONCACAF que han ganado algún campeonato: {wcpc[2]}')
        f.print_green_text(f'Países de la CAF que han ganado algún campeonato: {wcpc[3]}')
        f.print_green_text(f'Países de la AFC que han ganado algún campeonato: {wcpc[4]}')
        f.print_green_text(f'Países de la OFC que han ganado algún campeonato: {wcpc[5]}')

    else:
        f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')


def option5(countries):

    if len(countries) != 0:

        confederation_code, confederation_name = f.validate_confederation()
        countries_per_confederation = f.get_countries_in_confederation(confederation_code, countries)

        f.delete_atribute('confederation', countries_per_confederation)

        f.print_blue_text(f'\nListado de paises de la confederación {confederation_name}\n')
        for i in countries_per_confederation:
            print(i)

        path = f'clasificacion{confederation_code}.dat'
        f.create_binary_file(countries_per_confederation, path)

        f.print_green_text('\nArchivo generado correctamente.')

        print(f'\nNombre: {path}')
        print(f'Se cargaron {len(countries_per_confederation)} registros al archivo.')

    else:
        f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')


def option6(countries):

    if len(countries) != 0:

        confederation_code, confederation_name = f.validate_confederation()
        path = f'clasificacion{confederation_code}.dat'

        if not os.path.exists(path):

            countries_per_confederation = f.get_countries_in_confederation(confederation_code, countries)

            f.delete_atribute('confederation', countries_per_confederation)

            f.create_binary_file(countries_per_confederation, path)

            f.print_blue_text(f'\nEl archivo de la confederación {confederation_name} no había sido generado.')

            f.print_green_text('\nArchivo generado correctamente.')

            print(f'\nNombre: {path}')
            print(f'Se cargaron {len(countries_per_confederation)} registros al archivo.')

        else:

            file_countries = f.get_countries_from_file(path)

            f.print_green_text('Archivo encontrado\n')
            f.print_blue_text(f'Clasificación de la confederación {confederation_name}:\n')

            for i in file_countries:
                print(i)

    else:
        f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')
