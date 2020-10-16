import os
import pickle
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
    countries_per_confederation = [0] * 6
    for i in range(len(countries_per_confederation)):
        countries_per_confederation[i] = get_countries_in_confederation(i, countries)

    return countries_per_confederation


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


def validate_and_return_country(text, countries):
    name = input(text)
    validated = False
    while not validated:
        for i in countries:
            if name.lower() == i.lower():
                print_green_text('\nPaís validado.')
                return i

        print_red_text('\nEl país ingresado no existe.')
        name = input(text)


def get_new_fixture(countries):
    groups_number = 8
    participants_per_group = 4
    # Generamos un arreglo solo con los nombres de los países para poder manipularlos mejor.
    nombres = get_countries_names(countries)

    fixture = [[None] * groups_number for i in range(participants_per_group)]
    
    org = validate_and_return_country('Ingrese el nombre del país organizador: ', nombres)
    fixture[0][0] = org
    nombres.remove(org)
    
    '''
    Obtenemos los cabeza de serie (el arreglo original se ordenó previamente por puntaje de mayor a menor) y los
    eliminamos para evitar repeticiones.
    El índice del país a retornar es siempre 0 ya que se van desplazando los elementos restantes.
    '''

    for i in range(groups_number - 1):
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


def show_fixture(fixture):
    header = "| {:^15} " * 8 + "|"
    header = header.format('Grupo A', 'Grupo B', 'Grupo C', 'Grupo D', 'Grupo E', 'Grupo F', 'Grupo G', 'Grupo H')

    print('-' * 145)
    print(header)
    print('-' * 145)

    for row in fixture:
        s = "| {:^15} " * 8 + "|"
        s = s.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]))
        print(s)
        print('-' * 145)
