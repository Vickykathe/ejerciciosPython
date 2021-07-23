import os

os.system('cls')

equipo = {
    9 : 'Muriel',
    10 : 'James',
    1 : 'Ospina',
    15 : 'Uribe',
    8 : 'Cuellar'
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
        for i in equipo:
            print('[' , i , '] ' , equipo[i])
        input('<Enter> para continuar ')

    elif opc == 2:
        numero = int(input('Digite el numero del jugador: '))
        if numero in equipo.keys():
            print('Jugador existente')
        else:
            nombre = input('Digite el nombre del jugador: ')
            equipo[numero] = nombre
        input('<Enter> para continuar ')

    elif opc == 3:
        eliminar = int(input('Digite número de jugador que quiere eliminar: '))
        if eliminar in equipo.keys():
            del(equipo[eliminar])
            print('Jugador eliminado')
        else:
            print('Jugador inexistente!!')
        input('<Enter> para continuar ')

    elif opc == 4:
        buscar = int(input('Digite el número de camisa del jugador a buscar: '))
        if buscar in equipo:
            print(equipo.get(buscar))
        else:
            print('Jugador inexistente!!')
        input('<Enter> para continuar ')

    elif opc == 5:
        jugador = input('Digite el nombre del jugador a buscar: ').lower()
        encontrado = 0
        for val in equipo:
            if equipo.get(val).lower() == jugador:
                encontrado = 1
                print(f'El número del jugador {equipo.get(val)} es: {val}')
        if encontrado == 0:
            print('Jugador no encontrado')
        input('<Enter> para continuar ')
