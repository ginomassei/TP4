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


def main():
    print_blue_text('TP4 Sistema de Gestión de una Competencia Mundial.\n')
    print('-' * 80)
    

    option = -1
    while option != 0:
        print_blue_text('Opciones: ')
        print('\n1 - Mostrar el listado completo de países.')
        print('2 - Mostrár país con mayor cantidad de campeonatos ganados.')
        print('3 - Mostrar los países que ganaron algún campeonato.')
        print('4 - Generar nuevo vector con paises de alguna confederación.')

        print('0 - Salir.')

        option = int(input('\nIngrese su opción: '))

        if option == 1:
            pass

        elif option == 2:
            pass

        elif option == 3:
            pass
        
        elif option == 4:
            pass

        print('-' * 80)


if __name__ == "__main__":
    main()
