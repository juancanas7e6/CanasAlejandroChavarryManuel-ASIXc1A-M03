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
import openai

def get_data_from_keyboard():
    """Esta función recoge los datos del teclado y los retorna como una única cadena de caracteres"""
    return input('Introduce un texto: ')

def get_data_from_url(url="Introduce una URL"):
    """Esta función recoge datos desde una URL"""
    response = requests.get(url)
    data = response.text
    return data

def get_data_from_chatgpt(prompt="Introduce tu pregunta"):
    """Esta función recoge datos desde ChatGPT a través de una API"""  
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    data = response.choices[0].text.strip()
    return data

def choose_data_source():
    """Esta función permite al usuario elegir una fuente de datos"""
    print("Elige una opción:")
    print("1 - Recopilar datos desde el teclado")
    print("2 - Recopilar datos desde una URL")
    print("3 - Recopilar datos desde ChatGPT")
    choice = input("Opción elegida: ")
    if choice == "1":
        return get_data_from_keyboard()
    elif choice == "2":
        url = input("Introduce una URL: ")
        return get_data_from_url(url)
    elif choice == "3":
        prompt = input("Introduce tu pregunta: ")
        return get_data_from_chatgpt(prompt)
    else:
        print("Opción inválida")
