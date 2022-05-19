estudiantes = {}
D=0
for x in range(1,4):
    Nom=str(input("Ingrese el nombre del estudiante: "))
    Nota=float(input("Ingrese la nota del estudiante: "))
#estudiantes.update({x:{"Nombre": Nom, "Nota": Nota}})
    estudiantes[D] = {'nombre':Nom, 'nota':Nota}
    D+=1
for no,nt in estudiantes.items():
    if(nt['nota']<=59):
        print("estidiantes que suspenden")
        print(f"Nombre: {nt['nombre']} Nota = {nt['nota']}")
for no,nt in estudiantes.items():
    if(nt['nota']>=60):
        print("Estudiantes que pasan")
        print(f"Nombre: {nt['nombre']} Nota = {nt['nota']}")

nota = 0
for no,nt in estudiantes.items():
    nota += nt['nota']
print("promedio")
print("la nota promedio es: ",nota/len(estudiantes))

"""
print(estudiantes)
for i in estudiantes:
    if(i>=6):
        
        lista.append(i)
        print(lista)
    else:
        lista_2.append(i)
        print(lista_2)
"""