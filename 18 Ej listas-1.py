import os

descArt=[]
cantArt=[]
precArt=[]

#descArt[0]="Arroz kg"
#cantArt[0]=120
#precArt[0]=5500

continuar="S"
while (continuar=="S"):
    os.system('cls')
    print(" MENU PRINCIPAL")
    print("1. Agregar articulos")
    print("2. Listar inventario")
    print("3. Salir")
    opcion=int(input("Digite opción: "))

    if (opcion<1 or opcion>3):
        input("Opcion incorrecta, presione <ENTER>")
    elif (opcion==1):

        os.system('cls')
        seguir="S"
        while (seguir=="S"):
            descArt.append(input("Descripcion Articulo: "))
            cantArt.append(int(input("Cantidad Articulo: ")))
            precArt.append(int(input("Precio unitario: ")))
            seguir=input("Desea continuar S/N?: ").upper()

    elif (opcion==2):
        os.system('cls')
        #                       3-1 = 2 ..... 2
        for i in range(0, len(descArt)):
            print(f"Descripcion Articulo: {descArt[i]}")
            print("Cantidad Articulo: ",cantArt[i])
            print("Precio unitario: ",precArt[i])
        
        input("Digite <ENTER> para continuar")

    else:
        continuar="N"

print("bye!!")



  


    




        


