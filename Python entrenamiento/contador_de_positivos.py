contador = 0

for i in range(10):
    number = int(input("Ingresa el numero: "))
    
    if number>0:
        contador +=1
print(f"Los numero mayores que cero son {contador}")