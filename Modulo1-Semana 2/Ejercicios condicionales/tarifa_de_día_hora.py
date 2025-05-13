

si= "S"
no= "N"
hora = int(input("Cuantas horas trabajaste :"))

print("Ingrese si su dia es laborable S/N")
dia = input(f"Ingresa({si} / {no} ):")



if dia == no:
    print("Fin de semana")
elif dia == si:
    if 7 <= hora <= 9 or 17 <= hora <= 19:
        print("Pico")
    else:
        print("Normal")
else:
    print("Entrada no válida. Debe ingresar S o N.")
