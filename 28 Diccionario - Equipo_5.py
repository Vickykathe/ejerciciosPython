import os
from functions import opcion1,opcion2,opcion3,opcion4,opcion5
os.system('cls')

equipo = {
    9 : ['Muriel','Delantero',24,1.74],
    10 : ['James','MedioCampista',25,1.75],
    1 : ['Ospina','Arquero',27,1.80],
    15 : ['Uribe','MedioCampista',23,1.78],
    8 : ['Cuellar','MedioCampista',24,1.77]
}

# Definimos opc y encontrado en una sola linea separado por ,
opc = 0

while opc != 6:
    os.system('cls')
    print('Seleccione una opción: ')
    opc = int(input(
'''1. Presentar equipo
2. Agregar jugador
3. Eliminar jugador
4. Consultar por número de camisa
5. Consultar por nombre
6. Salir
-> '''))
    if opc == 1:
        opcion1(equipo)
    elif opc == 2:
        opcion2(equipo)
    elif opc == 3:
        opcion3(equipo)
    elif opc == 4:
        opcion4(equipo)
    elif opc == 5:
        opcion5(equipo)