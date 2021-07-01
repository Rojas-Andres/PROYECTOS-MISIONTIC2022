from pruebas import pruebas_codigo_estudiante
import csv
import datetime
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)

def agno_mes_dia(fecha):
    fecha=fecha.split("-")
    return int(fecha[0]),int(fecha[1]),int(fecha[2])

"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    dic = {}
    i = 0
    titulos = ["Fecha","Mean-Min-Max","Concepto"]
    mean_min_max = []
    concepto = []
    with open('MSFT.csv') as archivo:
        datos = csv.reader(archivo,delimiter=",")
        #print(datos)
        
        for data in datos:
            if i == 0:
                for j in data:
                    dic[j]=[]
                i=1
            else:
                dic["Date"].append(data[0])
                dic["High"].append(float(data[2]))
                dic["Low"].append(float(data[3]))
                var = (float(data[2])+float(data[3]))/2
                mean_min_max.append(var)
                if var<207:
                    concepto.append("MUY BAJO")
                elif var>=207 and var<221:
                    concepto.append("BAJO")
                elif var>=221 and var<235:
                    concepto.append("MEDIO")
                elif var>=235 and var<249:
                    concepto.append("ALTO")
                elif var>=249:
                    concepto.append("MUY ALTO")
    
    #Saco los precios mas bajos y el valor
    lowest_value = min(c for c in dic["Low"])
    index = dic["Low"].index(lowest_value)
    date_lowest = dic["Date"][index]
    #Saco el precio mas alto y el valor
    highest_value = max(c for c in dic["High"])
    index = dic["High"].index(highest_value)
    date_highest = dic["Date"][index]

    with open('analisis_archivo.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f,delimiter="\t")
        writer.writerow(titulos)
        for i,j,k in zip(dic["Date"],mean_min_max,concepto):
            lista=[i,j,k]
            writer.writerow(lista)
    return str(date_lowest), lowest_value, str(date_highest), highest_value

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(solucion)