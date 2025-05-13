def calculadora_aritmetica(operacion_aritmetica, number1, number2):
    
    resulatado_aritmetico = 0
    operacion_ejecutada = True
    mensaje = ""
    
    if operacion_aritmetica == "suma":
        resulatado_aritmetico = number1 + number2
    elif operacion_aritmetica == "resta":
        resulatado_aritmetico = number1 - number2
    elif operacion_aritmetica == "multiplicacion":
        resulatado_aritmetico = number1 * number2
    elif resulatado_aritmetico == "division":
        resulatado_aritmetico = number1 / number2
    else:
        operacion_ejecutada = False
        mensaje = "opcion invalida"
    return {
            "operacion_aritmetica": operacion_aritmetica,
            "resultado_aritmetico": resulatado_aritmetico,
            "mensaje": mensaje,
            "operacion_ejecutada": operacion_ejecutada
         }

##############################################################
numbe1 = int(input("Ingrese un valor :"))
numbe2 = int(input("Ingrese otro valor :"))
operacion = input("Escriba la operacion :")

resultado = calculadora_aritmetica(operacion,number1,number2)
print(resultado)

if resultado["operacion_ejecutada"]:
    print[resultado["resultado