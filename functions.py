import os
import pickle
import country
import random
import fileManager


# Funciones ANSI para colorear las salidas por terminal.
def print_red_text(string):
    red_text = '\033[31;1m'
    reset_text = '\033[m'

    print(red_text + string + reset_text)


def print_green_text(string):
    green_text = '\033[32;1m'
    reset_text = '\033[m'

    print(green_text + string + reset_text)


def print_blue_text(string):
    blue_text = '\033[34;1m'
    reset_text = '\033[m'

    print(blue_text + string + reset_text)


def red_string(string):
    red_text = '\033[31;1m'
    reset_text = '\033[m'

    return red_text + string + reset_text


# Funciones para el desarollo del tp.
def get_most_winning_country(countries):
    max_wins = 0
    most_winning_country = None

    for country in countries:
        if country.wins > max_wins:
            most_winning_country = country
            max_wins = country.wins
        
    return most_winning_country


def get_winning_countries_per_confederation(countries):
    uefa = count_winning_countries(get_countries_in_confederation(0, countries))
    conmebol = count_winning_countries(get_countries_in_confederation(1, countries))
    concacaf = count_winning_countries(get_countries_in_confederation(2, countries))
    caf = count_winning_countries(get_countries_in_confederation(3, countries))
    afc = count_winning_countries(get_countries_in_confederation(4, countries))
    ofc = count_winning_countries(get_countries_in_confederation(5, countries))

    return [uefa, conmebol, concacaf, caf, afc, ofc]


def count_winning_countries(countries):
    c = 0
    for country in countries:
        if country.wins > 0:

            c += 1

    return c


def get_countries_names(countries):
    """
    Genera un arreglo con los nombres de los países involucrados.
    """
    countries_names = []

    for country in countries:
        if country.name not in countries:
            countries_names.append(country.name)
    return countries_names


def validate_confederation():
    """
    Valida que la confederación ingresada por teclado esté dentro de la posibilidades.
    Y retorna su codigo numérico correspondiente.
    """
    available_confederations = ('UEFA', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC', 'OFC')
    confederation = input('Ingrese la confederación de la cual desea obtener los datos (Nombre en mayusculas): ')

    while confederation not in available_confederations:
        print_red_text('\nLa confederación ingresada no coincide con las cargadas en nuestros registros.')
        confederation = input('Ingrese la confederación de la cual desea obtener los datos (Nombre en mayusculas): ')

    if confederation == 'UEFA':
        return 0, confederation
    elif confederation == 'CONMEBOL':
        return 1, confederation
    elif confederation == 'CONCACAF':
        return 2, confederation
    elif confederation == 'CAF':
        return 3, confederation
    elif confederation == 'AFC':
        return 4, confederation
    elif confederation == 'OFC':
        return 5, confederation


def get_countries_in_confederation(confederation_code, countries):
    countries_in_confederation = []
    for country in countries:
        if country.confederation == confederation_code:
            fileManager.add_in_order(countries_in_confederation, country)

    return countries_in_confederation


def create_binary_file(array, path):
    file = open(path, 'wb')

    for element in array:
        pickle.dump(element, file)

    file.close()


def delete_atribute(atribute, array):
    for element in array:
        delattr(element, atribute)


def get_countries_from_file(path):
    countries = []

    file = open(path, 'rb')
    size = os.path.getsize(path)

    while file.tell() < size:
        countries.append(pickle.load(file))

    file.close()

    return countries


def validate_and_return_country(text, countries):
    name = input(text)
    validado = False
    while not validado:

        for i in countries:

            if name == i:
                print_green_text('\nPaís validado.')
                return i

        print_red_text('\nEl país ingresado no existe.')
        name = input(text)


def new_fixture(countries):
    fixture = 4 * [None]

    # Generamos un arreglo solo con los nombres de los países para poder manipularlos mejor.
    nombres = get_countries_names(countries)

    for i in range(len(fixture)):
        fixture[i] = 8 * [None]

    print(fixture)

    org = validate_and_return_country('Ingrese el nombre del país organizador: ', nombres)
    fixture[0][0] = org
    nombres.remove(org)

    '''
    Obtenemos los cabeza de serie (el arreglo original se ordenó previamente por puntaje de mayor a menor) y los
    eliminamos para evitar repeticiones.
    El índice del país a retornar es siempre 0 ya que se van desplazando los elementos restantes.
    '''

    for i in range(7):
        fixture[0][i + 1] = nombres.pop(0)

    '''
    Obtenemos los países restantes de forma aleatoria entre los 28 mejores.
    Para ello generamos un arreglo que contenga a estos 28 mejores.
    '''

    best_countries = []

    for i in range(28):

        best_countries.append(nombres.pop(0))

    for i in range(1, len(fixture)):

        for j in range(len(fixture[i])):

            picked_country = random.choice(best_countries)
            fixture[i][j] = picked_country
            best_countries.remove(picked_country)

    return fixture


def search_in_fixture(fixture, countries):
    # Generamos un arreglo solo con los nombres de los países para poder manipularlos mejor.
    nombres = get_countries_names(countries)
    country = validate_and_return_country('Ingrese el nombre del país a buscar: ', nombres)

    groups = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

    for i in range(len(fixture)):

        for j in range(len(fixture[i])):

            if fixture[i][j] == country:

                print_green_text(f'\nPaís encontrado. {country} pertenece al grupo {groups[j]}')
                return

    print_green_text(f'\nLamentablemente, {country} no participa del mundial este año.')
