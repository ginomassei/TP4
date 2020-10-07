import os
import pickle
import country


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
def load_text_file_on_memory(path):
    readed_lines = []

    if not os.path.exists(path):
        # Checkea la existencia del archivo, si no existe, retorna el arreglo vacío.
        return readed_lines

    file = open(path, 'rt')
    while True:
        readed_line = file.readline()

        if readed_line == '':  # Si encuentra el EOF, termina.
            break

        if readed_line[-1] == '\n':  # Remover el caracter de salto de línea.
            readed_line = readed_line[:-1]

        readed_line_as_list = readed_line.split(',')
        readed_lines.append(readed_line_as_list)

    file.close()
    return readed_lines


def get_country(line):
    """
    Retorna un objeto del tipo País, tomando como parámetro una línea de datos.
    """
    confederation = int(line[0])
    name = line[1]
    points = int(line[2])
    wins = int(line[3])

    return country.Country(confederation, name, points, wins)


def add_in_order(v, r):
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].points == r.points:
            pos = med
            break

        if r.points > v[med].points:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [r]


def get_countries(readed_lines):
    """
    Transforma las líneas cargadas desde el .csv en objetos de tipo país.
    Retorna un arreglo de registros tipo País.
    """
    countries = []
    for line in readed_lines:
        country = get_country(line)  # Crea el país.
        add_in_order(countries, country)  # Lo añade de manera ordenada al arreglo.

    return countries


def get_wins_per_country(v):
    """
    Retorna un vector de conteos, con la cantidad de campeonatos ganados por país.
    """
    countries = get_countries_names(v)
    n = len(countries)

    wins = [0] * n
    wins_per_country = [[countries[i], wins[i]] for i in range(n)]

    for country in v:
        pass


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
    confederation = input('Ingrese la confederación de la cual desea obtener los países (Nombre en mayusculas): ')

    while confederation not in available_confederations:
        print_red_text('\nLa confederación ingresada no coincide con las cargadas en nuestros registros.')
        confederation = input('Ingrese la confederación de la cual desea obtener los países (Nombre en mayusculas): ')

    if confederation == 'UEFA':
        return 0
    elif confederation == 'CONMEBOL':
        return 1
    elif confederation == 'CONCACAF':
        return 2
    elif confederation == 'CAF':
        return 3
    elif confederation == 'AFC':
        return 4
    elif confederation == 'OFC':
        return 5


def get_countries_per_confederation(confederation_code, countries):
    countries_per_confederation = []
    for country in countries:
        if country.confederation == confederation_code:
            add_in_order(countries_per_confederation, country)

    return countries_per_confederation


def create_binary_file(array, path):
    file = open(path, 'wb')

    for element in array:
        pickle.dump(element, file)

    file.close()


def delete_atribute(atribute, array):
    for element in array:
        delattr(element, atribute)
