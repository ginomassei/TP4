# Definición de la clase país.
class Country:
    def __init__(self, confederation, name, points, wins):
        self.confederation = confederation
        self.name = name
        self.points = points
        self.wins = wins

    def __str__(self):
        # Decodificación de la confederación en base a su número de clave.
        confederation_as_string = ''
        if self.confederation == 0:
            confederation_as_string = 'UEFA'
        elif self.confederation == 1:
            confederation_as_string = 'CONMEBOL'
        elif self.confederation == 2:
            confederation_as_string = 'CONCACAF'
        elif self.confederation == 3:
            confederation_as_string = 'CAF'
        elif self.confederation == 4:
            confederation_as_string = 'AFC'
        elif self.confederation == 5:
            confederation_as_string = 'OFC'

        # Formateo del string de salida para mostrar por terminal.
        s = "Confederación: {:<10} | Nombre: {:<30} | Puntos: {:<5} | Cantidad de campeonatos ganados: {:<5}"
        return s.format(confederation_as_string, self.name, self.points, self.wins)
