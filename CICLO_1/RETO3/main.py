#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""



#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 



"""Fin espacio para programar funciones propias"""

def calculadora(bits1, bits2, OP):
    
    resultado = ""
    if OP=="AND":
        for i,j in zip(bits1, bits2):
            if int(i)==1 and int(j)==1:
                resultado +="1"
            else:
                resultado +="0"
    elif OP=="OR":
        for i,j in zip(bits1, bits2):
            if int(i)==1 or int(j)==1:
                resultado +="1"
            else:
                resultado +="0"
    elif OP=="XOR":
        for i,j in zip(bits1, bits2):
            if (int(i)==1 and int(j)==0) or (int(i)==0 and int(j)==1):
                resultado +="1"
            else:
                resultado +="0"
    
    #PROGRAMA ACÁ LA SOLUCIÓN

    return resultado

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
pruebas_codigo_estudiante(calculadora)