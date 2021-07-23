import os
os.system('cls')

def promedio():
    prom=(nota1+nota2)/2
    print("Promedio : ",prom)
    return prom

def resul(definitiva):
    print("El resultado de promedio es: ",definitiva)

"""
def calcularNeto(v1,v2,v3):
    print ("Valor neto es: ",(v1+v2+v3))
"""

nota1=float(input("Primer nota: "))
nota2=float(input("Segunda nota: "))
resultado=promedio()
resul(resultado)

"""
valor1=f1()
valor2=f2()
valor3=f3()
calcularNeto(valor1,valor2,valor3)
"""