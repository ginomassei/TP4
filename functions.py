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
            add_in_order(countries_in_confederation, country)

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
