number = int(input("Ingresa un numero entero: "))

if number>0:
    print("Es un numero positivo")
elif number<0:
    print("Es un numero negativo")
else:
    print("El numero es cero")


while number !=0:
    if number % 2 ==0:
        print("Es par")
    else:
        print("Es impar")
    break