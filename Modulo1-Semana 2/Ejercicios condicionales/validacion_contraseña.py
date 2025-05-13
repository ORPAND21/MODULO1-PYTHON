contraseña = input("Crea una contraseña :")

contador = 0
for caracter in contraseña:
    contador += 1

# Verificar si cumple con los requisitos
if contador < 8:
    print("Contraseña muy corta")
elif '@' not in contraseña:
    print("La contraseña debe incluir al menos un '@'")
else:
    print("Contraseña válida")