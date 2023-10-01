# Primeramente usamos la funcion para class para colocar los atributos a las variable M y Y
class CalculadoraTemperaturaEbullicion:
    def __init__(self, M, Y):
        # En esta parte realizamos na condicional para determinar valor 
        # que sean menores a cero y que nos indique error debido a que no 
        # existen valores negativos de Peso molecular del carbono C
        if M < 0 or Y < 0:
            raise ValueError("Los valores de m y Y deben ser no negativos.")

        self.M = M
        self.Y = Y
#Con la siguiente linea de codigo ejecutamos el comando de temperatura
#de ebullicion desarrollado por Whitson
    def calcular_temperatura_ebullicion(self):
        T = ((4.5579 * self.M**0.15178) * (self.Y**0.15427))**3
        return T


M = float(input("Ingrese el valor de M: "))
Y = float(input("Ingrese el valor de Y: "))

# Crea una instancia de la clase y calcula la temperatura de ebullición
calculadora = CalculadoraTemperaturaEbullicion(M    , Y)
temperatura_resultante = calculadora.calcular_temperatura_ebullicion()

print(f"La temperatura de ebullición calculada es: {temperatura_resultante}")
# Usamos valores como 142 para el peso molecular Y
# 0.807 para la densidad relativa para que nos lanze 
# el resultado de la temperatura de ebullicion en grados Rankine

# puede tambien hacerse de manera simple y consisa pero sin una usar herramientas
# de clase y funciones nos imposiblita el uso en futuras ecuaciones


# def calcular_temperatura_ebullicion(m, Y):
#     if m < 0 or Y < 0:
#         raise ValueError("Los valores de m y Y deben ser no negativos.")
    
#     T = ((4.5579 * m**0.15178) * (Y**0.15427))**3
#     return T

# # Uso de la función
# m = float(input("Ingrese el valor de m: "))
# Y = float(input("Ingrese el valor de Y: "))
# temperatura_resultante = calcular_temperatura_ebullicion(m, Y)
# print(f"La temperatura de ebullición calculada es: {temperatura_resultante}")
