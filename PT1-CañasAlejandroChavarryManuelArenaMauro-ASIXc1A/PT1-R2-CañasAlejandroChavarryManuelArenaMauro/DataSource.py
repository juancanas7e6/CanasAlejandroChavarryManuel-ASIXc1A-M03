"""
   Alejandro Cañas, Manuel Chavarry y Mauro Arena

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "DataSource.py" R2 - Paraules Boges
"""
import requests

def getDataFromKeyboard():
    """Esta función recoge los datos del teclado y los retorna como una única cadena de caracteres"""
    return input('Introduce un texto: ')

def getDataFromServer(URL):
    """Esta función obtiene los datos desde una URL y los retorna como una única cadena de caracteres"""
    response = requests.get(URL)
    return response.text

"Se debe tener en cuenta que para la implementación del método getDataFromChatGPT es necesario utilizar la API de GPT-3 de OpenAI, la cual requiere una clave de API válida y un proceso de autenticación previo."
def getDataFromChatGPT(question):
    """Esta función obtiene los datos desde OpenAI's GPT-3 API mediante la pregunta y los retorna como una única cadena de caracteres"""
    # Aquí iría el código para interactuar con la API de GPT-3
    # y obtener los datos en función de la pregunta
    return "Respuesta obtenida desde GPT-3"

def getDataFromFile(fileName):
    """Esta función recoge los datos desde un archivo y los retorna como una única cadena de caracteres"""
    with open(fileName, 'r') as f:
        data = f.read()
    return data
