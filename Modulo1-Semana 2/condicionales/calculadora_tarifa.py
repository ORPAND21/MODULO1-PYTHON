tarifa = float(input("Ingresa tu tarifa: "))
print("Ingresa tu tipo de cliente")
print("normal")
print("premium")
print("vip")
tipo = input("Ingresa tu tipo de cliente: ")


if tipo == "normal":
    descuento = 0.05
elif tipo == "premium":
    descuento = 0.10
elif tipo == "vip":
    descuento = 0.20
else:
    print("Tipo de cliente no identificado")


tarifa_final = tarifa*(1-descuento)
print(f"Tu tarifa {tarifa_final} de {tipo}")