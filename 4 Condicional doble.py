import os
os.system('cls')

"""
Calcular el valor a pagar por una entrada a un concierto teniendo en cuenta
que si la persona es mayor de edad la entrada tiene un incremento del 20%
y si la persona es menor de edad la entrada tiene un descuento del 10%. Se
debe presentar el valor a pagar por la entrada al concierto.
"""

# CONDICIONAL DOBLE
n=int(input("Digite cantidad de personas: "))

for i in range(1,n+1,1):
    print("Datos persona #",i)
    edad = int(input('Digite la edad de la persona: '))
    valor = float(input('Digite el valor de la boleta: $ '))
    if edad >= 18:
        vlrAdicional = valor * 0.2
    else:
        vlrAdicional = -valor * 0.1
    vlrPagar = valor + vlrAdicional
    print('Valor a pagar: $ ' + str(vlrPagar))
    input(" ... Digite una tecla para continuar!!")
    os.system('cls')

