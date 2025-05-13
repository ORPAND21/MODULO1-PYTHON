x = float(input("Ingresa tu sueldo: "))
y = float(input("Ingresa el procentaje de aumento: "))

z = x * (y / 100)
a = x + z
print(f"Tu sueldo se le aplicado el procentaje {y:.0f}% ")
print(f"El sueldo actual {x:.0f}")
print(f"El sueldo aumentado es {a:.0f}")