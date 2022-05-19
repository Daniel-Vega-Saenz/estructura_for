lista=[12,23,5,12,92,5,12, 5, 29, 92, 64,23]
numeros={}
for i in lista:
    a=lista.count(i)#cuanta cada dato 
    numeros.update({i:a})
print(numeros)