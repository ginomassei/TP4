import os
import country
import pickle


def generate_array(path):
    loaded_array = []
    if not os.path.exists(path):
        # Checkea la existencia del archivo, si no existe, retorna el arreglo vacío.
        return loaded_array

    file = open(path, 'rt')
    for line in file:
        country = get_country(line)
        add_in_order(loaded_array, country)

    file.close()
    return loaded_array


def get_country(line):
    """
    Retorna un objeto del tipo País, tomando como parámetro una línea de datos.
    """
    line = line.split(',')
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


def create_binary_file(array, path):
    file = open(path, 'wb')
    for element in array:
        pickle.dump(element, file)

    file.close()


def get_countries_from_file(path):
    countries = []

    file = open(path, 'rb')
    size = os.path.getsize(path)

    while file.tell() < size:
        countries.append(pickle.load(file))

    file.close()

    return countries


def delete_atribute(atribute, array):
    for element in array:
        delattr(element, atribute)
