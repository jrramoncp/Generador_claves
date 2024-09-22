import random

MAYUSCULAS = "ABCDEFJHIJKLMNOPQRSTUVWKYZ"
MINUSCULAS = "abcdefjhijlkmnoprqstuvwkyz"
ESPECIALES = "$%&€@#+Ç"
NUMEROS = "1234567890"

password = ""

# 1. Decidir los requisitos de la contraseña

# longitud = int(input("¿De que tamaño deseas la contraseña?"))
decidir_especial = input("¿Deseas que tu contraseña incluya caracteres especiales?")
decidir_numero = input("¿Deseas que tu contraseña incluya números?")

# 2. Generar la contraseña

def caracter_aleatorio(especial, numero): 
    caracter = ""
    if especial.lower() == "si":
        if numero == "si":
            aleatorio = random.randint(1,8)
            if aleatorio == 1 or aleatorio == 8:
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
            elif aleatorio == 2 or aleatorio == 7:
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
            elif aleatorio == 3 or aleatorio == 6: 
                caracter = ESPECIALES[random.randint(0, (len(ESPECIALES)-1))]
            else: 
                caracter = NUMEROS[random.randint(0, len(NUMEROS))]
        else: 
            aleatorio = random.randint(1,6)
            if aleatorio == 1 or aleatorio == 6:
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
            elif aleatorio == 2 or aleatorio == 5:
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
            else:
                caracter = ESPECIALES[random.randint(0, (len(ESPECIALES)-1))]
    if especial.lower() == "no": 
        if numero == "si":
            aleatorio = random.randint(1,6)
            if aleatorio == 1 or aleatorio == 6:
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
            elif aleatorio == 2 or aleatorio == 5:
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
            else:
                caracter = NUMEROS[random.randint(0, (len(NUMEROS)-1))]
        if numero == "no":
            aleatorio = random.randint(1,4)
            if aleatorio == 1 or aleatorio == 4: 
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))]
            else: 
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
                


    return caracter

print(caracter_aleatorio(decidir_especial, decidir_numero))
    
# def generar_contraseña(longitud, caracter): 
#     if caracter.lower() == "si": 
#         contraseña = ""
#         while len(contraseña) != longitud: 
            
#                 contraseña += 

# 3. Mostrar contraseña generada