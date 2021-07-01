import csv
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    
def pruebas_codigo_estudiante(function_to_test):
    try:
        print("===TESTEADOR AUTOMÁTICO - RETO 5: Variante 2 - UdeA===\n")
        if not caso_aprobado(function_to_test):
            return False
            exit()
    
    except Exception as e:
        print(f"{bcolors.FAIL}¡ERROR!{bcolors.RESET}\nAl probar tu código nos genera un error que NO está relacionado con los resultados\nChequéalo tu mismo: {e}")
        return False
    
    print(f"{bcolors.OK}¡Tu código está funcionando correctamente! Procede a evaluarlo{bcolors.RESET}")
    return True
    
def caso_aprobado(function_to_test):
    #SALIDAS ESTUDIANTE
    date_lowest_estudiante, lowest_value_estudiante, date_highest_estudiante, highest_value_estudiante = function_to_test()
    
    #SALIDAS CORRECTAS
    date_lowest_correcta, lowest_value_correcta, date_highest_correcta, highest_value_correcta = ('2020-06-29', 193.550003, '2021-06-24', 267.850006)
    
    if not(isinstance(lowest_value_estudiante, float) and isinstance(highest_value_estudiante, float)):
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        {bcolors.FAIL}TIPOS DE DATOS INCORRECTOS:""")
        
        if not isinstance(lowest_value_estudiante, float):
            print(f"""\tlowest_value es de tipo {type(lowest_value_estudiante)} y DEBE SER tipo {type(12.0)}""")
        if not isinstance(highest_value_estudiante, float):
            print(f"""\thighest_value es de tipo {type(highest_value_estudiante)} y DEBE SER tipo {type(12.0)}""")
        print(f"""{bcolors.RESET}""")
        return False
    
    c = {
        False : {
            0 : 0, 
        },
        
        True: {
            0 : 0,
        }
    }
    
    
    #Los retornos suministrados por el estudiante son correctos?
    date_lowest_es_correcto = date_lowest_estudiante == date_lowest_correcta
    c[date_lowest_es_correcto][0]+=1
    c[date_lowest_es_correcto]['date_lowest'] = date_lowest_estudiante
    
    lowest_value_es_correcto = lowest_value_estudiante == lowest_value_correcta
    c[lowest_value_es_correcto][0]+=1
    c[lowest_value_es_correcto]['lowest_value'] = lowest_value_estudiante
    
    date_highest_es_correcto = date_highest_estudiante == date_highest_correcta
    c[date_highest_es_correcto][0]+=1
    c[date_highest_es_correcto]['date_highest'] = date_highest_estudiante
    
    highest_value_es_correcto = highest_value_estudiante == highest_value_correcta
    c[highest_value_es_correcto][0]+=1
    c[highest_value_es_correcto]['highest_value'] = highest_value_estudiante
    
    retornos_estudiante_son_correctos = date_lowest_es_correcto and lowest_value_es_correcto and date_highest_es_correcto and highest_value_es_correcto
    
    if not retornos_estudiante_son_correctos:
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        {bcolors.FAIL}TUS SALIDAS INCORRECTAS SON:""")
        incorrectos = c[False]
        for key in incorrectos:
            if key == 0:
                continue
            print(f"""
                {key} = {incorrectos[key]} es incorrecto 
            """)
        print(f"""
        {bcolors.RESET}
        """)
        return False
        
        
    #¿El archivo entregado es correcto?
    try:
        with open('analisis_archivo.csv') as file_estudiante:
            with open('concepto.csv') as file_correcto:
                concepto_reader = csv.reader(file_correcto, delimiter = '\t')
                analisis_estudiante_reader = csv.reader(file_estudiante, delimiter = '\t')
                for renglon_concepto, renglon_estudiante in zip(concepto_reader, analisis_estudiante_reader):
                    if renglon_concepto[0] != renglon_estudiante[0] or renglon_concepto[1] != renglon_estudiante[1] or renglon_concepto[2] != renglon_estudiante[2]:
                        archivo_estudiante_es_correcto = False
                        print(f"""{bcolors.WARNING}
                        ¡INCORRECTO!{bcolors.RESET}
                        
                        {bcolors.OK}SALIDA ESPERADA:
                        Fecha: {renglon_concepto[0]}
                        Mean-Min-Max: {renglon_concepto[1]}
                        Concepto: {renglon_concepto[2]}
                        {bcolors.RESET}
                        
                        {bcolors.FAIL}TU SALIDA: 
                        Fecha: {renglon_estudiante[0]}
                        Mean-Min-Max: {renglon_estudiante[1]}
                        Concepto: {renglon_estudiante[2]}
                        
                        Por favor revisa:
                            -¿Estás usando delimiter = '\\t'?
                            -¿Estás almacenando correctamente los conceptos: 'MUY BAJO', 'BAJO', 'MEDIO', 'ALTO', 'MUY ALTO'?
                            -¿Tu encabezado (Primera línea) es 'Fecha   Mean-Min-Max   Concepto'?
                        {bcolors.RESET}
                        """)
                        return False
    except IndexError:
        print(f"""{bcolors.WARNING}
                ¡INCORRECTO!{bcolors.RESET}
                {bcolors.FAIL}
                Por favor revisa:
                    -¿Estás usando delimiter = '\\t'?
                    -¿Estás almacenando correctamente los conceptos: 'MUY BAJO', 'BAJO', 'MEDIO', 'ALTO', 'MUY ALTO'?
                    -¿Tu encabezado (Primera línea) es 'Fecha   Mean-Min-Max   Concepto'?
                    -TU ARCHIVO NO ES EL CORRECTO
                {bcolors.RESET}
                """)
        return False
    #El estudiante logró pasar el calificador
    return True
