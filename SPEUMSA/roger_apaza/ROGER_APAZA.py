#Funcion de calculo de la altura para el agua
def alturaH2O():
    if densidadH2O==0 and gravedad==0:
        print("Revise si el ingreso de datos es correcto")
    else:
        altura=(1000*presion)/(densidadH2O*gravedad)
        print(("La altura para el agua es:"),(altura),(" metros"))

#Funcion de calculo de la altura para el mercurio
def alturaHg():
    if densidadHg==0 and gravedad==0:
        print("Revise si el ingreso de datos es correcto")
    else:
        altura=(1000*presion)/(densidadHg*gravedad)
        print(("La altura para el mercurio es:"),(altura),(" metros"))

while True: 
    try:
        #Ingreso de datos para el ejercicio
        presion=float(input("Ingresa la presion en kPa :\n"))
        densidadH2O=float(input("Ingresa la densidad del agua en kg/m3:\n"))
        densidadHg=float(input("Ingresa la densidad del mercurio en kg/m3:\n"))
        gravedad=float(input("Ingresa la gravedad en m/s2:\n"))

        #Lista para elegir que calcular
        print(("Que altura desea calcular: "),("?\n"))
        op=str(input(""" 
               1- Altura_de_H2O
               2- Altura_de_Hg\n"""))
    except:
        print("Error")
        op='?'
    
    #Aplicar funcion para la altura del agua
    if op=='1':
        alturaH2O()
        break

    #Aplicar funcion para la altura del mercurio
    elif op=='2':
        alturaHg()
        break
    else:
        print("""Has ingresado un numero de valor erroneo""")
