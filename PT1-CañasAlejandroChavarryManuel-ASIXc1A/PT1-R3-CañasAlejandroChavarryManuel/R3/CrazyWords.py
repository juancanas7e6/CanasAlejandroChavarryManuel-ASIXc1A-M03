"""
   Alejandro Cañas y Manuel Chavarry

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "CrazyWords.py" R3 - Paraules Boges
"""
import random

def convertToCrazy(text):
    words = text.split()
    crazy_words = []

    for word in words:
        if len(word) <= 3:
            crazy_words.append(word)
        else:
            # Convertimos la palabra a una "palabra loca"
            crazy_word = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
            crazy_words.append(crazy_word)
    
    # Unimos las "palabras locas" en un solo string
    crazy_text = ' '.join(crazy_words)

    return crazy_text
