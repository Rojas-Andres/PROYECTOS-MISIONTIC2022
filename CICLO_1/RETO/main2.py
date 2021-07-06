cadena = "HHHPPPPEEEECCQQQXKYYYVEEE"
#cadena = "AAAAABBBCCAAAADCC"

dic2 = {}
lista = []
indice = 0
for i in range(len(cadena)):
    if indice == 0:
        dic2[cadena[i]]=1
        indice=1
    else:
        if cadena[i]!=cadena[i-1]:
            lista.append([cadena[i-1],dic2[cadena[i-1]]])
            dic2.pop(cadena[i-1])
            dic2[cadena[i]] = 1
        else:
            if cadena[i] in dic2:
                dic2[cadena[i]]+=1
            else:
                dic2[cadena[i]]=1

for i,j in dic2.items():
    lista.append([i,j])

for i in lista:
    print(i[0],end=" ")
print("")
for i in lista:
    print(i[1],end=" ")
print("")