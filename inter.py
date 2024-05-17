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
                print("Damn!: La cadena debe estar encerrada entre comillas dobles.")
                return
            texto = linea.split('"')[1]
            print(texto)
        else:
            print("Error: La cadena debe estar encerrada entre comillas dobles.")
    elif linea.startswith('Wait'):
        segundos = int(linea[len('Wait '):])
        time.sleep(segundos)
    else:
        print(f"Comando no reconocido: {linea}")


# Ejemplo de uso
read_file('pruebas.furro')