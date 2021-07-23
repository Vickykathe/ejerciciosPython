import os

asignaturas=("Matematicas","Español","Ciencias","Ingles")
dimensiones=("Hacer","Saber","Ser","Acumulativa","Auto Evaluacion")
porcDim=(0.3,0.2,0.2,0.2,0.1)
notas=[]

continuar=True
while (continuar):
    os.system('cls')
    print("MENU PRINCIPAL")
    for i in range(0,len(asignaturas)):
        print(str(i+1)+" "+asignaturas[i])
    print (str(i+2)+" Salir" )
    opcion=int(input(" ... Digite opcion: "))

    if (opcion<1 or opcion>(i+2)):
        input("... opcion incorrecta, presione <ENTER>")
    elif (opcion>=1 and opcion<(i+2)):
        os.system('cls')
        print("digitar nnotas")
        notas=[]
        for i in range(0,len(dimensiones)):
            notas.append(float(input(f" {dimensiones[i]} : ")))
                 
        print(notas)
        input("... presione <ENTER>")
    
    else:
        continuar=False

print("Bye!!")
