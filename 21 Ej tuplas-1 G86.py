import os


materias=("Matematicas","Español","Ciencias","Ingles","Sociales")
dimensiones=("Hacer","Saber","Ser","Acumulativa","Auto Evaluacion")
porcDim=(0.3,0.2,0.2,0.2,0.1)
promedio=[]

for i in range(0,len(materias)):
    promedio.append(0)

continuar="S"
while (continuar=="S"):
    os.system('cls')
    print("MENU PRINCIPAL")
    for i in range(0,len(materias)):
        print((i+1)," ",materias[i])
    print((i+2),"  Salir")
    opcion = int(input("... Digite opcion: "))

    if (opcion<1 or opcion>(i+2)):
        input("... opcion incorrecta, presiones<ENTER>!! ")
    elif (opcion>=1 and opcion<(i+2)):
        os.system('cls')
        print("... Digitacion de notas!! ")
        notas=[]
        suma=0
        for j in range(0,len(dimensiones)):
            notas.append(float(input(f"{dimensiones[j]} : ")))
            suma += notas[j]*porcDim[j]
                      
        input(f"... Nota definitiva {materias[opcion-1]} : {suma} ... <ENTER> ")
        promedio[opcion-1]=suma


    #if (opcion==(i+2)):
    else:
        continuar="N"
        print(promedio)
        suma=0
        for i in range(0,len(promedio)):
            suma += promedio[i]
        print("Nota promedio ponderado: ",(suma/len(promedio)))

print("Bye!!")
