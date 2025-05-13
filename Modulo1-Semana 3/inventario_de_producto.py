# Diccionario para almacenar el inventario {nombre: (precio, cantidad)}
almancen = {}
# Hacemos la funcion añadir_producto para validar y perdile al usuario los datos del producto para añadir
def anadir_producto():
    nombre_producto = input("Ingresa tu producto: ")
    if nombre_producto in almancen:
       print("¡Este producto ya existe!")
       return
   
    try:
        precio = float(input("Ingresa el precio de tu producto: "))
        cantidad = int(input("Ingresa la cantidad que deseas llevar de tu producto: "))
        
        if precio <=0 or cantidad <0:
            print("!El precio y cantidad deben ser valores positivos¡")
            return
        almancen [nombre_producto] = (precio, cantidad)
        print(f"Producto '{nombre_producto}' añadido correctamente.")
    except:
        print("Valores invalidos")

# Función para buscar producto y condicinar si el producto es el mismo
def buscar_producto():
    nombre_producto = input("Escribe el nombre a buscar : ")
    
    if nombre_producto in almancen:
        precio, cantidad = almancen[nombre_producto]
        print(f"\nProducto: {nombre_producto}")
        print(f"Precio: ${precio:.2f}")
        print(f"Cantidad disponible: {cantidad}")
    else:
        print("¡Producto no encontrado en el inventario!")
        

#Función para actualizar el precio de un producto
def actualizar_precio():
    nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
    
    if nombre_producto not in almancen:
        print("¡Producto no encontrado!")
        return
    
    try:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("¡Error! El precio debe ser un valor positivo.")
            return
            
        # Actualizamos solo el precio, manteniendo la cantidad
        cantidad = almancen[nombre_producto][1]
        almancen[nombre_producto] = (nuevo_precio, cantidad)
        print(f"Precio de '{nombre_producto}' actualizado correctamente.")
    except:
        print("¡Error! Ingrese un valor numérico válido para el precio.")

# Función para eliminar un producto
def eliminar_producto():
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
    
    if nombre_producto in almancen:
        del almancen[nombre_producto]
        print(f"Producto '{nombre_producto}' eliminado correctamente.")
    else:
        print("¡Producto no encontrado!")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    # Usamos una función lambda para calcular el valor por producto
    calcular_valor = lambda item: item[1][0] * item[1][1]
    
    if not almancen:
        print("El inventario está vacío.")
        return
    
    total = sum(calcular_valor(item) for item in almancen.items())
    print(f"\nValor total del inventario: ${total:.2f}")
    print(f"Cantidad de productos distintos: {len(almancen)}")

# Función principal que maneja el menú
while True:
    print("\n--- GESTIÓN DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Buscar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("6. Salir")
        
    opcion = input("Seleccione una opción (1-6): ")
        
    if opcion == "1":
        anadir_producto()
    elif opcion == "2":
        buscar_producto()
    elif opcion == "3":
        actualizar_precio()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        calcular_valor_total()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
