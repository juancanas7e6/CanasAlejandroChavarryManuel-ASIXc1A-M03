"""
   Alejandro Cañas, Manuel Chavarry y Mauro Arena

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "Main.py" R2 - Paraules Boges
"""
from dataSource import getDataFromKeyboard
from crazyWords import get_crazy_words

# Obtenemos los datos del teclado
input_data = getDataFromKeyboard()

# Procesamos los datos para obtener las "paraules boges"
crazy_text = get_crazy_words(input_data)

# Mostramos el resultado por pantalla
print(crazy_text)
