

"""


Gestionar la información relacionada con un indeterminado número de

empleados, permitiendo en cualquier momento:

• Registrar la información básica como: documento de identidad, nombre,

salario básico mensual y días trabajados de empleados nuevos.

• Visualizar la información básica de los empleados registrados.

• Consultar y actualizar la información básica de un empleado en particular.

• Consultar y eliminar toda la información relacionada con un empleado en

particular.

• Calcular nómina: calcular el valor neto a pagar a cada empleado a partir del

salario básico mensual y los días trabajados en el mes, teniendo en cuenta

además el descuento del 8% de seguridad social que se calcula sobre el valor

de los días trabajados; y el auxilio de transporte calculado en proporción a los

días trabajados. Como resultado de este proceso se debe presentar para

cada empleado la información básica y los valores calculados incluido el valor

neto a pagar.
  
""" 
import os

os.system('cls')


ident=[]

nomb=[]

salab=[]          

diastra=[]        

auxT=[]

total=[]




continuar="S"

while (continuar=="S"):

    os.system('cls')

    print(" MENU PRINCIPAL")

    print("1. Registrar Empleado")

    print("2. Listar Empleado")

    print("3. Actualizar Empleado")

    print("4. Calcular Nomina")

    print("5. Eliminar Empleado")

    print("6. Salir")

    opcion=int(input("Digite opción: "))
     

    if (opcion<1 or opcion>6):

        input("Opcion incorrecta, presione <ENTER>")

    elif (opcion==1):


        os.system('cls')

        seguir="S"

        while (seguir=="S"):
           

            ident.append(int(input("Digite su numero de identificación: ")))

            nomb.append(input("Digite su nombre completo: "))

            salab.append(int(input("Digite su salario basico mensual: ")))

            diastra.append(int(input("Digite la cantidad de dias trabajados: ")))

            seguir=input("Desea continuar con otro empleado S/N?: ").upper()


    elif (opcion==2):

        os.system('cls')

        for i in range(0, len(ident)):   

            print(f"Documento: {ident[i]}")

            print(f"Nombre: {nomb[i]}")

            print(f"Salario basico: {salab[i]}")

            print(f"Dias trabajados: {diastra[i]}")

        input("Digite <ENTER> para continuar")
        

    elif (opcion==3):

       print("Busqueda de informacion")

       os.system('cls')

       seguir="S"

       while (seguir=="S"):

            nombre=input("Nombre a consultar: ")

            existe=nombre in nomb

            if (existe):

                pos=nomb.index(nombre)

                print(f"Salario basicobasico: {salab[pos]} Dias Trab: {diastra[pos]}  ")
                name=input("Actualizar nombre :")
                nomb[pos]=name

            seguir=input("Desea continuar con otro empleado S/N?: ").upper()    
    

    elif (opcion==4):

       print("Calcular Nomina")

       os.system('cls')

       seguir="S"

       while (seguir=="S"):

            nombre=input("Nombre a consultar: ")

            existe=nombre in nomb

            if (existe):

                pos=nomb.index(nombre)
                valdia=(int(input("Ingrese el valor de dia trabajado: ")))
                auxT.append(int(input("Ingrese el valor  que la empresa aporta para el auxlio de transporte de (30 dias): ")))
                
                calnom = salab[pos]
                
                dias= diastra[pos]
                
                trabajo = valdia * dias

                desc=trabajo*0.08
                
                aux= auxT[pos]/ 30

                auxTotal= (aux) * dias

                total = (calnom + trabajo + auxTotal)- desc
                
                print("************************ESTA ES SU NOMINA ***********************************")
                
            
                print("El valor a pagar al empleado: " ,nombre)
                 
                print(f"Salario basicobasico: {salab[pos]} Dias Trab: {diastra[pos]}  ")
                
                print("Pago de dias trabajados:" , trabajo)

                print("Descuento por Seguridad: ", desc )
                
                print("Auxilio de transporte es de: ", auxTotal)

                print("Salario Total: ",total)

            seguir=input("Desea continuar con otro empleado S/N?: ").upper()    
                                    

    elif (opcion==5):

        print("Busqueda de informacion")

        os.system('cls')

        seguir="S"

        while (seguir=="S"):

            nombre=input("Nombre a consultar: ")

            existe=nombre in nomb

            if (existe):

                nomb.remove(nombre)

                print("El empleado: ",nombre," Fue eliminado satisfactoriamente" )

            seguir=input("Desea eliminar otro empleado empleado S/N?: ").upper()     

    else:

        continuar="N"


print("Vuelve Pronto!!")
 