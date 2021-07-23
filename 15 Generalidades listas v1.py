import os
os.system('cls')

# listas ... estructuras de datos ... almacenar y manipular datos
# unidad basica minima de ED es la variable 

"""
[10 , "juan" , 1.75 , True]    = 4
  0     1       2      3       = 0 (4-1) = 0 - 3

[ 10 , 22 , 25, 30 , 18]    = 5 elementos con indices entre 0 y (5-1) .. 0 - 4
   0    1    2   3    4  ... indice = posicion que ocupa el elemento en la lista iniciando en cero (0)


[ "maria" , 22 , 1800000 , "mariabonita@gmail.com" , 3102220987 , "cra 20 #10-10" , 1.75] = 7 => 0 - 6
     0       1      2               3                     4             5             6

lista=[]
lista = [ "maria" , 22 , 1800000 , 3102220987 , "mariabonita@gmail.com" , 3102220987 , "cra 20 #10-10" , 1.75]

print(type(lista))
print(lista)
print(lista[1])
#print(dir(lista))

lista.append("Auxiliar")
print(lista[7])
print(lista)
print(len(lista))  
#= 8 = 0 ..7 
print(23 in lista)
lista.insert(2,"Auxiliar")
print(lista)

lista.pop()
print(lista)
lista.pop(1)
print(lista)

lista.insert(3,"Gomez")
print(lista)

print(lista1.index(5))
print(lista)
"""

lista1=[10,3,5,2,1]
print(lista1)
lista1.sort()
print(lista1)

lista1=[10,3,5,2,1,3]
print(lista1)
lista1.sort(reverse=True)
print(lista1)

print(lista1.count(3))

print(lista1.index(2))
print(lista1.index(3))

print(lista1.index(20))

#print(lista1.clear())
"""
lista1.remove(10)
print(lista1)

print(10 in lista1)

lista2=[]
for i in range(1,11):
    lista2.append("Hola")
print(lista2)
"""
"""
print("inicio del ciclo")

for i in range(0,len(lista)):
    print(lista[i])

print("... salio")
"""




