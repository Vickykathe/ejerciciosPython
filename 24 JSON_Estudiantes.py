import json
import os

dicc = {}

dicc['estudiantes'] = []

dicc['estudiantes'].append({
    'id': 1,
    'nota': 3.8})

dicc['estudiantes'].append({
    'id': 2,
    'nota': 4.5})

dicc['estudiantes'].append({
    'id': 3,
    'nota': 2.5})

def opcion1():
    print(dicc)
    input("\n<ENTER> para continuar ...")

def opcion2():
    with open('c:\Python\MINTIC 2022\datos.json', 'w') as file:
        json.dump(dicc, file, indent=4)
    input("\nArchivo generado, <ENTER> para continuar ...")

def opcion3():
    os.system('cls')
    with open('c:\Python\MINTIC 2022\datos.json') as file:
        datos = json.load(file)
    for estu in datos['estudiantes']:
        print('Id:', estu['id'])
        print('Nota: ', estu['nota'])
        print('--//--')

    input("\n<ENTER> para continuar ...")

continuar = "S"
while (continuar=="S"):
    os.system('cls')
    opcion=int(input("MENU PRINCIPAL JSON \n1. Diccionario \n2. Generar JSON \n3. Leer JSON \n4. Salir \n\nOpción?: "))

    if (opcion<1 or opcion>4):
        input("\nOpcion incorrecta <ENTER>!!")
    elif (opcion==1):
        opcion1()

    elif (opcion==2):
        opcion2()

    elif (opcion==3):
        opcion3()

    else: 
        continuar="N"

print("\nBye!")



