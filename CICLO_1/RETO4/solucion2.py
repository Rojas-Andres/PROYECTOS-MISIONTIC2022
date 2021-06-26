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
    cola_retirar = []
    cola_consignar = []
    for i in cola_general:
        #print(i.fila_interes)
        if i.fila_interes == "caja":
            cola_caja.append(i.nombre)
            if i.cantidad_retirar>0 and i.transaccion=="retirar":
                cola_retirar.append(i)
            elif i.cantidad_consignar>0 and i.transaccion == "consignar":
                cola_consignar.append(i)
        elif i.fila_interes == "info":
            cola_info.append(i)
    #Sacamos el menor de info 
    if len(cola_info)==0:
        edad_minima_info = -1
    else:
        edad_minima_info = min(c.edad for c in cola_info)
    #Sacamos el menor de consignar
    if len(cola_consignar)==0:
        edad_minima_consignacion = -1
        suma_consignaciones = 0
    else:
        edad_minima_consignacion = min(c.edad for c in cola_consignar)
        suma_consignaciones = sum(c.cantidad_consignar for c in cola_consignar)

    #Sacamos el menor de retiro
    if len(cola_retirar)==0:
        edad_minima_retiro = -1
        suma_retiros = 0 
    else:
        edad_minima_retiro = min(c.edad for c in cola_retirar)
        suma_retiros = sum(c.cantidad_retirar for c in cola_retirar)

    #Hacemos la lista pero con los nombres con List Comprehension
    cola_info = [i.nombre for i in cola_info]

    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion


"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)