import os
os.system('cls')

# CONDICIONAL SIMPLE

grado=int(input("Grado del estudiante: "))
pagar=0

if (grado==3):
    valorTarifa=int(input("Valor de la tarifa: "))
    pagar=valorTarifa/4
    
print("El estudiante debe pagar: ",pagar)


