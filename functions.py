
def opcion1(equipo):
    for i in equipo:
        print('[' , i , '] ' , equipo[i])
    input('<Enter> para continuar ')

def opcion2(equipo):
    busca=buscarCla(equipo)
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

def opcion3(equipo):
    busca=buscarCla(equipo)
    if (busca[0]):
        del(equipo[busca[1]])
        print('Jugador eliminado!!')
    else:
        print('Jugador inexistente!!')
    input('<Enter> para continuar ')

def opcion4(equipo):
    busca=buscarCla(equipo)
    if (busca[0]):
        print(equipo.get(busca[1]))
    else:
        print('Jugador inexistente!!')
    input('<Enter> para continuar ')

def opcion5(equipo):
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

def buscarCla(equipo):
    numero = int(input('Digite número del jugador: '))
    busca=[]
    if numero in equipo:
        busca=[True,numero]
    else:
        busca=[False,numero]
    return busca