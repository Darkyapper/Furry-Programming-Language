import time

def read_file(nombre_archivo):
    if not nombre_archivo.endswith('.furro'):
        raise ValueError("Hit! (a97001): The file is not a .furro file!")

    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        if linea.strip().startswith('7u7'):
            continue
        show_res(linea.strip())

def print_e(message):
    print("\033[91m" + message + "\033[0m")

def print_a(message):
    print("\033[93m" + message + "\033[0m")

def show_res(linea):
    if linea.startswith('Scream'): # Mostrar un texto en la consola
        if '"' in linea:
            if linea.count('"') != 2:
                print_e("Damn! (x0001): Are you trying to scream in the wrong way!")
                return
            texto = linea.split('"')[1]
            print(texto)
        else:
            print_e("Damn! (x0001): Are you trying to scream in the wrong way!")
    elif linea.startswith('Wait'): # Esperar un tiempo
        tiempo_str = linea[len('Wait '):]
        try:
            segundos = int(tiempo_str)
        except ValueError:
            print_e("Damn! (x0002): You can't wait fractionally or decimal, little fox.")
            return
        time.sleep(segundos)
    elif linea.startswith('Hurray_End'): # Comprobar que el código se ejecutó hasta este punto
        print_a("Hit! (a97000): The code is executed successfully!")

    elif linea.startswith('Protogen.Plus'):
        args = linea.split('(')[1].split(')')[0].split(',')
        if len(args) != 2:
            print_e("Error: Sintaxis incorrecta para el comando Protogen.Plus")
            return
        try:
            resultado = float(args[0].strip()) + float(args[1].strip())
            print(resultado)
        except ValueError:
            print_e("Error: Los argumentos de Protogen.Plus deben ser números enteros o decimales.")
    elif linea.startswith('Protogen.Minus'):
        args = linea.split('(')[1].split(')')[0].split(',')
        if len(args) != 2:
            print_e("Error: Sintaxis incorrecta para el comando Protogen.Minus")
            return
        try:
            resultado = float(args[0].strip()) - float(args[1].strip())
            print(resultado)
        except ValueError:
            print_e("Error: Los argumentos de Protogen.Minus deben ser números enteros o decimales.")
    elif linea.startswith('Protogen.DivBy'):
        args = linea.split('(')[1].split(')')[0].split(',')
        if len(args) != 2:
            print_e("Error: Sintaxis incorrecta para el comando Protogen.DiBy")
            return
        try:
            resultado = float(args[0].strip()) / float(args[1].strip())
            print(resultado)
        except ValueError:
            print_e("Error: Los argumentos de Protogen.DiBy deben ser números enteros o decimales.")
        except ZeroDivisionError:
            print_e("Error: No se puede dividir entre cero")
    elif linea.startswith('Protogen.Times'):
        args = linea.split('(')[1].split(')')[0].split(',')
        if len(args) != 2:
            print_e("Error: Sintaxis incorrecta para el comando Protogen.Times")
            return
        try:
            resultado = float(args[0].strip()) * float(args[1].strip())
            print(resultado)
        except ValueError:
            print_e("Error: Los argumentos de Protogen.Times deben ser números enteros o decimales.")

    else:
        print_e(f"Damn! (x0000): What the hell means '{linea}' ?")
    

# Ejemplo de uso
read_file('pruebas.furro')