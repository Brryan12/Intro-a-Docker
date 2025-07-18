def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

def calculadora():
    print("Calculadora simple")
    while True:
        print("\nOpciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == '5':
            print("Saliendo...")
            break

        if opcion not in ['1', '2', '3', '4']:
            print("Opción inválida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor ingresa números.")
            continue

        if opcion == '1':
            resultado = suma(num1, num2)
        elif opcion == '2':
            resultado = resta(num1, num2)
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
        elif opcion == '4':
            resultado = division(num1, num2)

        print(f"Resultado: {resultado}")
        input("Presione ENTER para continuar")

if __name__ == "__main__":
    calculadora()
