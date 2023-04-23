import os
import random
import glob
import chardet
import logging

log_directory =  "CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_filename = os.path.join(log_directory, 'archivo_procesamiento.log')
logging.basicConfig(filename=log_filename, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def desordenar_palabra(palabra):
    if len(palabra) <= 3:
        return palabra
    
    medio = list(palabra[1:-1])
    random.shuffle(medio)
    palabra_desordenada = palabra[0] + ''.join(medio) + palabra[-1]
    
    return palabra_desordenada

def desordenar_frase(frase):
    palabras = frase.split()
    palabras_desordenadas = [desordenar_palabra(p) for p in palabras]
    frase_desordenada = ' '.join(palabras_desordenadas)
    
    return frase_desordenada

def procesar_archivos_txt(directorio, directorio_salida):
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    for archivo in glob.glob(os.path.join(directorio, '*.txt')):
        with open(archivo, 'rb') as f:
            contenido_binario = f.read()
        
        resultado_chardet = chardet.detect(contenido_binario)
        codificacion = resultado_chardet['encoding']

        try:
            with open(archivo, 'r', encoding=codificacion) as f:
                contenido = f.read()
        except Exception as e:
            print(f"Error al leer el archivo {archivo}: {e}")
            continue

        contenido_desordenado = desordenar_frase(contenido)

        nombre_archivo, extension = os.path.splitext(os.path.basename(archivo))
        nuevo_nombre = nombre_archivo + 'Boges' + extension
        ruta_salida = os.path.join(directorio_salida, nuevo_nombre)

        with open(ruta_salida, 'w', encoding='utf-8') as f:
            f.write(contenido_desordenado)

directorio = "CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/entrada"
directorio_salida = "CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/entrada"
procesar_archivos_txt(directorio, directorio_salida)
