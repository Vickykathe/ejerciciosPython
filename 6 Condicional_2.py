import os
os.system('cls')

"""
A partir de dos notas de un estudiante, se debe determinar con un mensaje su nota
promedio y el rendimiento al que corresponde: 
bajo = 0.0 a 2.9
basico = 3.0 a 3.9
alto =  4.0 a 4.5
superior = mayor 4.5 
Restriccion ... SIN OPERADORES and y or
"""

n1=float(input("Primer nota: "))
n2=float(input("Segunda nota: "))

prom=(n1+n2)/2

print("CONDICIONAL ANIDADO SIN AND")

if ( prom < 3.0 ):
    print("La nota promedio: ",prom, " con Rendimiento Bajo")
else:
    if ( prom < 4.0 ):
        print("La nota promedio: ",prom, " con Rendimiento Basico")
    else:
        if ( prom <= 4.5 ):
            print("La nota promedio: ",prom, " con Rendimiento Alto")
        else:
            print("La nota promedio: ",prom, " con Rendimiento Superior")

print("CONDICIONAL ANIDADO CON AND")

if ( prom >= 0.0 and prom < 3.0 ):
    print("La nota promedio: ",prom, " con Rendimiento Bajo")
else:
    if ( prom >= 3.0 and prom < 4.0 ):
        print("La nota promedio: ",prom, " con Rendimiento Basico")
    else:
        if ( prom >= 4.0 and prom <= 4.5 ):
            print("La nota promedio: ",prom, " con Rendimiento Alto")
        else:
            print("La nota promedio: ",prom, " con Rendimiento Superior")

print("OTRA FORMA DE CODIFICAR")

if ( prom >= 0.0 and prom < 3.0 ):
    print("La nota promedio: ",prom, " con Rendimiento Bajo")
elif ( prom >= 3.0 and prom < 4.0 ):
    print("La nota promedio: ",prom, " con Rendimiento Basico")
elif ( prom >= 4.0 and prom <= 4.5 ):
    print("La nota promedio: ",prom, " con Rendimiento Alto")
else:
    print("La nota promedio: ",prom, " con Rendimiento Superior")
