import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        suposicion = int(input("Introduce tu suposición: "))
        intentos += 1

        if suposicion < numero_secreto:
            print("Mi número es mayor. ¡Sigue intentándolo!")
        elif suposicion > numero_secreto:
            print("Mi número es menor. ¡Sigue intentándolo!")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    jugar_adivinanza()
