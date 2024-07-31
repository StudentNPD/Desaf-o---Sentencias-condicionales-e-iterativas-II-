import itertools
from string import ascii_lowercase

# La contraseña que estamos tratando de adivinar
contraseña = input("ingrese contraseña: ")

def fuerza_bruta(contraseña):
    intentos = 0
    # Genera todas las combinaciones posibles de 1 a la longitud de la contraseña
    for length in range(1, len(contraseña) + 1):# Genera todas las combinaciones posibles de 1 a la longitud de la contraseña
        for intento in itertools.product(ascii_lowercase, repeat=length): #genera los intentos
            intentos += 1 #genera el numero en los intentos
            intento_contra = ''.join(intento) #aqui toma la lista de intentos y la convierte en cadena para manejar los intentos de forma contable
            print(f"Intento {intentos}: {intento_contra}") #este imprime los intentos junto a los que va generando
            if intento_contra == contraseña: #este corta el ciclo he imprime el final
                print(f"Contraseña encontrada: {intento_contra} en {intentos} intentos") #imprime la contraseña junto a los intentos
                return

fuerza_bruta(contraseña)