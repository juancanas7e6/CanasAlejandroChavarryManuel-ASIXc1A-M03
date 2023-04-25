import os
import logging
from datetime import datetime
from pathlib import Path
import random

def get_crazy_word(word):
    """Esta función recibe una palabra y la retorna desordenada excepto por la primera y la última letra"""
    if len(word) < 3:
        return word
    middle = list(word[1:-1])
    random.shuffle(middle)
    return word[0] + ''.join(middle) + word[-1]

def get_crazy_words(text):
    """Esta función recibe un texto y lo retorna con las palabras desordenadas"""
    words = text.split()
    crazy_words = [get_crazy_word(word) for word in words]
    return ' '.join(crazy_words)

def main():
    logging.basicConfig(filename=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'log', 'boges.log'),
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info('Iniciando el programa')

    entrada_dir = './entrada'
    sortida_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sortida')
    log_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'log')

    Path(sortida_dir).mkdir(parents=True, exist_ok=True)
    Path(log_dir).mkdir(parents=True, exist_ok=True)

    try:
        for file_name in os.listdir(entrada_dir):
            if file_name.endswith('.txt'):
                input_file_path = os.path.join(entrada_dir, file_name)
                output_file_path = os.path.join(sortida_dir, file_name[:-4] + 'Boges.txt')

                try:
                    with open(input_file_path, 'r', encoding='utf-8') as input_file:
                        content = input_file.read()
                        transformed_content = get_crazy_words(content)

                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(transformed_content)

                    logging.info(f'Archivo transformado: {file_name} -> {file_name[:-4]}Boges.txt')

                except Exception as e:
                    logging.error(f'Error al procesar el archivo {file_name}: {e}')

    except Exception as e:
        logging.error(f'Error al acceder al directorio de entrada: {e}')

    logging.info('Finalizando el programa')



main()
