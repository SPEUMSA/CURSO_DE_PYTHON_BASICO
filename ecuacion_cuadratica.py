import math


def ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        # Dos raíces reales distintas
        raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return raiz1, raiz2
    elif discriminante == 0:
        # Una única raíz real (raíz doble)
        raiz = -b / (2 * a)
        return raiz
    else:
        # Raíces imaginarias
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-discriminante) / (2 * a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2
