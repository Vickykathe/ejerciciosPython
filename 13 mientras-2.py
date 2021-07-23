import os
os.system('cls')

#CICLO MIENTRAS CONTROLADO POR PREGUNTA

continuar=True
cont=1
while (continuar):
    input("Nombre del empleado: ")
    seguir=input("continuar con otro empleado S/N ? ").upper()
    if (seguir!="S"):
        continuar=False
    
    if (cont==3):
        break
    
    cont +=1   
print("... salio del ciclo!!")
