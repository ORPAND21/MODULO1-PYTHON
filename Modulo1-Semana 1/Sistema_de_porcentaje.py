#Sistema de para descuentos en una tienda 
# Le damos la bienvenidad al usuario

print("----Hola Bienvenido a la mejor Tienda---- ")
print("  ")

#Datos del cliente 

cliente = input("Ingresa tu nombre: ")
print("  ")


#Le preguntamos que desea
print("--Que desesas comprar hoy?----")
print("  ")


#Le pedimos el producto al usuario

producto = input("Cual es tu producto: ")

 
#Hacemos un blucle while para determinar si los datos son correctos
#Validacion de precio

while True:
    try:
        precio = float(input("Cual es el precio del producto: "))
        if precio >0:
            break
        print("Error: La cantidad debe se mayor que 0")
    except:
        print("Error: Ingrese un valor valido")

#Validacion de cantidad
while True:
    try:
        cantidad = int(input("Que cantidad va a llevar: "))
        if cantidad >0:
            break
        print("Error: La cantidad debe se mayor que 0")
    except:
        print("Error: Ingrese un valor valido")     
        
#Validacion de descuento
        
while True:
    try:
        descuento = float(input("Que descuento quieres Aplicar (0 si no aplica) : "))
        if descuento >=0 and descuento<=100:
            break
        print("Error: La cantidad debe se mayor que 0 y menor o igual que 100")
    except:
        print("Error: Ingrese un valor valido")
print("  ")
print("  ")  


#Mostrar Resumen de la compra
print("/==============FACTURA============/")
print("  ")
print(f"Cliente: {cliente}")
print(f"Tu producto es: {producto}")
print(f"El precio del producto es: ${precio:.2f}")
print(f"La cantidad que vas a llevar es: {cantidad:.0f}")


# Indicamos si el producto tiene descuento
if descuento>0:
    print(f"Se a aplicado el descuento y es de: {descuento:.0f}% ")
else:
    print("No aplica el descuento")


#Calculamos los precios importantes
subcosto = precio * cantidad
valor_descuento = subcosto * (descuento /100)   
total_pagar = subcosto - valor_descuento

#Indicamos el precio total
print("=-----------------------------=")
print(f"TOTAL A PAGAR = ${total_pagar:.2f}")
print(f"{producto} =  ${total_pagar:.2f}")
print("=-----------------------------=")


#Ingresamos para motivar al cliente a seguir comprando

if total_pagar >100:
    print("Gracias por su compra mayorista!")
elif total_pagar >50:
    print("¡Gracias por su compra!")
else:
    print("¡Gracias por preferirnos!")
    

