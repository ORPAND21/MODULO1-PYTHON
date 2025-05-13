edad = int(input("Ingresa tu edad :"))

if edad>=0 and edad<=18:
    print("Eres menor de edad")
elif edad>=18 and edad<=30:
    print("Eres un adulto")
elif edad>=31 and edad<=64:
    print("Adulto maduro")
elif edad>=65:
    print("Adulto mayor")
else:
    print("ingresa una edad valida")