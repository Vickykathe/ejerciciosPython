# Comentarios de una sola linea
""" comentarios multi linea 
con triple comilla doble
al principio y final """ 
''' comentarios multi linea 
con triple comilla doble
al principio y final '''

# una funcion es un subprograma que realiza una accion especifica ... nombreFuncion(informacionRequerida) 
# print()  ... es la funcion que presenta en pantalla la informacion del parentesis (datos, variables, etc)  ... SALIDAS
# type() ... es la funcion que determina el tipo o natrualeza del dato del parentesis.

# Algunos Tipos de datos: TEXTO (String ... Str), NUMERICOS (int y float) , Booleanos (True , False) 

# El tupe() por si solo en ejecucion no presenta ninguna respuesta
type("Juan Perez")

print("Juan Perez")
print(type("Juan Perez"))

print(10)
print(type(10))

print(10000000)
print(type(10000000))

print(1.75)
print(type(1.75))

print(True)
print(type(False))

# Variables ... consideraciones a tener en cuenta en la definicion de nombres de variables

'''camel case
nombreEstudiante'''
#nombre_estudiante

nombre="Juan Perez"
print(nombre)
print(type(nombre))

edad=10
print(edad)
print(type(edad))

estatura=1.75
print(estatura)
print(type(estatura))

soltero=True
print(soltero)
print(type(soltero))


''' La funcion input() ... permite ingresar datos por teclado. Esta informacion es de tipo texto
 si quisieramos tratarla de tipo numerico (entero o decimal) ... se debe convertir. '''

''' La funcion int() convierte un dato tipo texto en uno numerico entero
    la funcion float() convierte un dato tipo texto en uno numerico decimal '''

nombre=input("Digite nombre del estudiante: ")
print(nombre)
print(type(nombre))

peso=input("Digite el peso del estudiante: ")
print(peso)
print(type(peso))
print(peso*2)

edadEstudiante=int(input("Digite edad del estudiante "+nombre+" : "))
print(edadEstudiante)
print(type(edadEstudiante))
print(edadEstudiante*2)

estatura=float(input("Digite estatura del estudiante: "))
print(estatura)
print(type(estatura))
print(estatura/2)