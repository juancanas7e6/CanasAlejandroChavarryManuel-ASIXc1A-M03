"""
   Alejandro Cañas

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "CrazyWords.py" R2 - Paraules Boges
"""
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
