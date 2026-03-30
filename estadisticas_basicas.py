# Actividad 3 - Estadísticas básicas desde un fichero
import os

archivo = "edades.txt"
default_edades = [23, 45, 12, 87, 50, 66]

# Comprobamos que el fichero exista, sino, lo creamos
if not os.path.exists(archivo):
    with open(archivo, "w") as fichero:
        # Creamos el fichero
        pass

        # Le añadimos 6 edades de prueba
        for edad in default_edades:
            fichero.write(f"{edad}\n")

# Abrimos el fichero en modo lectura (r)
with open(archivo, "r") as fichero:
    # Creamos una lista para almacenar todas las edades del fichero
    edades = []
    media = 0

    # Las añadimos leyendo el fichero y convertiendolas a entero (int)
    for linea in fichero:
        # Añadimos el valor de la linea a la lista
        edades.append(int(linea))
        # Sumamos el valor total de la media el último valor de la lista
        media += edades[-1]

    # Cálculos finales
    media /= len(edades)
    maximo = max(edades)
    minimo = min(edades)
    entradas = len(edades)

    # Imprimimos los resultados por pantalla
    print(f"\t\t\n.:ESTADÍSTICAS BÁSICAS:.\n\nEdad media --> {media} años\nMáxima edad --> {maximo} años\nMínima edad --> {minimo} años\nTotal de edades --> {entradas} edades")