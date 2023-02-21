"""
   Alejandro Cañas

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "R1.py" R1 - Paraules Boges
"""
# Función para desordenar las letras de una palabra
def desordenar_palabra(palabra):
    import random
    letras = list(palabra[1:-1])
    random.shuffle(letras)
    return palabra[0] + ''.join(letras) + palabra[-1]

# Función para procesar una frase completa
def procesar_frase(frase):
    palabras = frase.split()
    palabras_desordenadas = [desordenar_palabra(palabra) for palabra in palabras]
    return ' '.join(palabras_desordenadas)

# Función principal del programa
def main():
    frase = input("Introduce una frase: ")
    frase_desordenada = procesar_frase(frase)
    print(frase_desordenada)

# Ejecutar la función principal
if __name__ == '__main__':
    main()
