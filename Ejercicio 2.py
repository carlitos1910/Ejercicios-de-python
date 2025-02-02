Rama 1
def calcular_letra_dni(dni):
    """Calcula la letra del DNI a partir del número."""
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    residuo = dni % 23
    return letras[residuo]
Rama 2
def validar_dni_completo(dni, letra):
    """Valida si la letra proporcionada corresponde al número del DNI."""
    return calcular_letra_dni(dni) == letra.upper()
Rama 3
def main():
    """Función principal para solicitar opciones al usuario."""
    while True:
        print("\nOpciones:")
        print("1. Calcular la letra del DNI")
        print("2. Validar un DNI completo (número + letra)")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1, 2 o 3): ")
        
        if opcion == '1':
            while True:
                try:
                    dni = int(input("Introduce el número del DNI (sin letra): "))
                    if dni < 0:
                        print("Por favor, introduce un número válido.")
                        continue
                    letra = calcular_letra_dni(dni)
                    print(f"La letra correspondiente al DNI {dni} es: {letra}")
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, introduce un número entero.")

        elif opcion == '2':
            while True:
                try:
                    dni = int(input("Introduce el número del DNI (sin letra): "))
                    letra = input("Introduce la letra del DNI: ")
                    if dni < 0 or len(letra) != 1 or not letra.isalpha():
                        print("Por favor, introduce un número y una letra válidos.")
                        continue
                    if validar_dni_completo(dni, letra):
                        print(f"El DNI {dni}{letra} es válido.")
                    else:
                        print(f"El DNI {dni}{letra} no es válido.")
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, introduce un número entero.")

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()
