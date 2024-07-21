def main():
    try:
        # Solicita al usuario ingresar dos números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Calcula la suma
        suma = num1 + num2

        # Muestra el resultado
        print(f"La suma de {num1} y {num2} es igual a {suma}")
    except ValueError:
        print("Ingresa números válidos.")

if __name__ == "__main__":
    main()
