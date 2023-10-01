def calcular_presion_peng_robinson(T, P_sat, acentric_factor, R, Tc, Pc):
    """
    Esta función calcula la presión de un gas utilizando la ecuación de Peng-Robinson.
    
    :param T: Temperatura en Kelvin
    :param P_sat: Presión de saturación del componente puro en Pascales
    :param acentric_factor: Factor acentrico del componente puro
    :param R: Constante de los gases (por ejemplo, 8.314 J/(mol*K))
    :param Tc: Temperatura crítica del componente puro en Kelvin
    :param Pc: Presión crítica del componente puro en Pascales
    :return: Presión en Pascales
    """
    def peng_robinson_eqn(P):
        a = 0.45724 * R**2 * (Tc**2) / Pc
        b = 0.07780 * R * Tc / Pc
        alpha = (1 + (0.37464 + 1.54226 * acentric_factor - 0.26992 * acentric_factor**2) * (1 - (T / Tc)**0.5))**2
        A = a * alpha * P / (R**2 * T**2)
        B = b * P / (R * T)
        return P - (R * T / (V - B)) - (A / (V*(V + B) + B*(V - B)))
    
    # Inicialización de variables, si lo desea podrian ser cambiados estos valores :)
    V = 1.0
    tol = 1e-6
    max_iter = 1000
    
    # Iteración utilizando el método de Newton-Raphson; aquí mejor si no cambian :0
    for _ in range(max_iter):
        prev_V = V
        f = peng_robinson_eqn(P_sat)
        f_prime = (peng_robinson_eqn(V + 1e-6) - f) / 1e-6
        V = V - f / f_prime
        if abs(V - prev_V) < tol:
            break
    
    Z = P_sat * V / (R * T)
    P = Z * R * T / V
    return P

# los datos con los que se podran generar las operaciones necesarias depende de ti si los cambias para lo que necesites;)
T = int (input("temperatura="))  # Kelvin
P_sat = int (input("Presión de saturación")) # Presión de saturación en Pascales
acentric_factor = 0.344
R = 8.314  # J/(mol*K)
Tc = int (input ("Temperatura crítica del componente puro"))  # Kelvin
Pc = int (input ("Presión crítica del componente puro"))  # Presión crítica en Pascales

presion = calcular_presion_peng_robinson(T, P_sat, acentric_factor, R, Tc, Pc)
print(f'La presión calculada utilizando la ecuación de Peng-Robinson es {presion} Pascales.')
