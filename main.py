import functions as f


def main():
    f.print_blue_text('TP4 Sistema de Gestión de una Competencia Mundial.\n')
    print('-' * 80)
    v = []

    option = -1
    while option != 0:
        f.print_blue_text('Opciones: ')
        print('\n1 - Cargar el archivo.')
        print('2 - Mostrar el listado completo de países.')
        print('3 - Mostrár país con mayor cantidad de campeonatos ganados.')
        print('4 - Mostrar los países que ganaron algún campeonato.')
        print('5 - Generar nuevo vector con paises de alguna confederación.')

        print('0 - Salir.')

        option = int(input('\nIngrese su opción: '))
        print()

        if option == 0:
            f.print_blue_text('Programa finalizado...')

        if option == 1:
            v = f.load_text_file_on_memory('paises.csv')
            v = f.object_loader(v)

            f.print_green_text('Archivo cargado en memoria correctamente.')

        elif option == 2:
            if len(v) != 0:
                f.print_blue_text('Listado completo de países: \n')
                for country in v:
                    print(country)
            else:
                f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')

        elif option == 3:
            if len(v) != 0:
                f.count_wins(v)
            else:
                f.print_red_text('No se encuentra ningún registro en memoria, por favor cárguelo con la opcion 1.')
        
        elif option == 4:
            pass

        print('-' * 80)


if __name__ == "__main__":
    main()
