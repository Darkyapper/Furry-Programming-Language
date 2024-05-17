import time

def read_file(nombre_archivo):
    if not nombre_archivo.endswith('.furro'):
        raise ValueError("El archivo debe tener la extensión .furro")

    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        show_res(linea.strip())

def show_res(linea):
    if linea.startswith('Scream'):
        if '"' in linea:
            if linea.count('"') != 2:
                print("Damn! (x0001): Are you trying to scream in the wrong way!")
                return
            texto = linea.split('"')[1]
            print(texto)
        else:
            print("Damn! (x0001): Are you trying to scream in the wrong way!")
    elif linea.startswith('Wait'):
        segundos = int(linea[len('Wait '):])
        time.sleep(segundos)
    else:
        print(f"Damn! (x0000): What the hell means '{linea}' ?")


# Ejemplo de uso
read_file('pruebas.furro')