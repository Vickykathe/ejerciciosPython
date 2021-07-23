import os
os.system('cls')
"""
 CICLOS ANIDADOS (UNO DENTRO DE OTRO)
 * variable contadora ... es la q se incrementa con un valor fijo o constante
 por eje i y j son variables contadoras
 * variables sumadoras o acumuladoras .. se incrementan con valores variables
 por ej suma es una variable acumuladora
"""
n=int(input("Digite cantidad de estudiantes: "))
for i in range(1,(n+1),1):
    print("Datos estudiante #",i)
    suma=0

    for j in range(1,6,1):
        nota=float(input("Digite nota "+str(j)+" : "))
        suma += nota
        #suma = suma + nota
    print("Nota promedio: ",(suma/5))
    input(" ... Digite una tecla")
    os.system('cls')

