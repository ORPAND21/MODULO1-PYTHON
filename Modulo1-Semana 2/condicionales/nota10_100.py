nota = float(input("Ingresa una nota 0-100: "))
if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 80 and nota <= 89:
    print("Muy bueno")
elif nota >=70 and nota <=79: 
    print("Bueno") 
elif nota >=60 and nota <=69: 
    print("Regular")
elif nota < 60: 
    print("Reprobado")
else:
    print("Tiene que ser un numero de 0-100")    