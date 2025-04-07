# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

Desarrolla una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya:

- **Balance Final:**  
  Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

- **Transacción de Mayor Monto:**  
  Identificar el ID y el monto de la transacción con el valor más alto.

- **Conteo de Transacciones:**  
  Número total de transacciones para cada tipo ("Crédito" y "Débito").

## Instrucciones

1. Clona el repositorio `git clone https://github.com/csantv/interbank-academy-25.git`

2. Descargar python
   En este proyecto se utilizó la herramienta [uv](https://docs.astral.sh/uv/) para el manejo de versiones locales
   Se utilizó python 3.13, no se utilizó dependencias externas

   Seguir las intrucciones de uv https://docs.astral.sh/uv/getting-started/installation/

3. Ejecutar el archivo main.py
   Usando uv:  `uv run main.py`

## Enfoque y Solución

Es un proyecto sencillo por lo que un archivo main.py es suficiente
Se abre primero el archivo, luego se procesan las líneas y finalmente se imprime el reporte final

## Estructura del proyecto

- main.py (archivo principal)
- data.csv (archivo conteniendo transacciones)