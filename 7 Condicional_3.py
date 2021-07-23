import os
os.system('cls')

"""
En un parque de diversiones al que solo tienen acceso niños y niñas con estatura que
no sobrepase 1.2 metros, se requiere presentar un mensaje en el que se indique que las
niñas con edad a partir de 10 años entran gratis, y para los demas niños y niñas 
calcular el valor a pagar por la entrada teniendo en cuenta que pagan la mitad de la 
tarifa.
""" 
estatura=float(input("Digite la estatura del niño o niña: "))

print ("CONDICONAL ANIDADO SIN AND")
if (estatura <= 1.2):
    tarifa=int(input("Digite el valor de la tarifa: "))
    edad=int(input("Digite edad del niño o niña: "))
    genero=input("Digite genero (M/F): ")
    if ( edad >= 10 ):
        if ( genero=="F" ):
            print("Las niñas entran gratis!! ")
        else:
            print("Valor a pagar por el niño o niña es: ",(tarifa/2))
    else:
        print("Valor a pagar por el niño o niña es: ",(tarifa/2))
else:
    print("Por la estatura no tiene acceso!!")

print ("CONDICONAL ANIDADO CON AND")

if (estatura <= 1.2):
    tarifa=int(input("Digite el valor de la tarifa: "))
    edad=int(input("Digite edad del niño o niña: "))
    genero=input("Digite genero (M/F): ")
    if ( edad >= 10 and genero=="F" ):
        print("Las niñas entran gratis!! ")
    else:
        print("Valor a pagar por el niño: ",(tarifa/2))
else:
    print("Por la estatura no tiene acceso!!")
    