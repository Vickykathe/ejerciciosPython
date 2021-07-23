import os
os.system('cls')

"""
De todos los empleadas de La clínica de la rodilla, en el mes de mayo se requiere
otorgar una bonificación a las empleadas madres de profesión ortopedistas y
fisioterapeutas correspondiente al 10% de su salario si tiene hasta 2 hijos y 
del 15% de su salario para quienes tengan más de 2 hijos. Las demás mujeres de
profesión contaduría y administración de empresas, entre otras, independientemente
de ser madres o no con hijos serán beneficiadas con un día de salario.
"""

profesion = input("Digite la profesion F -> Fisioterapia O -> Ortopedia X -> Otra: ")
salario = int (input("Digite el salario basico mensual: " ))
nroHijos = int(input("Digite numero de hijos: "))
pagar=0

if (( profesion == "O" or profesion == "F" ) and nroHijos > 0 ):
    if (nroHijos <= 2):
        pagar=salario*.1
    else:
        pagar=salario*.15
elif ( profesion == "X" ):
    pagar=salario/30

print ("Empleada con profesión: ",profesion," Recibe: ",pagar)

