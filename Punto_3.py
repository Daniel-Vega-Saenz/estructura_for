user= { 
    "iperurena": { 
    "nombre": "Iñaki", 
    "apellido": "Perurena", 
    "password": "123123" 
    }, 
    "fmuguruza": { 
    "nombre": "Fermín", 
    "apellido": "Muguruza", 
    "password": "654321" 
    }, 
    "aolaizola": { 
    "nombre": "Aimar", 
    "apellido": "Olaizola", 
    "password": "123456" 
    } 
    }
c=0

for I in user: 
    t=user[I]

M=("iperurena" in user) 
L=("password" in t) 

while True:
    if(c==3):
        print("Demasiados intentos.")
        break
    Usuario=str(input("Digite su usuario: "))
    Contra=int(input("Digite su contraseña: "))
    if((Usuario=="iperurena" and M==True) and (Contra==123123 and L==True)):
        pri= user["iperurena"]
        pri.pop("password")
        print(pri)
        break
    elif((Usuario=="fmuguruza" and M==True) and (Contra==654321 and L==True)):
        seg= user["fmuguruza"]
        seg.pop("password")
        print(seg)
        break
    elif((Usuario=="aolaizola" and M==True) and (Contra==123456 and L==True)):
        tre= user["aolaizola"]
        tre.pop("password")
        print(tre)
        break
    else:
        c+=1
        print("Error al ingresar. Vuelva a intentarlo.")