import os
os.system('cls')

for i in range(1,4,1): 
    genero=input("Digite su genero (F , M): ")
    profecion=input("Digite su profeción donde O: (ortopedista), F: (fisioterapeuta), D: (diferente): ")
    salario=int(input("Digite su salario: "))
    canHijos=int(input("Digete la cantidad de hijos que tiene: "))

    if (genero=="F" and (profecion=="O" or profecion=="F") and canHijos>0):
        if (canHijos<=2):
            bono=salario*0.10
        else:
            bono=salario*0.15
         
        print("Tiene un bono de: ",bono)
       
    else:
        print("No participa de la bonificacion!!")
    
    input("... presione una tecla")
    os.system('cls')


print("... salio")