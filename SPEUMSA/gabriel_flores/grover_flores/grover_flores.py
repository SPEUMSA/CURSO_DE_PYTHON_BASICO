while True:
    year = input('Introduce un año para saber si es bisiesto o "FIN" para salir: ')
    if year.upper() == 'FIN':
        break  # Se sale del bucle si el usuario ingresa "FIN"
    try:
        year = int(year)
        if 1000 <= year <= 9999:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        resultado = 'SI ES BISIESTO'
                    else:
                        resultado = 'NO ES BISIESTO'
                else:
                    resultado = 'SI ES BISIESTO'
            else:
                resultado = 'NO ES BISIESTO'
            print('El año ',year,resultado)
        else:
            print("Introduce un año válido con exactamente 4 dígitos >= 1000 y <= 9999.")
    except ValueError:
        print("Introduce un año válido.")