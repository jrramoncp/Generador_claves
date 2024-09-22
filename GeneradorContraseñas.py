import random

MAYUSCULAS = "ABCDEFJHIJKLMNOPQRSTUVWKYZ"
MINUSCULAS = "abcdefjhijlkmnoprqstuvwkyz"
ESPECIALES = "$%&€@#+Ç"

password = ""

# 1. Decidir los requisitos de la contraseña

# longitud = int(input("¿De que tamaño deseas la contraseña?"))
# espec_char = input("¿Deseas que tu contraseña incluya caracteres especiales?")

# 2. Generar la contraseña

def caracter_aleatorio(): 
    caracter = ""
    
    aleatorio = random.randint(1,9)
    if aleatorio == 1 or aleatorio == 4 or aleatorio == 7:
        caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
    elif aleatorio == 2 or aleatorio == 5 or aleatorio == 8:
        caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
    else: 
        caracter = ESPECIALES[random.randint(0, (len(ESPECIALES)-1))]
    return caracter

print(caracter_aleatorio())
    
# def generar_contraseña(longitud, caracter): 
#     if caracter.lower() == "si": 
#         contraseña = ""
#         while len(contraseña) != longitud: 
            
#                 contraseña += 

# 3. Mostrar contraseña generada