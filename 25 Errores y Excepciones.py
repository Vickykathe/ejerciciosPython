import os
os.system('cls')

#ZeroDivisionError:
#a = 5; b = 0
#c = a/b

#TypeError
#d = 2 + "Hola"

#KeyError
#equipo={1:"Ospina",7:"Diaz",11:"Cuadrado"}
#print(equipo[10])     

#ValueError ... ingresar un tipo de dato inconsistente
#edad=int(input("digite edad: "))
#print(edad)

"""
a = 5; b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("No se ha podido realizar la división")
    input("... presione <ENTER> para continuar")
"""

"""
equipo={1:"Ospina",7:"Diaz",11:"Cuadrado"}
clave=int(input("Jugador a buscar: "))
try:
    print(equipo[clave])     
except KeyError:
    print("No se ha encontrado el jugador")
    input("... presione <ENTER> para continuar")
"""

"""
a = 5; b = 0
try:
    c = a/b       
    d = 2 + "Hola" 
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except TypeError:
    print("Problema de tipos de datos!!")
"""

"""
a = 5; b = 0
try:
    c = a/b       
    d = 2 + "Hola" 
except (ZeroDivisionError, TypeError):
    print("Excepcion ZeroDivisionError/TypeError")
"""

"""
a = 5; b = 0
try:
    #c = a/b      
    d = 2 + "Hola" 
except Exception:
    print("Ha habido una excepción")
"""

"""
try:
    d = 2 + "Hola" 
except Exception as ex:
    print("Ha habido una excepción", type(ex))
    print("Ha habido una excepción", ex)
"""

"""
a = 5; b = 0
try:
    c=a/b
    print(c)
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en else, no ha ocurrido ninguna excepción")
"""

"""
a = 5; b = 0
try:
    c=a/b
    print(c)
except:
    print("Entra en except, ha ocurrido una excepción")
else:
    print("Entra en el else, no ha ocurrido ninguna excepción")
    input("... presione <ENTER> para continuar") 
finally:
    print("Entra en finally, con o sin excepción")
    input("... presione <ENTER> para continuar")
"""