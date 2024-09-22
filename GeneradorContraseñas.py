import random

MAYUSCULAS = "ABCDEFJHIJKLMNOPQRSTUVWKYZ" # Todas las letras mayusculas menos la ñ
MINUSCULAS = "abcdefjhijlkmnoprqstuvwkyz" # Todas las letras minusculas menos la ñ
ESPECIALES = "$%&€@#+Ç" # Caracteres especiales más importantes
NUMEROS = "1234567890" # Números enteros

# 1. Decidir los requisitos de la contraseña
''' Validacion para que si o si el usuario introduzca un número entero'''
longitud = 0 
while longitud == 0: 
    try:
        longitud = int(input("¿De que tamaño deseas la contraseña?: ")) # Tamaño de la contraseña
    except ValueError: 
        print("Tienes que introducir un número entero") # Si introducimos algo que no sea un entero, devuelve este mensaje pero no detiene la ejecucion

''' Validacion para que solo se pueda introducir si o no'''
validate_especial = False
while validate_especial == False:
    decidir_especial = input("Deseas que tu contraseña incluya caracteres especiales? (si|no): ") # Decidimos si queremos especiales o no
    if decidir_especial.lower() == "si" or decidir_especial == "no": 
        validate_especial = True
    else: 
        print("Tienes que escribir si o no") # Si introducimos algo diferente, devuelve el mensaje pero no detiene la ejecucion
        validate_especial = False

''' Validacion para que solo pueda introducir si o no'''
validate_number = False
while validate_number == False: 
    decidir_numero = input("¿Deseas que tu contraseña incluya números? (si|no): ") # Decidimos si queremos numeros o no
    if decidir_numero.lower() == "si" or decidir_numero == "no": 
        validate_number = True
    else: 
        print("Tienes que escribir si o no") # Si introducimos algo diferente, devuelve el mensaje pero no detiene la ejecucion
        validate_number = False


# 2. Generar caracter aleatorio

def caracter_aleatorio(especial, numero): 
    ''' Una funcion que devuelve un caracter aleatorio, dependiendo de nuestras elecciones en el paso anterior'''
    ''' Funciona con random, eligiendo numeros aleatorios asociados a cada decision y haciendo la eleccion sobre la longitud de la cadena'''
    
    caracter = ""
    if especial.lower() == "si": # Si elegimos que si queremos especiales y números
        if numero == "si": 
            aleatorio = random.randint(1,8) 
            if aleatorio == 1 or aleatorio == 8:
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
            elif aleatorio == 2 or aleatorio == 7:
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
            elif aleatorio == 3 or aleatorio == 6: 
                caracter = ESPECIALES[random.randint(0, (len(ESPECIALES)-1))]
            else: 
                caracter = NUMEROS[random.randint(0, len(NUMEROS) -1)]
        else: # Si queremos especiales, pero no numeros
            aleatorio = random.randint(1,6)
            if aleatorio == 1 or aleatorio == 6:
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
            elif aleatorio == 2 or aleatorio == 5:
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
            else:
                caracter = ESPECIALES[random.randint(0, (len(ESPECIALES)-1))]
    if especial.lower() == "no": # SI no queremos especiales, pero si numeros
        if numero == "si":
            aleatorio = random.randint(1,6)
            if aleatorio == 1 or aleatorio == 6:
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))] 
            elif aleatorio == 2 or aleatorio == 5:
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
            else:
                caracter = NUMEROS[random.randint(0, (len(NUMEROS)-1))]
        if numero == "no": # Si no queremos especiales ni numeros
            aleatorio = random.randint(1,4)
            if aleatorio == 1 or aleatorio == 4: 
                caracter = MAYUSCULAS[random.randint(0, (len(MAYUSCULAS)-1))]
            else: 
                caracter = MINUSCULAS[random.randint(0, (len(MINUSCULAS) -1))]
                


    return caracter # Devuelve el caracter aleatorio

# 3. Generar contraseña

def generar_contraseña(longitud): 
    ''' Una función que genera una contraseña, en funcion de la longitud elegida y va añadiendo caracteres aleatorios a una cadena vacía'''

    password = ""
    while len(password) < longitud: 
        password += caracter_aleatorio(especial= decidir_especial, numero= decidir_numero)
    
    return password
    


# 3. Mostrar contraseña generada

print("Aqui tienes tu contraseña")
print(generar_contraseña(longitud))