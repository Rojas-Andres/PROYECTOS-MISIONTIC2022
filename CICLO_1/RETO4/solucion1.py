#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
from pruebas import pruebas_codigo_estudiante
from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""


"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL




"""Fin espacio para programar funciones propias"""

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
 #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    #print(cola_general)
    cola_caja = []
    cola_info = []
    edad_minima_info = 9999
    edad_minima_retiro = 9999
    edad_minima_consignacion = 9999
    suma_consignaciones = 0
    suma_retiros = 0
    for i in cola_general:
        #print(i.fila_interes)
        if i.fila_interes == "caja":
            cola_caja.append(i.nombre)
            if i.cantidad_retirar>0 and i.transaccion=="retirar":
                if i.edad < edad_minima_retiro:
                    edad_minima_retiro=i.edad
                suma_retiros+=i.cantidad_retirar 
            elif i.cantidad_consignar>0 and i.transaccion=="consignar" :
                if i.edad < edad_minima_consignacion:
                    edad_minima_consignacion=i.edad
                suma_consignaciones+=i.cantidad_consignar
        elif i.fila_interes == "info":
            if i.edad < edad_minima_info:
                edad_minima_info = i.edad
            cola_info.append(i.nombre)
            #cola_info.pop(0)
        #suma_consignaciones+=i.cantidad_consignar
        #suma_retiros+=i.cantidad_retirar
    if edad_minima_info==9999:
        edad_minima_info=-1
    if edad_minima_retiro ==9999 : 
        edad_minima_retiro = -1
    if edad_minima_consignacion ==9999:
        edad_minima_consignacion =-1
    
    #suma_cola_caja = sum(c.edad for c in cola_general)
    #print(suma_cola_caja," es ")
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion


"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)