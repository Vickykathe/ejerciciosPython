import os
os.system('cls')

def opcion1():
    for i in equipo:
        print('[' , i , '] ' , equipo[i])
    input('<Enter> para continuar ')

def opcion2():
    busca=buscarCla()
    if (busca[0]):
        print('Jugador existente!!')
    else:
        lista=[]
        lista.append(      input("Nombre: "))
        lista.append(      input("Posicion de juego: "))
        lista.append(  int(input("Edad: ")))
        lista.append(float(input("Estatura: ")))
        equipo[busca[1]]=lista
    input('<Enter> para continuar ')

def opcion3():
    busca=buscarCla()
    if (busca[0]):
        del(equipo[busca[1]])
        print('Jugador eliminado!!')
    else:
        print('Jugador inexistente!!')
    input('<Enter> para continuar ')

def opcion4():
    busca=buscarCla()
    if (busca[0]):
        print(equipo.get(busca[1]))
    else:
        print('Jugador inexistente!!')
    input('<Enter> para continuar ')

def opcion5():
    jugador = input('Digite el nombre del jugador a buscar: ').lower()
    encontrado = 0
    for val in equipo:
        lista=equipo[val]
        if (lista[0].lower() == jugador):
            encontrado = 1
            print(f'El número del jugador {lista[0]} es: {val}')
    if encontrado == 0:
        print('Jugador no encontrado')
    input('<Enter> para continuar ')

def buscarCla():
    numero = int(input('Digite número del jugador: '))
    busca=[]
    if numero in equipo:
        busca=[True,numero]
    else:
        busca=[False,numero]
    return busca

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
        opcion1()
    elif opc == 2:
        opcion2()
    elif opc == 3:
        opcion3()
    elif opc == 4:
        opcion4()
    elif opc == 5:
        opcion5()