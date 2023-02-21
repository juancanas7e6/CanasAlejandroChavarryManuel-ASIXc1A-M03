"""
   Alejandro Cañas

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "Main.py" R3 - Paraules Boges
"""
from crazyWords import convertToCrazy
from dataSource import getDataFromFile
import logging

# Configuración del logger
logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(message)s', filemode='a')

# Obtenemos los datos del archivo de entrada
try:
    data = getDataFromFile('paraules.txt')
except FileNotFoundError:
    logging.error('Archivo de entrada no encontrado')
    exit()

# Convertimos el texto de entrada a "palabras locas"
crazy_text = convertToCrazy(data)

# Escribimos las palabras locas en el archivo de salida
try:
    with open('boges.txt', 'w') as file:
        file.write(crazy_text)
except IOError:
    logging.error('Error al escribir en archivo de salida')

