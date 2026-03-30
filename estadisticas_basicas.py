# Actividad 3 - Estadísticas básicas desde un fichero
import os

archivo = "edades.txt"
edades = [23, 45, 12, 87, 50, 66]

# Comprobamos que el fichero exista, sino, lo creamos
if not os.path.exists(archivo):
    with open(archivo, "w") as fichero:
        # Creamos el fichero
        pass

        # Le añadimos 6 edades de prueba
        for edad in edades:
            fichero.write(f"{edad}\n")

# Abrimos el fichero en modo lectura (r)
with open(archivo, "r") as fichero:
    for edad in fichero:
        # Leemos cada linea, borrando el salto de linea del documento
        print(edad.strip())