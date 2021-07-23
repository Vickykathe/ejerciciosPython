import os
os.system('cls')

tupla1=(10,True,"silvia",1.55)
#       0   1      2      3 
 
print(tupla1)
print(type(tupla1))

print(tupla1[2])
print(20 in tupla1)

print(tupla1.index(10))

print(tupla1.count("silvia"))

print(len(tupla1))

lista1=list(tupla1)
print(tupla1)
print(lista1)
lista1.pop()

tupla2=tuple(lista1)
print(lista1)
print(tupla2)