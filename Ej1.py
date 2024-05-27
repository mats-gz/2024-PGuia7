from contextlib import contextmanager

@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = open(ruta_archivo, modo)
    try:
        yield archivo
    finally:
        archivo.close()

def leer_archivo(ruta_archivo):
    try:
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f'Error: El archivo {ruta_archivo} no fue encontrado.')

def escribir_archivo(ruta_archivo):
    with gestionar_archivo(ruta_archivo, 'w') as archivo:
        archivo.write('Hola, buenos dias.\n')
        archivo.write('¿Cómo te encuentras?\n')
        archivo.write('Hoy es un hermoso día para salir a pasear.\n')


escribir_archivo('texto-TP7.txt')
leer_archivo('texto-TP7.txt')