"""
   Alejandro Cañas y Manuel Chavarry

   DATE:
   15/02/2023

   ASIXc M03 UF2 A2
   PT1- Modular Programming

   DESCRIPTION:
   Proyect "DataSource.py" R3 - Paraules Boges
"""
def getDataFromFile(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data
