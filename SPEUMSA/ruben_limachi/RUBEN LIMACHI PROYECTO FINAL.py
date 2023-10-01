#utilizando la correlacion Glaso determinar la viscosidad de un crudo 
#de 31° api a 180 °F 4000 lpca, el cual tiene un razon de gas disuelto-petroleo de 675 PCN/BN 
#a su presion de burbujeo de 2500 lpca 
print("Correlacion de Glaso para Crudo muerto")
import math
def calcular_viscosidad_del_crudo(T, API):
  viscosidad=3.141*(1e10)*((T)**(-3.444))*((math.log10(API))**(10.313*(math.log10(T))-36.447)) 
  print(viscosidad)
                                              
T = int(input("Inserte temp. en °F = ")) 
API = int(input("API del crudo =")) 
if T==0 and API==0:
    print("inserte un numero positivo")
else:
    calcular_viscosidad_del_crudo(T,API)
    

    