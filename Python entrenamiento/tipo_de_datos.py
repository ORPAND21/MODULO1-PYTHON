data = input("Ingrese un valor numerico: ")
data2 = input("Ingrese un segundo valor numerico: ")
contador = 0

try:
    data = int(data)
except:
    print("no se puede realizar esta operacion")
    contador = contador + 1
   
    
try:
    data2 = int(data2)
except:
    print("no se puede realizar esta operacion")
    contador = contador + 1
 
print("La cantidad de errores es: ", contador)