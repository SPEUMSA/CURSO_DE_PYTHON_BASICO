def peso_en_tierra(masa):
    gravedad_tierra = 9.81 
    peso = masa * gravedad_tierra
    return peso
def peso(masa, gravedad):
    peso = masa * gravedad
    return peso

print(peso(23,9.81))

