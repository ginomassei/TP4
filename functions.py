import os

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


def striketrought_print(string):
    crossed_text = '\033[09;37;37m'
    reset_text = '\033[m'

    print(crossed_text + string + reset_text)


# Definición de la clase país.
class Country:
    def __init__(self, confederation, name, points, wins):
        self.confederation = confederation
        self.name = name
        self.points = points
        self.wins = wins

    def __str__(self):
        # Decodificación de la confederación en base a su número de clave.
        conf = ''
        if self.confederation == 0:
            conf = 'UEFA'
        elif self.confederation == 1:
            conf = 'CONMEBOL'
        elif self.confederation == 2:
            conf = 'CONCACAF'
        elif self.confederation == 3:
            conf = 'CAF'
        elif self.confederation == 4:
            conf = 'AFC'
        elif self.confederation == 5:
            conf = 'OFC'

        # Formateo del string de salida para mostrar por terminal.
        s = "Confederación: {:<10} | Nombre: {:<30} | Puntos: {:<5} | Cantidad de campeonatos ganados: {:<5}"
        return s.format(conf, self.name, self.points, self.wins)


# Finciones para el desarollo del tp.
def load_text_file(path):
    """
    Carga en memoria un archivo de texto .csv y retorna un arreglo de dos dimensiones con los valores de cada línea.
    Retorna 0 si no encuentra el archivo.
    """
    v = []

    if not os.path.exists(path):
        return 0  # Checkea la existencia del archivo, si no existe retorna 0.

    file = open(path, 'rt')    
    while True:
        line = file.readline()

        if line == '':  # Si encuentra el EOF, termina.
            break
        
        if line[-1] == '\n':  # Remover el caracter de salto de línea.
            line = line[:-1]

        line = line.split(',')  # Divide cada línea por las comas, para crear así un arreglo con los atributos.
        v.append(line)  # Segunda dimension del arreglo, ahora es un arreglo de líneas.

    file.close()
    return v


def make_object(line):
    """
    Retorna un objeto del tipo País, tomando como parámetro una línea de datos.
    """
    confederation = int(line[0])
    name = line[1]
    points = int(line[2])
    wins = int(line[3])

    return Country(confederation, name, points, wins)


def add_in_order(p, country):
    """
    Tomando un vector, añade un objeto del tipo país en orden al mismo, por puntos.
    """
    n = len(p)
    pos = n
    for i in range(n):
        if country.points > p[i].points:  # Comparo en base a los puntos.
            pos = i
            break

    p[pos:pos] = [country] 


def object_loader(lines):
    """
    Transforma las líneas cargadas desde el .csv en objetos de tipo país.
    Retorna un arreglo de registros tipo País.
    """
    v = []
    for element in lines:
        country = make_object(element)  # Crea el país.
        add_in_order(v, country)  # Lo añade de manera ordenada al arreglo.

    return v
