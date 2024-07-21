from datetime import datetime, date

# Solicitar la fecha de nacimiento al usuario
while True:
    fecha_str = input('\nIngrese fecha "aaaa/mm/dd": ')
    try:
        fecha = datetime.strptime(fecha_str, '%Y/%m/%d')
        fecha_str = fecha.strftime('%d-%m-%Y')
        print(f'\nTu fecha es: {fecha_str}')
    except ValueError:
        print("\nNo has ingresado una fecha correcta...")
    else:
        break

# Calcular la edad en años
hoy = date.today()
dias_transcurridos = (hoy - fecha).days
años = dias_transcurridos // 365
print(f'Tienes {años} años')
