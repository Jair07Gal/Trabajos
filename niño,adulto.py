def clasi(edad):
    if edad >= 0 and edad <= 2:
        return "Bebé"
    elif edad >= 3 and edad <= 11:
        return "Niño"
    elif edad >= 12 and edad <= 17:
        return "Adolescente"
    elif edad >= 18 and edad <= 64:
        return "Adulto"
    elif edad >= 65:
        return "Anciano"
    else:
        return "Edad inválida"

edad_usuario = int(input("Dime tu edad: "))
N = clasi(edad_usuario)
print(f"Eres un {N}.")
