import os
os.system('cls')


datos=[20,5,22,2,7,9,15,9,18,21]
print(datos)

for x in range(0,len(datos)):
    for y in range(0,(len(datos)-1)):
        if (datos[y]<datos[y+1]):
            temp=datos[y]
            datos[y]=datos[y+1]
            datos[y+1]=temp

print(datos)

for x in range(0,len(datos)):
    for y in range(0,(len(datos)-1)):
        if (datos[y]>datos[y+1]):
            temp=datos[y]
            datos[y]=datos[y+1]
            datos[y+1]=temp

print(datos)
