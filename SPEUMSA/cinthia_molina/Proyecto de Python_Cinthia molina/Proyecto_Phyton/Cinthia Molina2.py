class AnioBisiesto:
    def __init__(self, anio):
        self.anio = anio

    def es_bisiesto(self):
        if (self.anio % 4 == 0 and self.anio % 100 != 0) or (self.anio % 400 == 0):
            return True
        else:
            return False
if __name__ == '__main__':


    anio_usuario = int(input("Ingrese un año: "))
    anio = AnioBisiesto(anio_usuario)

    if anio.es_bisiesto():
        print(f"{anio_usuario} es un año bisiesto.")
    else:
        print(f"{anio_usuario} no es un año bisiesto.")

