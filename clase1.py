# Acceso a los atributos y métodos de un objeto
# -------------------------------------------------------------------------------
c = "Python"
print(c.upper())  # Llamada al método upper del objeto c (cadena)

l = [1, 2, 3]
l.append(4)  # Llamada al método append del objeto l (lista)
print(l)
# -------------------------------------------------------------------------------

# Clases
# -------------------------------------------------------------------------------


class Saludo:
    pass  # Clase vacía sin atributos ni métodos.


print(Saludo)
# -------------------------------------------------------------------------------

# Clases primitivas
# -------------------------------------------------------------------------------
type(1)
type(1.5)
type("Python")
type([1, 2, 3])
type((1, 2, 3))
type({1: "A", 2: "B"})
# -------------------------------------------------------------------------------


# Instanciación de clases
# -------------------------------------------------------------------------------
class Saludo:
    pass  # Clase vacía sin atributos ni métodos.


s = Saludo()  # Creación del objeto mediante instanciación de la clase.
print(s)
# <__main__.Saludo object at 0x7fcfc7756be0>      # Dirección de memoria donde se crea el objeto
type(s)
# <class '__main__.Saludo'>     # Clase del objeto
# -------------------------------------------------------------------------------


# Definición de métodos
# -------------------------------------------------------------------------------
class Saludo:
    mensaje = "Bienvenido "  # Definición de un atributo

    def saludar(self, nombre):  # Definición de un método
        print(self.mensaje + nombre)
        return


s = Saludo()
s.saludar("Alf")
# -------------------------------------------------------------------------------


# El método __init__
# -------------------------------------------------------------------------------
class Tarjeta:
    def __init__(self, id, cantidad=0):  # Inicializador
        self.id = id  # Creación del atributo id
        self.saldo = cantidad  # Creación del atributo saldo
        return

    def mostrar_saldo(self):
        print("El saldo es", self.saldo, "€")
        return


t = Tarjeta("1111111111", 1000)  # Creación de un objeto con argumentos
t.mostrar_saldo()
# -------------------------------------------------------------------------------


# Atributos de instancia vs atributos de clase
# -------------------------------------------------------------------------------
class Circulo:
    pi = 3.14159  # Atributo de clase

    def __init__(self, radio):
        self.radio = radio  # Atributo de instancia

    def area(self):
        return Circulo.pi * self.radio**2


c1 = Circulo(2)
c2 = Circulo(3)
print(c1.area())
print(c2.area())
print(c1.pi)
print(c2.pi)
# -------------------------------------------------------------------------------


# El método __str__
# -------------------------------------------------------------------------------
class Tarjeta:
    def __init__(self, numero, cantidad=0):
        self.numero = numero
        self.saldo = cantidad
        return

    def __str__(self):
        return "Tarjeta número {} con saldo {}€".format(self.numero, str(self.saldo))


t = Tarjeta("0123456789", 1000)
print(t)
# -------------------------------------------------------------------------------


# Herencia
# -------------------------------------------------------------------------------
class Tarjeta:
    def __init__(self, id, cantidad=0):
        self.id = id
        self.saldo = cantidad
        return

    def mostrar_saldo(
        self,
    ):  # Método de la clase Tarjeta que hereda la clase Tarjeta_descuento
        print("El saldo es", self.saldo, "€.")
        return


class Tarjeta_descuento(Tarjeta):
    def __init__(self, id, descuento, cantidad=0):
        self.id = id
        self.descuento = descuento
        self.saldo = cantidad
        return

    def mostrar_descuento(self):  # Método exclusivo de la clase Tarjeta_descuento
        print("Descuento de", self.descuento, "% en los pagos.")
        return


t = Tarjeta_descuento("0123456789", 2, 1000)
t.mostrar_saldo()
t.mostrar_descuento()
# -------------------------------------------------------------------------------

# Jerarquia de clases
# -------------------------------------------------------------------------------

t1 = Tarjeta("1111111111", 0)
t2 = t = Tarjeta_descuento("2222222222", 2, 1000)
print(isinstance(t1, Tarjeta))
print(isinstance(t1, Tarjeta_descuento))
print(isinstance(t2, Tarjeta_descuento))
print(isinstance(t2, Tarjeta))
# -------------------------------------------------------------------------------


# Sobrecarga y polimorfismo
# -------------------------------------------------------------------------------
class Tarjeta:
    def __init__(self, id, cantidad=0):
        self.id = id
        self.saldo = cantidad
        return

    def mostrar_saldo(self):
        print("El saldo es {:.2f}€.".format(self.saldo))
        return

    def pagar(self, cantidad):
        self.saldo -= cantidad
        return


class Tarjeta_Oro(Tarjeta):
    def __init__(self, id, descuento, cantidad=0):
        self.id = id
        self.descuento = descuento
        self.saldo = cantidad
        return

    def pagar(self, cantidad):
        self.saldo -= cantidad * (1 - self.descuento)


t1 = Tarjeta("1111111111", 1000)
t2 = Tarjeta_Oro("2222222222", 1, 1000)
t1.pagar(100)
t1.mostrar_saldo()
t2.pagar(100)
t2.mostrar_saldo()
# -------------------------------------------------------------------------------
