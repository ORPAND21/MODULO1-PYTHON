
contador = 0 
for i in range(10):
    numero = float(input("ingrasa un numero: "))
    if i >0:
        contador += 1
        
print(f"\nDe los 10 números ingresados, {contador} son mayores que cero.")