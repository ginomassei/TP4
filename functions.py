# ANSI colours functions.
import io, os


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


# Class definition.
class Country:
    def __init__(self, confederation, name, points, wins):
        self.confederation = confederation
        self.name = name
        self.points = points
        self.wins = wins

    def __str__(self):
        # Defining confederation name based in the code.
        conf = ''
        if self.confederation == 0:
            conf = 'UEFA'
        elif self.confederation == 1:
            conf = 'CONCACAF'
        elif self.confederation == 2:
            conf = 'CAF'
        elif self.confederation == 4:
            conf = 'AFC'
        elif self.confederation == 5:
            conf = 'OFC'

        # Formating the output sring.
        s = "Confederación: {:<10} | Nombre: {:<25} | Puntos: {:<5} | Cantidad de campeonatos ganados: {:<5}"
        return s.format(conf, self.name, self.points, self.wins)


# TP Functions.
def load_text_file(path):
    v = []

    if not os.path.exists(path):
        return 0  # If the file not exists.

    file = open(path, 'rt')    
    while True:
        line = file.readline()

        if line == '':  # If EOF brake.
            break
        
        if line[-1] == '\n':
            line = line[:-1]

        line = line.split(',')
        add_in_order(v, make_object(line))

    file.close()
    return v


def make_object(line):
    confederation = int(line[0])
    name = line[1]
    points = int(line[2])
    wins = int(line[3])

    return Country(confederation, name, points, wins)


def add_in_order(p, country): 
    n = len(p)
    pos = n
    for i in range(n):
        if country.points < p[i].points: 
            pos = i
            break

    p[pos:pos] = [country] 
