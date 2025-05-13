#Le damos la bienvenida al usuario 
print("Bienvenido a tu sistema de calificaciones")
print("Quieres saber tus notas?")

#Utilziamos un ciclo while para determinar la calificacion de el estudiante

while "Calificacion":
    try:
        calificacion = float(input("Ingresa una calificacion del 0 al 100 :"))
        if 0<= calificacion <= 100:
            break
        else:
            print("Valor no valido es un valor de 0 al 100")
    except:
        print("Ingresa un valor valido")


#Usamos el condicional para determinar si esta APROBADO o REPROBADO
if calificacion>=60:
    print(f"Con calificacion :{calificacion} Estas APROBADO")
else:
    print(f"Con calificacion :{calificacion} Estas REPROBADO")


#En este ciclo lo que hacemos es sacar el promedio y se condiciona para que el usuario no se salga del codigo
print("\nIngresa tus calificaciones para sacar el promedio")

while True:
    notas = input("\nColoca las calificaciones separadas por comas (0-100): ").split(",")

    try:
        valores = [float(n.strip()) for n in notas]
        if all(0 <= n <= 100 for n in valores):
            promedio = sum(valores) / len(valores)
            print(f"Promedio: {promedio:.1f}")
            break
        else:
            print("Solo notas entre 0 y 100")
    except:
        print("Ingrese solo números")
        
        
#Cuales son mayores determinando una media que desea el usuario y cual esta por encima 
while True:
    try:
        valor = float(input("\nIngrese un valor para contar calificaciones mayores: "))
        if 0 <= valor <= 100:
            break
        else:
            print("Error: El valor debe estar entre 0 y 100")
    except:
        print("Error: Ingrese un valor numérico válido")

contador = 0
i = 0
while i < len(valores):
    if valores [i] > valor:
        contador += 1
    i += 1
    
print(f"Hay {contador} calificaciones mayores que {valor}")

#Verificar los valores y buscamos cual calificacion se repite y el usuario la pueda ver cuantas calificaciones tiene el mismo valor
while True:
        try:
            buscar = float(input("\nIngrese una calificación específica a buscar: "))
            if 0 <= buscar <= 100:
                break
            else:
                print("Error: La calificación debe estar entre 0 y 100")
        except:
            print("Error: Ingrese un valor numérico válido")

encontrado = False
conteo = 0
for cal in valores:
    if cal == buscar:
        encontrado = True
        conteo += 1
        continue  # Continúa para contar todas las ocurrencias
    else:
        continue
if encontrado:
    print(f"La calificación {buscar} aparece {conteo} veces en la lista")
else:
    print(f"La calificación {buscar} no se encuentra en la lista")