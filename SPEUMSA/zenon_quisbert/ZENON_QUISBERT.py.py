# Definición de constantes
GRAVITY = 9.81  # Aceleración debida a la gravedad en m/s²

# Clase para calcular la velocidad de sedimentación
class SedimentationCalculator:
    def __init__(self, radio_particula_mm, densidad_particula_gcc, densidad_fluido_gcc, viscosidad_fluido_mPas):
        self.radio_particula = radio_particula_mm / 1000.0  # Convertir de milímetros a metros
        self.densidad_particula = densidad_particula_gcc * 1000.0  # Convertir de gr/cc a kg/m³
        self.densidad_fluido = densidad_fluido_gcc * 1000.0  # Convertir de gr/cc a kg/m³
        self.viscosidad_fluido = viscosidad_fluido_mPas / 1000.0  # Convertir de mPas a Pa·s

    def calcular_velocidad_sedimentacion(self):
        # Calcular la velocidad de sedimentación usando la ecuación de Stokes
        velocidad_sedimentacion = (2.0 / 9.0) * ((self.radio_particula ** 2) * GRAVITY * (self.densidad_particula - self.densidad_fluido)) / self.viscosidad_fluido
        return velocidad_sedimentacion

    def calcular_velocidad_sedimentacion_con_organica(self, concentracion_organica, densidad_organica_gcc):
        # Calcular el efecto de las partículas orgánicas en la velocidad de sedimentación
        concentracion_fraccion = concentracion_organica / 100.0
        densidad_organica = densidad_organica_gcc * 1000.0  # Convertir de gr/cc a kg/m³
        velocidad_organica = concentracion_fraccion * (densidad_organica - self.densidad_fluido)
        
        # Calcular la velocidad de sedimentación total con materia orgánica
        velocidad_sedimentacion_con_organica = self.calcular_velocidad_sedimentacion() + velocidad_organica
        return velocidad_sedimentacion_con_organica

# Función para obtener datos del usuario y calcular la velocidad de sedimentación
def main():
    print("Cálculo de Velocidad de Sedimentación")
    radio_mm = float(input("Radio de la partícula (mm): "))
    densidad_particula_gcc = float(input("Densidad de la partícula (gr/cc): "))
    densidad_fluido_gcc = float(input("Densidad del fluido (gr/cc): "))
    viscosidad_fluido_mPas = float(input("Viscosidad del fluido (mPas): "))

    # Crear una instancia de la clase SedimentationCalculator
    calculadora = SedimentationCalculator(radio_mm, densidad_particula_gcc, densidad_fluido_gcc, viscosidad_fluido_mPas)

    # Preguntar si se tomará en cuenta la materia orgánica
    materia_organica = input("¿Se tomará en cuenta la materia orgánica en el cálculo? (s/n): ")
    if materia_organica.lower() == "s":
        concentracion_organica = float(input("Concentración de partículas orgánicas (%): "))
        densidad_organica_gcc = float(input("Densidad de la materia orgánica (gr/cc): "))
        # Calcular la velocidad de sedimentación con materia orgánica
        velocidad_sedimentacion = calculadora.calcular_velocidad_sedimentacion_con_organica(concentracion_organica, densidad_organica_gcc)
    else:
        # Calcular la velocidad de sedimentación sin materia orgánica
        velocidad_sedimentacion = calculadora.calcular_velocidad_sedimentacion()

    # Imprimir el resultado
    print(f"La velocidad de sedimentación es: {velocidad_sedimentacion:.2f} m/s")

if __name__ == "__main__":
    main()
