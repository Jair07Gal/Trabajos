def calcular_imc(peso_kg, altura_m):
    """
    Calcula el índice de masa corporal (IMC) dado el peso en kilogramos y la altura en metros.
    """
    imc = peso_kg / (altura_m ** 2)
    return imc

def main():
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))
        imc_resultado = calcular_imc(peso, altura)
        print(f"Tu IMC es: {imc_resultado:.2f}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos para peso y altura.")

if __name__ == "__main__":
    main()
