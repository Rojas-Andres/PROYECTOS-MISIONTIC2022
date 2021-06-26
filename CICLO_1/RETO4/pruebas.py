from cliente import cliente
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
def pruebas_codigo_estudiante(function_to_test):
    try:
        print("===TESTEADOR AUTOMÁTICO - RETO 4 - UdeA===\n")

        if not caso1_aprobado(function_to_test):
            return False
            exit()
      
        elif not caso2_aprobado(function_to_test):
            return False
            exit()

        elif not caso3_aprobado(function_to_test):
            return False
            exit()
       
        elif not caso4_aprobado(function_to_test):
            return False
            exit()
        elif not caso5_aprobado(function_to_test):
            return False
            exit()
    
    except Exception as e:
        print(f"{bcolors.FAIL}¡ERROR!{bcolors.RESET}\nAl probar tu código nos genera un error que NO está relacionado con los resultados\nChequéalo tu mismo: {e}")
        return False
    
    print(f"{bcolors.OK}¡Tu código está funcionando correctamente! Procede a evaluarlo{bcolors.RESET}")
    return True

def caso1_aprobado(function_to_test):
    #ENTRADAS
    cola_general = [
    cliente("Matt",21,235000,"caja","retirar",100000,0),
    cliente("Dan",32,658000,"caja","retirar",98000,0),
    cliente("Diana",29,87000,"info","ninguna",0,0)
    ]
    
    #SALIDAS CORRECTAS
    cola_caja_correcta = ['Matt', 'Dan']
    cola_info_correcta = ['Diana']
    suma_retiros_correcta = 198000
    suma_consignaciones_correcta = 0
    edad_minima_retiro_correcta = 21
    edad_minima_info_correcta = 29
    edad_minima_consignacion_correcta  = -1 
    
    #SALIDAS ESTUDIANTE
    cola_caja_estudiante = function_to_test(cola_general)[0]
    cola_info_estudiante = function_to_test(cola_general)[1]
    suma_retiros_estudiante = function_to_test(cola_general)[2]
    suma_consignaciones_estudiante = function_to_test(cola_general)[3]
    edad_minima_retiro_estudiante = function_to_test(cola_general)[4]
    edad_minima_info_estudiante = function_to_test(cola_general)[5]
    edad_minima_consignacion_estudiante  = function_to_test(cola_general)[6]
    
    if not (cola_caja_correcta == cola_caja_estudiante and cola_info_correcta == cola_info_estudiante and suma_retiros_correcta == suma_retiros_estudiante and suma_consignaciones_correcta == suma_consignaciones_estudiante and edad_minima_retiro_correcta == edad_minima_retiro_estudiante and edad_minima_info_correcta == edad_minima_info_estudiante and edad_minima_consignacion_correcta == edad_minima_consignacion_estudiante):
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        ENTRADA: 
        cola_general = {cola_general}
        {bcolors.OK}SALIDA ESPERADA:
        cola_caja = {cola_caja_correcta}
        cola_info = {cola_info_correcta}
        suma_retiros = {suma_retiros_correcta}
        suma_consignaciones = {suma_consignaciones_correcta}
        edad_minima_retiro = {edad_minima_retiro_correcta}
        edad_minima_info = {edad_minima_info_correcta}
        edad_minima_consignacion  = {edad_minima_consignacion_correcta}{bcolors.RESET}
        {bcolors.FAIL}TU SALIDA: 
        cola_caja = {cola_caja_estudiante}
        cola_info = {cola_info_estudiante}
        suma_retiros = {suma_retiros_estudiante}
        suma_consignaciones = {suma_consignaciones_estudiante}
        edad_minima_retiro = {edad_minima_retiro_estudiante}
        edad_minima_info = {edad_minima_info_estudiante}
        edad_minima_consignacion  = {edad_minima_consignacion_estudiante}{bcolors.RESET}
        """)
        return False
    return True
def caso2_aprobado(function_to_test):
    #ENTRADAS
    cola_general = [
    cliente("Matt",21,235000,"caja","retirar",100000,0),
    cliente("Dan",32,658000,"caja","retirar",98000,0),
    cliente("Steve",22, 34000,"caja","consignar", 0, 20000),
    cliente("Diana",29,87000,"info","ninguna",0,0),
    cliente("Cris",21, 87000,"caja","consignar", 0, 77000),
    cliente("Jorge",41, 987000,"caja","retirar", 400000, 0)
    ]
    
    #SALIDAS CORRECTAS
    cola_caja_correcta = ['Matt', 'Dan', 'Steve', 'Cris', 'Jorge']
    cola_info_correcta = ['Diana']
    suma_retiros_correcta = 598000
    suma_consignaciones_correcta = 97000
    edad_minima_retiro_correcta = 21
    edad_minima_info_correcta = 29
    edad_minima_consignacion_correcta  = 21
    
    #SALIDAS ESTUDIANTE
    cola_caja_estudiante = function_to_test(cola_general)[0]
    cola_info_estudiante = function_to_test(cola_general)[1]
    suma_retiros_estudiante = function_to_test(cola_general)[2]
    suma_consignaciones_estudiante = function_to_test(cola_general)[3]
    edad_minima_retiro_estudiante = function_to_test(cola_general)[4]
    edad_minima_info_estudiante = function_to_test(cola_general)[5]
    edad_minima_consignacion_estudiante  = function_to_test(cola_general)[6]
    
    if not (cola_caja_correcta == cola_caja_estudiante and cola_info_correcta == cola_info_estudiante and suma_retiros_correcta == suma_retiros_estudiante and suma_consignaciones_correcta == suma_consignaciones_estudiante and edad_minima_retiro_correcta == edad_minima_retiro_estudiante and edad_minima_info_correcta == edad_minima_info_estudiante and edad_minima_consignacion_correcta == edad_minima_consignacion_estudiante):
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        ENTRADA: 
        cola_general = {cola_general}
        {bcolors.OK}SALIDA ESPERADA:
        cola_caja = {cola_caja_correcta}
        cola_info = {cola_info_correcta}
        suma_retiros = {suma_retiros_correcta}
        suma_consignaciones = {suma_consignaciones_correcta}
        edad_minima_retiro = {edad_minima_retiro_correcta}
        edad_minima_info = {edad_minima_info_correcta}
        edad_minima_consignacion  = {edad_minima_consignacion_correcta}{bcolors.RESET}
        {bcolors.FAIL}TU SALIDA: 
        cola_caja = {cola_caja_estudiante}
        cola_info = {cola_info_estudiante}
        suma_retiros = {suma_retiros_estudiante}
        suma_consignaciones = {suma_consignaciones_estudiante}
        edad_minima_retiro = {edad_minima_retiro_estudiante}
        edad_minima_info = {edad_minima_info_estudiante}
        edad_minima_consignacion  = {edad_minima_consignacion_estudiante}{bcolors.RESET}
        """)
        return False
    return True

def caso3_aprobado(function_to_test):
    #ENTRADAS
    cola_general = [
    cliente("Matt",21,235000,"caja","retirar",100000,0),
    cliente("Dan",32,658000,"caja","retirar",98000,0),
    cliente("Steve",22, 34000,"caja","consignar", 0, 20000),
    cliente("Diana",29,87000,"info","ninguna",0,0),
    cliente("Cris",21, 87000,"caja","consignar", 0, 77000),
    cliente("Jorge",41, 987000,"caja","retirar", 400000, 0),
    cliente("Rosa",35, 2340000,"info","ninguna", 0, 0),
    cliente("Sherlock",41, 5340000,"caja","retirar", 2345000, 0)
    ]
    
    #SALIDAS CORRECTAS
    cola_caja_correcta = ['Matt', 'Dan', 'Steve', 'Cris', 'Jorge', 'Sherlock']
    cola_info_correcta = ['Diana', 'Rosa']
    suma_retiros_correcta = 2943000
    suma_consignaciones_correcta = 97000
    edad_minima_retiro_correcta = 21
    edad_minima_info_correcta = 29
    edad_minima_consignacion_correcta  = 21
    
    #SALIDAS ESTUDIANTE
    cola_caja_estudiante = function_to_test(cola_general)[0]
    cola_info_estudiante = function_to_test(cola_general)[1]
    suma_retiros_estudiante = function_to_test(cola_general)[2]
    suma_consignaciones_estudiante = function_to_test(cola_general)[3]
    edad_minima_retiro_estudiante = function_to_test(cola_general)[4]
    edad_minima_info_estudiante = function_to_test(cola_general)[5]
    edad_minima_consignacion_estudiante  = function_to_test(cola_general)[6]
    
    if not (cola_caja_correcta == cola_caja_estudiante and cola_info_correcta == cola_info_estudiante and suma_retiros_correcta == suma_retiros_estudiante and suma_consignaciones_correcta == suma_consignaciones_estudiante and edad_minima_retiro_correcta == edad_minima_retiro_estudiante and edad_minima_info_correcta == edad_minima_info_estudiante and edad_minima_consignacion_correcta == edad_minima_consignacion_estudiante):
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        ENTRADA: 
        cola_general = {cola_general}
        {bcolors.OK}SALIDA ESPERADA:
        cola_caja = {cola_caja_correcta}
        cola_info = {cola_info_correcta}
        suma_retiros = {suma_retiros_correcta}
        suma_consignaciones = {suma_consignaciones_correcta}
        edad_minima_retiro = {edad_minima_retiro_correcta}
        edad_minima_info = {edad_minima_info_correcta}
        edad_minima_consignacion  = {edad_minima_consignacion_correcta}{bcolors.RESET}
        {bcolors.FAIL}TU SALIDA: 
        cola_caja = {cola_caja_estudiante}
        cola_info = {cola_info_estudiante}
        suma_retiros = {suma_retiros_estudiante}
        suma_consignaciones = {suma_consignaciones_estudiante}
        edad_minima_retiro = {edad_minima_retiro_estudiante}
        edad_minima_info = {edad_minima_info_estudiante}
        edad_minima_consignacion  = {edad_minima_consignacion_estudiante}{bcolors.RESET}
        """)
        return False
    return True
def caso4_aprobado(function_to_test):
    #ENTRADAS
    cola_general = [
    cliente("Matt",21,235000,"caja","retirar",100000,0),
    cliente("Dan",32,658000,"caja","retirar",98000,0),
    cliente("Steve",22, 34000,"caja","retirar", 10000, 0),
    cliente("Diana",29,87000,"info","ninguna",0,0),
    cliente("Cris",21, 87000,"caja","retirar", 85000, 0),
    cliente("Jorge",41, 987000,"caja","retirar", 400000, 0),
    cliente("Rosa",35, 2340000,"info","ninguna", 0, 0),
    cliente("Sherlock",41, 5340000,"caja","retirar", 2345000, 0)
    ]
    
    #SALIDAS CORRECTAS
    cola_caja_correcta = ['Matt', 'Dan', 'Steve', 'Cris', 'Jorge', 'Sherlock']
    cola_info_correcta = ['Diana', 'Rosa']
    suma_retiros_correcta = 3038000
    suma_consignaciones_correcta = 0
    edad_minima_retiro_correcta = 21
    edad_minima_info_correcta = 29
    edad_minima_consignacion_correcta  = -1
    
    #SALIDAS ESTUDIANTE
    cola_caja_estudiante = function_to_test(cola_general)[0]
    cola_info_estudiante = function_to_test(cola_general)[1]
    suma_retiros_estudiante = function_to_test(cola_general)[2]
    suma_consignaciones_estudiante = function_to_test(cola_general)[3]
    edad_minima_retiro_estudiante = function_to_test(cola_general)[4]
    edad_minima_info_estudiante = function_to_test(cola_general)[5]
    edad_minima_consignacion_estudiante  = function_to_test(cola_general)[6]
    
    if not (cola_caja_correcta == cola_caja_estudiante and cola_info_correcta == cola_info_estudiante and suma_retiros_correcta == suma_retiros_estudiante and suma_consignaciones_correcta == suma_consignaciones_estudiante and edad_minima_retiro_correcta == edad_minima_retiro_estudiante and edad_minima_info_correcta == edad_minima_info_estudiante and edad_minima_consignacion_correcta == edad_minima_consignacion_estudiante):
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        ENTRADA: 
        cola_general = {cola_general}
        {bcolors.OK}SALIDA ESPERADA:
        cola_caja = {cola_caja_correcta}
        cola_info = {cola_info_correcta}
        suma_retiros = {suma_retiros_correcta}
        suma_consignaciones = {suma_consignaciones_correcta}
        edad_minima_retiro = {edad_minima_retiro_correcta}
        edad_minima_info = {edad_minima_info_correcta}
        edad_minima_consignacion  = {edad_minima_consignacion_correcta}{bcolors.RESET}
        {bcolors.FAIL}TU SALIDA: 
        cola_caja = {cola_caja_estudiante}
        cola_info = {cola_info_estudiante}
        suma_retiros = {suma_retiros_estudiante}
        suma_consignaciones = {suma_consignaciones_estudiante}
        edad_minima_retiro = {edad_minima_retiro_estudiante}
        edad_minima_info = {edad_minima_info_estudiante}
        edad_minima_consignacion  = {edad_minima_consignacion_estudiante}{bcolors.RESET}
        """)
        return False
    return True
def caso5_aprobado(function_to_test):
    #ENTRADAS
    cola_general = [
    cliente("Matt",21,235000,"caja","consignar",0,100000),
    cliente("Dan",32,658000,"caja","consignar",0,98000),
    cliente("Steve",22, 34000,"caja","consignar", 0, 10000),
    cliente("Diana",29,87000,"info","ninguna",0,0),
    cliente("Cris",21, 87000,"caja","consignar", 0, 85000),
    cliente("Jorge",41, 987000,"caja","consignar", 400000, 400000),
    cliente("Rosa",35, 2340000,"info","ninguna", 0, 0),
    cliente("Sherlock",41, 5340000,"caja","consignar", 0, 2345000)
    ]
    
    #SALIDAS CORRECTAS
    cola_caja_correcta = ['Matt', 'Dan', 'Steve', 'Cris', 'Jorge', 'Sherlock']
    cola_info_correcta = ['Diana', 'Rosa']
    suma_retiros_correcta = 0
    suma_consignaciones_correcta = 3038000
    edad_minima_retiro_correcta = -1
    edad_minima_info_correcta = 29
    edad_minima_consignacion_correcta  = 21
    
    #SALIDAS ESTUDIANTE
    cola_caja_estudiante = function_to_test(cola_general)[0]
    cola_info_estudiante = function_to_test(cola_general)[1]
    suma_retiros_estudiante = function_to_test(cola_general)[2]
    suma_consignaciones_estudiante = function_to_test(cola_general)[3]
    edad_minima_retiro_estudiante = function_to_test(cola_general)[4]
    edad_minima_info_estudiante = function_to_test(cola_general)[5]
    edad_minima_consignacion_estudiante  = function_to_test(cola_general)[6]
    
    if not (cola_caja_correcta == cola_caja_estudiante and cola_info_correcta == cola_info_estudiante and suma_retiros_correcta == suma_retiros_estudiante and suma_consignaciones_correcta == suma_consignaciones_estudiante and edad_minima_retiro_correcta == edad_minima_retiro_estudiante and edad_minima_info_correcta == edad_minima_info_estudiante and edad_minima_consignacion_correcta == edad_minima_consignacion_estudiante):
        print(f"""{bcolors.WARNING}
        ¡INCORRECTO!{bcolors.RESET}
        ENTRADA: 
        cola_general = {cola_general}
        {bcolors.OK}SALIDA ESPERADA:
        cola_caja = {cola_caja_correcta}
        cola_info = {cola_info_correcta}
        suma_retiros = {suma_retiros_correcta}
        suma_consignaciones = {suma_consignaciones_correcta}
        edad_minima_retiro = {edad_minima_retiro_correcta}
        edad_minima_info = {edad_minima_info_correcta}
        edad_minima_consignacion  = {edad_minima_consignacion_correcta}{bcolors.RESET}
        {bcolors.FAIL}TU SALIDA: 
        cola_caja = {cola_caja_estudiante}
        cola_info = {cola_info_estudiante}
        suma_retiros = {suma_retiros_estudiante}
        suma_consignaciones = {suma_consignaciones_estudiante}
        edad_minima_retiro = {edad_minima_retiro_estudiante}
        edad_minima_info = {edad_minima_info_estudiante}
        edad_minima_consignacion  = {edad_minima_consignacion_estudiante}{bcolors.RESET}
        """)
        return False
    return True