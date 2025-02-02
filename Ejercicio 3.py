Rama 1
def leibniz_series(n):
    """Calcula la suma de la serie de Leibniz hasta n términos."""
    suma = 0
    for k in range(1, n + 1):
        suma += (-1)**(k + 1) / (2 * k - 1)
    return suma
Rama 2
def calculate_pi(n):
    """Calcula el valor de π utilizando la serie de Leibniz."""
    suma = leibniz_series(n)
    pi_approximation = 4 * suma
    return pi_approximation
Rama 3
def main():
    """Función principal para ejecutar el cálculo de π."""
    n = 200
    pi_value = calculate_pi(n)
    print(f"El valor aproximado de π con n={n} es: {pi_value}")

if __name__ == "__main__":
    main()
