primer_numero_ingresado = float(input("Ingrese el primer numero: "))
segundo_numero_ingresado = float(input("Ingrese el segundo numero: "))

operacion = input("Escriba tipo de operacion: ")

# PROCEDIMIENTO Y SALIDA 


# Si operacion = "suma" entonces

if operacion == "suma":
    resultado = primer_numero_ingresado + segundo_numero_ingresado
    
if operacion == "resta":
    resultado = primer_numero_ingresado - segundo_numero_ingresado
    
if operacion == "multiplicacion":
    resultado = primer_numero_ingresado * segundo_numero_ingresado

print(f"El resultado de la {operacion} es :" , resultado )
# Salida de datos  


