import os
os.system('cls')


       

nombres = ["juan","silvia","pedro", "paola", "carlos", "maria" ,"daniela" ,"luz"]
edad = [20,17,32,21,12,8,15,25,17,31]

for x in range (0,len(nombres)):
    for y in range (0,(len(edad)-1)):
        if(edad[y]>edad[y+1]):
            temp=edad[y] 
            edad[y]=edad[y+1]
            edad[y+1]=temp
            
for tupla in zip(nombres, edad): #obtenemos la tupla en cada iteración
	print(tupla[0], tupla[1])

for valor_a, valor_b in zip(nombres, edad): #obtenemos los valores en cada iteración
	print(valor_a, valor_b)