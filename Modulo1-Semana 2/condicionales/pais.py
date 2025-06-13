def continente ():
    paises = {
        "argentina":"America",
        "brasil":"America",
        "chile":"America",
        "ecuador":"America",
        "canada":"America",
        "españa":"Europa",
        "inglatera":"Europa",
        "dinamarca":"Europa",
        "china":"Asia",
        "japon":"Asia",
        "egipto":"Africa",
        "marruecos":"Africa"        
    }
    pais = input("Ingresa tu pais natal: ")

    if pais in paises:
        print(f"Tu pais se encuentra en el continente {paises[pais]}")
    else:
        print("Continente desconocido")
continente()
    
