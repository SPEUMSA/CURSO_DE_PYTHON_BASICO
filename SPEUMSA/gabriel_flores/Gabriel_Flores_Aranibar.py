#Nombre: Gabriel Flores Aranibar
#Carrera: Ingeniería Química
#LIBRO Termodinámica - CAPÍTULO 8 "EXERGÍA" Ejercicio 8.30
#a) La cantidad de transferencia de calor al cuarto y 
#b) La cantidad máxima de calor que puede suministrarse al cuarto si el calor del radiador es suministrado
#   a la máquina térmica que está impulsado la bomba de calor. Suponga que la máquina térmica opera entre el radiador
#   y los alrededores.
#DATOS:
def litro(): #Definimos la función litro
    a = v/1000
    print (("Volumen en m3:"), (a))
def cm3():#Definimos la función cm3
    a = v*(10**(-6))
    print (("Volumen en m3"), (a))
def m3():#Definimos la función m3
    a = v
    print (("Volumen en m3"), (a))
#Ciclo while 
while True: #Creamos un bucle
    try: #Intentamos obtener los datos de entrada
        v= float(input("Ingrese el volumen del sistema \n"))
        print (("¿En qué unidad está tu volumen?")) #Preguntamos el volumen
        #Ofrecemos las opciones de volumen las cuales van a llamar a las funciones
        op = str(input("""
        1- Litro
        2- cm3
        3- m3   \n"""))
    except: #En caso de error:
        print ("Error")
        op = '?'
#If 
    if op == '1':#Si el usuario elige opción 1 llamamos a litro
        litro()
        break
    elif op == '2':#Si el usuario elige opción 2 llamamos a cm3
        cm3()
        break
    elif op == '3':#Si el usuario elige opción 3 llamamos a m3
        m3()
        break
    else:
        print ("""Has ingresado un sistema de unidades erróneo """)
v1= float(input("Ingrese el volumen de entrada [m3] \n"))
p1 = float(input("Ingrese la presión de entrada [kPa] \n"))
t1= float(input("Ingrese la temperatura de entrada [°C] \n"))
s1= float(input("Ingrese la entropía de tablas de vapor de tabla A-6 [kJ/kg*K] \n"))
v1 = float(input("Ingrese el volumen específico de tabla A-6 [m3/kg] \n"))
u1 = float(input("Ingrese la energía interna de tabla A-6 [kJ/kg] \n"))
#Datos de salida
t2= float(input("Ingrese la temperatura de salida [°C] \n"))
taire= float(input("Ingrese la temperatura del aire [°C] \n"))
talrededores= float(input("Ingrese la temperatura alrededores [°C] \n"))
vg= float(input("Ingrese el volumen específico de vapor de saturación de tabla A-4 a t2 [m3/kg] \n"))
vf= float(input("Ingrese el volumen específico de líquido saturado de tabla A-4 a t2 [m3/kg] \n"))
uf= float(input("Ingrese la energía interna de líquido saturado de tabla A-4 a t2 [kJ/kg] \n"))
ufg= float(input("Ingrese la energía interna de evaporación de tabla A-4 a t2 [kJ/kg] \n"))
sf= float(input("Ingrese la entropía de líquido saturado de tabla A-4 a t2 [kJ/kg*K] \n"))
sfg= float(input("Ingrese la entropía de evaporación de tabla A-4 a t2 [kJ/kg*K] \n"))
#Solución
#  
vfg= (vg-vf)
x2= (v1-vf)/vfg
u2= uf + (x2*ufg)
s2= sf + (x2*sfg)
m = v/v1
#Cálculo del calor
Q= m*(u1-u2)/1000
print (("a) Resultado del calor Q en kJ = "), (Q))
taire = taire + 273 #Temperatura en Kelvin
talrededores = talrededores + 273 #Temperatura en Kelvin
w = m*((u1-u2)-talrededores*(s1-s2))
QH = w/(1-(talrededores/taire))/1000
print (("b) Resultado del calor máximo QH en kJ = "), (QH))