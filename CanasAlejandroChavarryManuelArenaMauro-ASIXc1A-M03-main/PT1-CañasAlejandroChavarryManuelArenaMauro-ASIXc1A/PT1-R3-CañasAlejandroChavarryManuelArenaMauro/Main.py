"""
    Manuel Chavarry y Mauro Arena

   DATE:
   25/04/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "Main.py" R3 - Paraules Boges
"""
import os
import logging
from datetime import datetime
from pathlib import Path
from Crazywords import get_crazy_words


def main():
    logging.basicConfig(filename='CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/log/boges.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')                                         #configuracio de logs

    logging.info('Iniciando el programa')

    entrada_dir = 'CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/entrada'
    sortida_dir = 'CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/sortida'
    log_dir = 'CanasAlejandroChavarryManuelArenaMauro-ASIXc1A-M03-main/PT1-CañasAlejandroChavarryManuelArenaMauro-ASIXc1A/PT1-R3-CañasAlejandroChavarryManuelArenaMauro/log'

    Path(sortida_dir).mkdir(parents=True, exist_ok=True)
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    try:                                                     #os para acceder a los archivos en el directorio de entrada.
        for file_name in os.listdir(entrada_dir):
            if file_name.endswith('.txt'):
                input_file_path = os.path.join(entrada_dir, file_name)                                  # busca archivos con extensión .txt
                output_file_path = os.path.join(sortida_dir, file_name[:-4] + 'Boges.txt')

                try:
                    with open(input_file_path, 'r', encoding='utf-8') as input_file:
                        content = input_file.read()
                        transformed_content = get_crazy_words(content)                                  #transformacio

                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(transformed_content)

                    logging.info(f'Archivo transformado: {file_name} -> {file_name[:-4]}Boges.txt')         #especificaciones de log

                except Exception as e:
                    logging.error(f'Error al procesar el archivo {file_name}: {e}')

    except Exception as e:
        logging.error(f'Error al acceder al directorio de entrada: {e}')

    logging.info('Finalizando el programa')


if __name__ == '__main__':
    main()                          #ejecuta el archivo
