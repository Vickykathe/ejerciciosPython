import os
os.system('cls')
#LISTAS

#[ 10 , 1.45 , True , "maria" , "Gomez" , 20]  =  6 elementos ... indice 0 ... 5
#   0     1      2      3         4        5   

lista1 = [ 10 , 1.45 , True , "maria" , "Gomez" , "maria" , 20]
lista2 = [ 10, 15 ,2 , 5, 22, 20 , 5]

#print(type(lista1))

# listas son objetos  ... tienen acciones = metodos

#print(dir(lista1))

print(lista1)
lista1.append("jorge")
lista1.append(22)
print(lista1)

print(lista1[2])

lista1.insert(2,"Cra 18 #20-10")
print(lista1)

lista1[0]=30
print(lista1)

if (lista1[0]>0):
    lista1[0]=0
else:
    lista1[0]=False
print(lista1)

lista1.pop(7)
print(lista1)

lista1.remove("maria")
print(lista1)

print(lista1.index("maria"))

print(len(lista2))

lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)

print(lista2.count(5))

lista2.clear()
print(lista2)
