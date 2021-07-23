import os
os.system('cls')

# CICLO MIENTRAS CONTROLADO POR PREGUNTA
# vbles contadoras y acumuladoras

continuar="S"

while (continuar=="S"):
    input("Nombre del empleado: ")
    continuar=input("continuar con otro empleado S/N ? ").upper()  
print("... salio del ciclo!!")