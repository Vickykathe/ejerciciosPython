import os
os.system('cls')

"""
Con el uso de condicionales anidados (sin operadores de union and) desarrolle
una propuesta de solucion funcional que a partir de tres numeros enteros diferentes
entre si, determine con un mensaje cual numero es mayor.:
"""

x = int(input("Digite primer numero: "))
y = int(input("Digite segundo numero: "))
z = int(input("Digite tercer numero: "))

print("CONDICIONAL ANIDADO SIN OPERADOR DE UNION AND")

if ( x > y ):
    if ( x > z ):
        print("Numero mayor: ",x)
    else:
        print("Numero mayor: ",z)
else: 
    if ( y > z ):
        print("Numero mayor: ",y)
    else:
        print("Numero mayor: ",z)

print("CON OPERADORES DE UNION AND")

if ( x > y and x > z):
    print("Numero mayor: ",x)
else:
    if ( y > x and y > z):
        print("Numero mayor: ",y)
    else: 
        print("Numero mayor: ",z)

print("OTRA FORMA DE CODIFICAR")

if ( x > y and x > z):
    print("Numero mayor: ",x)
elif ( y > x and y > z):
    print("Numero mayor: ",y)
else: 
    print("Numero mayor: ",z)

