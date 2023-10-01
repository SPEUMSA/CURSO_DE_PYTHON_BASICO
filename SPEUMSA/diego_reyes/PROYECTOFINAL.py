

#INTRODUCIR PRESION Y TEMPERATURA DEL RESERVORIO

Tr = float(input("INGRESE LA TEMPERATURA DE RESERVORIO EN R: "))
Pr = float(input("INGRESE LA PRESION DE RESERVORIO EN PSI: "))

#INTRODUCIR GRAVEDAD ESPECIFICA

SG = float(input("INGRESE LA GRAVEDAD ESPECIFICA DEL FLUIDO: "))

#CÁLCULO DE LAS CONDICIONES PSEUDOCRITICAS
#CÁLCULO DE Tpc y Ppc

Tpc = 170.5 + 307.3*SG
Ppc = 709.6 - 58.7*SG

#CÁLCULO DE LA CONDICONES PSEUDOREDUCIDAS
#CÁLCULO DE Tpr y Ppr

Tpr = Tr/Tpc
Ppr = Pr/Ppc


#CONSTANTES FIJAS
A1 = 0.3265
A2 = -1.07
A3 = -0.5339
A4 = 0.01569
A5 = -0.05165
A6 = 0.5475
A7 = -0.7361
A8 = 0.1844
A9 = 0.1056
A10 = 0.6134
A11 = 0.721

#CÁLCULO DE CONSTANTES

K1 = (A1 + A2/Tpr + A3/Tpr**3 + A4/Tpr**4 + A5/Tpr**5)
K2 = (A6 + A7/Tpr + A8/Tpr**2)
K3 = (A9*(A7/Tpr + A8/Tpr**2))
K4 = (0.27*Ppr/Tpr)

#CÁLCULO DE LA DENSIDAD PSEUDOREDUCIDA (d)


dc = 1
dif = 0.1

while dif > 0.00000000001:

    d = dc
    dc = K4/(K1*d + K2*(d**2) - K3*(d**5) + (A10*(1 + A11*(d**2))*((d**2)/(Tpr**3))*(2.71828182845905**(-A11*(d**2)))) + 1)

    dif = abs((d-dc)/d)
    
prom = (d+dc)/2

#CÁLCULO DEL VALOR DE Z

Z = ((0.27*Ppr)/(prom*Tpr))

print(("El valor de Z es: "), (Z))

# print(Ppc)
# print(Tpc)
# print(Ppr)
# print(Tpr)
# print(K1)
# print(K2)
# print(K3)
# print(K4)

