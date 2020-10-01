# ANSI colours functions.
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

        s = ''  # Formating the output sring.
        s += '{:<8}'.format('Confederación: ' + str(conf))
        s += '{:<15}'.format('Nombre: ' + str(self.name))
        s += '{:<5}'.format('Puntos: ' + str(self.points))
        s += '{:<3}'.format('Cantidad de campeonatos ganados: ' + str(self.wins))
        return s


# TP Functions.
def load_text_file(path):
    file = open(path, 'rt')
    pass


def add_in_order(p, country): 
    n = len(p)
    pos = n
    for i in range(n):
        if country.poits < p[i].points: 
            pos = i
            break

    p[pos:pos] = [country] 
