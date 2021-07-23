import os

nombres=[]
salarios=[]
dias=[]
auxT=106454

continuar="S"
while (continuar=="S"):
    os.system('cls')
    print("MENU PRINCIPAL")
    print("1 Registrar")
    print("2 Listar")
    print("3 Consultar")
    print("4 Salir")
    opcion=int(input("Digite opcion: "))

    if (opcion<1 or opcion>4):
        input("Opcion inconsistente ... <ENTER>")
    elif (opcion==1):

        input("Incluir en listas")
        os.system('cls')
        seguir="S"
        while(seguir=="S"):
            nombres.append(input("Nombre: "))
            salarios.append(int(input("Salario: ")))
            dias.append(int(input("Dias trabajados: ")))
            seguir=input("Continuar con otro empleado S/N?: ").upper()

    elif (opcion==2):

        input("Visualizar contenido de listas")
        os.system('cls')
        for i in range(0,len(nombres)):
            print("Nombre: ",nombres[i])
            print("Salario: ",salarios[i])
            print("Dias Trab.: ",dias[i])
        input("Visualizar contenido de listas")

    elif (opcion==3):

        input("Busqueda de informacion")
        os.system('cls')
        seguir="S"
        while (seguir=="S"):
            nombre=input("Nombre a consultar: ")
            existe=nombre in nombres
            if (existe):
                pos=nombres.index(nombre)
                print(f"Salarios: {salarios[pos]} Dias Trab: {dias[pos]}  ")
            else:
                print("Empleado Inexistente!!")
                seguir="N"
        
        """         
        for i in range(0,len(nombres)):
            if (dias[i]>=0):
                dias[i] *= 10
        """
          

    else:
        continuar="N"

print("bye...")




