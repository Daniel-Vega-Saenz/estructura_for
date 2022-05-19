Diccionario={"Mikel":3, "Ane":8, "Amaia":12, "Unai":5, "Jon":8, "Ainhoa":7, "Maite":5}
lista=[]
for i in Diccionario:
    M=(Diccionario[i])
    lista.append(M)
    Coleccion=set(lista)
    T=list(Coleccion)
print(T)