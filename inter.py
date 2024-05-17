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
    if linea.startswith('Scream'):
        if '"' in linea:
            if linea.count('"') != 2:
                print_e("Damn! (x0001): Are you trying to scream in the wrong way!")
                return
            texto = linea.split('"')[1]
            print(texto)
        else:
            print_e("Damn! (x0001): Are you trying to scream in the wrong way!")
    elif linea.startswith('Wait'):
        tiempo_str = linea[len('Wait '):]
        try:
            segundos = int(tiempo_str)
        except ValueError:
            print_e("Damn! (x0002): You can't wait fractionally or decimal, little fox.")
            return
        time.sleep(segundos)
    elif linea.startswith('Hurray_End'):
        print_a("Hit! (a97000): The code is executed successfully!")

    else:
        print_e(f"Damn! (x0000): What the hell means '{linea}' ?")


# Ejemplo de uso
read_file('pruebas.furro')