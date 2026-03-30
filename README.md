# Programación en Python: Estadísticas Básicas

Este proyecto ha sido desarrollado como parte de la **Actividad de evaluación 3** de la Unidad de Trabajo 4 (UT4): "Entrada y salida de información".

El programa implementa un sistema que accede (y crea en caso de no existir) a un fichero de texto (`edades.txt`) para calcular estadísticas básicas.

A partir de las edades leídas, se calcula la media, máximo, mínimo y total de edades del fichero.

## Características Principales

* **Archivo Predeterminado**: El programa crea un archivo de texto (`edades.txt`) con 6 edades predeterminadas para poder hacer pruebas.
* **Gestión de Archivos**: Uso de la sentencia `with open()` para asegurar la apertura y cierre automático de los archivos.
* **Calculo de Estadísticas**: Uso de cálculos básicos para obtener las estadísticas demandadas (media, máximo, mínimo y total de edades).

## Funcionamiento

El programa sigue el siguiente flujo:

1. **Inicialización**: Se comprueba la existencia del archivo `edades.txt` y lo crea si es necesario.
2. **Lectura de datos**: Accede al fichero en modo *read* (`r`) para leer todas las edades.
3. **Procesamiento y Cálculo**:
    * Procesa todas las entradas del fichero y las almacena en la lista `edades`.
    * Con todas las edades recopiladas, se realizan los cálculos demandados y se imprimen por pantalla con `print()`.

## Instrucciones de Uso

Para ejecutar este programa, es necesario descargar el [código fuente](https://git.paualdea.com/paualdea/Python-Estadisticas-Basicas/-/releases) y ejecutar el fichero `estadisticas_basicas.py`.

---
Este proyecto sirve como evidencia del aprendizaje sobre el manejo de archivos en Python, de la asignatura **Programación en Python**.