import functions as f


def main():
    f.print_blue_text('TP4 Sistema de Gestión de una Competencia Mundial.\n')
    print('-' * 80)
    

    option = -1
    while option != 0:
        f.print_blue_text('Opciones: ')
        print('\n1 - Mostrar el listado completo de países.')
        print('2 - Mostrár país con mayor cantidad de campeonatos ganados.')
        print('3 - Mostrar los países que ganaron algún campeonato.')
        print('4 - Generar nuevo vector con paises de alguna confederación.')

        print('0 - Salir.')

        option = int(input('\nIngrese su opción: '))

        if option == 0:
            f.print_blue_text('\nPrograma finalizado...')

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
