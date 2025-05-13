monto = float(input("Ingresa el monto de su compra :"))

no = "N"
si = "S"
descuento = 0
condicion = input(f"Si eres VIP ({si}) y No VIP ({no}) :")

if condicion == no:
     if monto>=500:
        descuento = 0.05
        print("No eres VIP pero tienes un descuento de 10%")
     else:
        print("No eres VIP y no tienes descuento ;-; ")

elif condicion == si:
   if monto>=500:
      descuento = 0.20
      print("Eres VIP y tienes un descuento de 20%")
   else:
      descuento = 0.10
      print("Eres VIP y tienes un descuento de 10%")


monto_final = monto * (1 - descuento)

print(f"Tu monto final es: {monto_final:.0f}")