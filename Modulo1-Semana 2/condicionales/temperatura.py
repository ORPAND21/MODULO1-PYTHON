
temperatura = float(input("Ingresa los grados que te encuentras: "))

if temperatura < 0:
    print("Congelación")
elif 0 <= temperatura <= 10: 
    print("Muy frío")
elif 11 <= temperatura <= 20:  
    print("Frío")
elif 21 <= temperatura <= 30:  
    print("Agradable")
else:  
    print("Caluroso")