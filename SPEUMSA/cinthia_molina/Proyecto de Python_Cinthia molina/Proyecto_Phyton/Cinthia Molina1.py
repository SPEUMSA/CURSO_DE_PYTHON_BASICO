class Persona:
    def __init__(self):
        self.tarifas_envio = {
            'EEUU': 10,
            'Canadá': 15,
            'México': 12,
            'España': 20,
            'Bolivia':15,
            'Argentina':25


        }

    def calcular_costo_envio(self, total_carrito, pais_residencia):
        costo_envio = 0


        if pais_residencia in self.tarifas_envio:
            costo_envio = self.tarifas_envio[pais_residencia]
        else:
            print("Lo siento, no podemos realizar envíos a ese país.")


        costo_total = total_carrito + costo_envio


        print(f"El costo de envío a {pais_residencia} es de ${costo_envio}.")
        print(f"El costo total del carrito es de ${costo_total}.")


total_carrito = float(input("Ingrese el total del carrito: "))
pais_residencia = input("Ingrese el país de residencia: ")

envio = Persona()
envio.calcular_costo_envio(total_carrito, pais_residencia)