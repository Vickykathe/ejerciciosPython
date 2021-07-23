import os
os.system('cls')
# DICCIONARIOS
# ELEMENTO = clave : valor ... keys : values 

datos={"nombre" : "juan",
       "apellido" : "gomez",
       "edad" : 22,
       "estatura" : 1.75,
       "soltero" : True}

# VISUALIZAR LOS ELEMENTOS DEL DICCIONARIO
print(datos)

# VISUALIZAR EL VALOR DE UNA CLAVE, EN ESTE CASO LA CLAVE EDAD
print(datos["edad"])
# GENERA ERROR PUESTO QUE LA CLAVE JUAN NO EXISTE
print(datos["juan"])  

#ACTUALIZAR O MODIFICAR EL VALOR DE UNA CLAVE EXISTENTE
datos["edad"]=20

#AGREGAR ELEMENTOS CON CLAVE INEXISTENTE ASIGNANDO UN VALOR A LA CLAVE
datos["contacto"]=3101234560

#ELIMINAR UN ELEMENTO DE UNA CLAVE EXISTENTE
# SI LA CLAVE NO EXISTIERA ARROJARIA UN ERROR (EXCEPCION) QUE INTERRUMPIRIA LA EJECUCION DEL PROG 
del(datos["apellido"])
print(datos)

#PRESENTAR EL VALOR DE UNA CLVAE Y UN POSIBLE MENSAJE DE CLAVE INEXISTENTE EVITANDO
#UN ERROR DE EXCEPCION QUE INTERRUMPE LA EJECUCION DEL PROGRAMA
print(datos.get("apellidos","Clave es inexistente!!"))

# SENTENCIA DE BUSQUEDA DE UNA CLAVE EN UN DICIONARIO .. CON RESPUESTA TRUE O FALSE
print("edad" in datos)

# PREGUNTAR SI UN DATO EXISTE EN LOS VALORES DEL DICCIONARIO
if "juanes" in datos.values():
    print("Juan existe")
else:
    print("Juanes no existe")

# PRESENTA LOS VALORES DEL DICC
print(datos.values())
# PRESENTA LAS CLAVES DEL DICC
print(datos.keys())

#  PRESENTA EL TAMAÑO O NUMERO DE ELEMENTOS DEL DICCIONARIO
print(len(datos))

#PERMITE ELIMINAR LA TOTALIDAD DE ELEMENTOS DEL DICCIONARIO DEJANDOLO VACIO
datos.clear()
print(datos)

# ALMACENAR EN VARIABLE EL VALOR DE UNA CLAVE
nombre=datos["nombre"]
print(nombre)

# RECORRER EL DICC E IR TOMANDO EN X CADA CLAVE E IRLA PRESENTANDO 
for x in datos:
    print(x)
print("")

# RECORRER EL DICC E IR TOMANDO EN X CADA VALOR DEL DICC E IRLO PRESENTANDO
for x in datos.values():
    print(x)
print("")

# RECORRER EL DICC E IR TOMANDO EN X CADA CLAVE DEL DICC Y PRESENTAR LA CLAVE Y A PARTIR DE LA 
# CLAVE PRESENTAR SU RESPECTIVO VALOR 
for x in datos:
    print(x," : ",datos[x])

print("")
for x in datos:
    y=datos[x]
    print(x," : ",y)
