import functions as f


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
        print(f'\nEl país con mayor cantidad de partidos ganados es: ')
        print(most_winning_country)

    else:
        f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')


def option4():
    pass


def option5(countries):
    confederation_code = f.validate_confederation()
    countries_per_confederation = f.get_countries_per_confederation(confederation_code, countries)

    f.delete_atribute('confederation', countries_per_confederation)

    for i in countries_per_confederation:
        print(i)

    path = f'clasificacion{confederation_code}.dat'
    f.create_binary_file(countries_per_confederation, path)

    f.print_green_text('\nArchivo generado correctamente.')

    print(f'\nNombre: {path}')
    print(f'Se cargaron {len(countries_per_confederation)} registros al archivo.')


def option6():
    confederation = input('Ingrese la confederación a buscar: ')
