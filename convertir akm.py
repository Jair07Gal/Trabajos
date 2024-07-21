def convertir_longitud():
    print("1. Milímetro (mm)")
    print("2. Centímetro (cm)")
    print("3. Metro (m)")
    print("4. Kilómetro (km)")
    opcion_origen = int(input("Selecciona la unidad de longitud de origen (1-4): "))
    valor_origen = float(input("Ingresa el valor en la unidad de origen: "))

    if opcion_origen == 1:
        valor_convertido = valor_origen / 1000
    elif opcion_origen == 2:
        valor_convertido = valor_origen / 100
    elif opcion_origen == 3:
        valor_convertido = valor_origen
    elif opcion_origen == 4:
        valor_convertido = valor_origen * 1000
    else:
        print("Opción no válida. Inténtalo nuevamente.")
        return

    print(f"Valor convertido: {valor_convertido:.2f} metros")

def convertir_masa():
    print("1. Miligramo (mg)")
    print("2. Gramo (g)")
    print("3. Kilogramo (kg)")
    opcion_origen = int(input("Selecciona la unidad de masa de origen (1-3): "))
    valor_origen = float(input("Ingresa el valor en la unidad de origen: "))

    if opcion_origen == 1:
        valor_convertido = valor_origen / 1000
    elif opcion_origen == 2:
        valor_convertido = valor_origen
    elif opcion_origen == 3:
        valor_convertido = valor_origen * 1000
    else:
        print("Opción no válida. Inténtalo nuevamente.")
        return

    print(f"Valor convertido: {valor_convertido:.2f} kilogramos")

def convertir_temperatura():
    print("1. Grados Celsius (°C)")
    print("2. Grados Fahrenheit (°F)")
    opcion_origen = int(input("Selecciona la unidad de temperatura de origen (1-2): "))
    valor_origen = float(input("Ingresa el valor en la unidad de origen: "))

    if opcion_origen == 1:
        valor_convertido = (valor_origen * 9/5) + 32
    elif opcion_origen == 2:
        valor_convertido = (valor_origen - 32) * 5/9
    else:
        print("Opción no válida. Inténtalo nuevamente.")
        return

    print(f"Valor convertido: {valor_convertido:.2f} grados")

# Menú principal
while True:
    print("\n--- Conversor de unidades ---")
    print("1. Longitud")
    print("2. Masa")
    print("3. Temperatura")
    print("4. Salir")
    opcion_menu = int(input("Selecciona una opción (1-4): "))

    if opcion_menu == 1:
        convertir_longitud()
    elif opcion_menu == 2:
        convertir_masa()
    elif opcion_menu == 3:
        convertir_temperatura()
    elif opcion_menu == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo nuevamente.")
