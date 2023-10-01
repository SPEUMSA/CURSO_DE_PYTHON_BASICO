# Utilizando la correlacion de Standing, M.B., Determinar el factor volumetrico del petroleo a presiones de 2000, 2500 y 3000 lpca
# Dado los siguientes datos:
        # Pb = 2500 (lpca)
        # T = 180 (ºF)
        # GE_api = 31 (ªAPI)
        # GE_g = 0.95
        # Co = 9.61 * 10 ** -6 (lpc**-1)

# Calculando Rs "Razon de Petroleo"
# P1 = 2000 #lpca
# P2 = 2500 #lpca
# P3 = 3000 #lpca
import math

Pb = 2500 #lpca
T = 180 #ºF
GE_api = 31 #ºAPI
GE_g = 0.95
Co = 9.61 * 10 ** -6 #lpc**-1

P = int(input("Ingresa la presion: \n"))

if P > Pb:
    Presion = Pb
elif P < Pb:
    Presion = P
else:
    Presion = Pb

Rs = GE_g * (((Presion / 18.2)+1.4) * 10 ** (0.0125 * GE_api - 0.00091 * T)) ** 1.2048 


F = Rs * (GE_g/(141.5/(GE_api + 131.5))) ** (1/2) + 1.25 * T


Bo = 0.9759 + (12 * 10 ** -5) * (F ** 1.2)

Bop = Bo * math.e**(Co * (Pb - P))

if P > Pb:
    print(f"Bop= {Bop:.5f}", f"BY/BN")
elif P < Pb:
    print(f"Bo= {Bo:.5f}", f"BY/BN")
else:
    print(f"Bo= {Bo:.5f}", f"BY/BN")

