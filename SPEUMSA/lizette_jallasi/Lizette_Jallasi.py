# EJERCCICIO 1.70
# Constantes
peso_esp_h20 = 62.4 # Lbm/ft^3
SG_hg = 13.6  
SG_oil = 0.69
g = 32.2  # ft/s^2
peso_esp_hg=peso_esp_h20*SG_hg
peso_esp_oil=peso_esp_h20*SG_oil

# Definir la función para calcular la presion 1
def calcular_presion_gas(Patm, H_hg,h1, hoil):
    P1 = Patm + (peso_esp_hg * g*H_hg +peso_esp_h20*g*h1-peso_esp_oil*g*hoil)*(1/32.2)*(1/144)

    return P1

# Obtener datos de entrada
Patm = float(input("Ingrese la presión: "))
H_hg = float(input("Ingrese la altura de liquido de hg : "))
h1 = float(input("Ingrese la altura de liquido de agua: "))
hoil= float(input("ingrese la altura de aceite: "))

# Calcular la presion
P1 = calcular_presion_gas(Patm, H_hg,h1, hoil)
# Imprimir el resultado
print("La presion del gas es:", P1, "psi.")
