# Definición de la clase país.
class Country:
    def __init__(self, confederation, name, points, wins):
        self.confederation = confederation
        self.name = name
        self.points = points
        self.wins = wins

    def __str__(self):
        # Decodificación de la confederación en base a su número de clave.
        as_string = ('UEFA', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC', 'OFC')
        
        # Formateo del string de salida para mostrar por terminal.
        s = "Confederación: {:<10} | Nombre: {:<30} | Puntos: {:<5} | Cantidad de campeonatos ganados: {:<5}"
        return s.format(as_string[self.confederation], self.name, self.points, self.wins)


class CountryWithoutConfederation:
    def __init__(self, name, points, wins):
        self.name = name
        self.points = points
        self.wins = wins

    def __str__(self):
        # Formateo del string de salida para mostrar por terminal.
        s = "Nombre: {:<30} | Puntos: {:<5} | Cantidad de campeonatos ganados: {:<5}"
        return s.format(self.name, self.points, self.wins)
